"""
app.py — camada WEB do Escriba (FastAPI).

Esta camada NAO reimplementa nada: ela reaproveita os modulos de src/
(repo_reader, prompts, llm_client) e so faz o "trabalho de garcom":

    1. recebe a URL de um repositorio publico do GitHub
    2. clona o repo (raso) numa pasta temporaria
    3. usa src/ pra gerar README.md e CHANGELOG.md como TEXTO
    4. devolve tudo em JSON pro navegador (a landing) mostrar

A chave da Groq fica no servidor (variavel de ambiente GROQ_API_KEY),
NUNCA no navegador. Por isso precisa existir um backend: sem ele, a chave
vazaria pra qualquer um que abrisse a pagina.

Rodar local:
    cd web
    pip install -r requirements.txt
    uvicorn app:app --reload --port 8000
"""

import re
import sys
import time
import shutil
import tempfile
import subprocess
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# --- deixa importar os modulos que estao em ../src ---------------------------
SRC = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC))

from repo_reader import listar_arquivos, ler_conteudo_arquivos, pegar_git_log  # noqa: E402
from prompts import prompt_readme, prompt_changelog, SYSTEM_PROMPT             # noqa: E402
from llm_client import chamar_llm                                             # noqa: E402

# --- limites de seguranca (repos grandes / abuso) ----------------------------
# A Groq no plano gratuito aceita ~12.000 tokens POR MINUTO. Como 1 token ~= 4
# chars e o /gerar faz ate 2 chamadas no mesmo minuto (README + CHANGELOG),
# precisamos manter o contexto folgado abaixo disso. ~24000 chars ~= 6000 tokens.
MAX_ARQUIVOS = 40           # nao manda o repo inteiro pra LLM
MAX_CHARS_POR_ARQUIVO = 1500  # trecho de cada arquivo (antes eram 3000)
MAX_CHARS_CONTEXTO = 24000  # teto total de contexto (protege custo/tempo/limite Groq)
CLONE_TIMEOUT = 90          # segundos pra clonar
GIT_DEPTH = 50              # commits recentes bastam pro changelog

app = FastAPI(title="Escriba API", description="Gera README/CHANGELOG de um repo publico.")

# libera o fetch a partir da landing (GitHub Pages / arquivo local / etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


class Pedido(BaseModel):
    repo: str
    readme: bool = True
    changelog: bool = True


def normalizar_url_github(entrada: str) -> str:
    """
    Aceita 'github.com/user/repo', 'https://github.com/user/repo',
    'user/repo' e devolve uma URL https limpa e clonavel.
    Recusa qualquer coisa que nao seja um repo do GitHub (evita SSRF/caminho local).
    """
    txt = entrada.strip()
    txt = re.sub(r"^https?://", "", txt)
    txt = re.sub(r"^www\.", "", txt)
    txt = txt.rstrip("/")
    txt = re.sub(r"\.git$", "", txt)

    if txt.startswith("github.com/"):
        txt = txt[len("github.com/"):]

    # agora deve sobrar 'user/repo'
    m = re.fullmatch(r"([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)", txt)
    if not m:
        raise HTTPException(
            status_code=400,
            detail="URL invalida. Use um repositorio publico do GitHub, ex: github.com/user/repo",
        )
    return f"https://github.com/{m.group(1)}/{m.group(2)}.git"


def clonar(url: str, destino: str) -> None:
    """Clona raso (poucos commits, sem historico gigante)."""
    try:
        resultado = subprocess.run(
            ["git", "clone", "--depth", str(GIT_DEPTH), url, destino],
            capture_output=True, text=True, timeout=CLONE_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=504, detail="O clone demorou demais. Tente um repo menor.")
    if resultado.returncode != 0:
        raise HTTPException(
            status_code=404,
            detail="Nao consegui clonar. O repo existe e e publico?",
        )


def montar_contexto(caminho_repo: str) -> tuple[str, int]:
    """Usa src/ pra ler os arquivos, mas com teto de quantidade/tamanho."""
    arquivos = listar_arquivos(caminho_repo)
    qtd_total = len(arquivos)
    arquivos = arquivos[:MAX_ARQUIVOS]
    conteudo = ler_conteudo_arquivos(arquivos, max_chars=MAX_CHARS_POR_ARQUIVO)
    if len(conteudo) > MAX_CHARS_CONTEXTO:
        conteudo = conteudo[:MAX_CHARS_CONTEXTO] + "\n\n[...contexto truncado...]"
    return conteudo, qtd_total


def gerar_com_llm(prompt: str) -> str:
    """
    Chama a Groq tratando os erros mais comuns (repo grande demais / limite do
    plano gratuito). Sem isso, a excecao subiria e viraria um HTTP 500 mudo.
    """
    try:
        return chamar_llm(prompt, system=SYSTEM_PROMPT)
    except Exception as e:
        msg = str(e).lower()
        # 413/429 da Groq: passou do teto de tokens por minuto (TPM)
        if "rate_limit" in msg or "too large" in msg or "tokens per minute" in msg:
            raise HTTPException(
                status_code=429,
                detail="Repo grande demais para o plano gratuito da Groq (limite de tokens). "
                       "Tente um repositorio menor ou aguarde um minuto.",
            )
        raise HTTPException(status_code=502, detail="A IA falhou ao gerar o texto. Tente de novo.")


@app.get("/")
def raiz():
    return {"ok": True, "servico": "Escriba API", "use": "POST /gerar {repo, readme, changelog}"}


@app.post("/gerar")
def gerar(pedido: Pedido):
    url = normalizar_url_github(pedido.repo)
    inicio = time.time()

    tmp = tempfile.mkdtemp(prefix="escriba_")
    try:
        clonar(url, tmp)

        contexto, qtd_arquivos = montar_contexto(tmp)
        log = pegar_git_log(tmp, qtd_commits=GIT_DEPTH)
        n_commits = len([l for l in log.splitlines() if l.strip()])

        resposta = {
            "repo": url.replace("https://github.com/", "").replace(".git", ""),
            "readme": None,
            "changelog": None,
        }

        if pedido.readme:
            prompt = prompt_readme(contexto + "\n\nCommits:\n" + log)
            resposta["readme"] = gerar_com_llm(prompt)

        if pedido.changelog:
            prompt = prompt_changelog(log)
            resposta["changelog"] = gerar_com_llm(prompt)

        resposta["stats"] = {
            "arquivos": qtd_arquivos,
            "commits": n_commits,
            "segundos": round(time.time() - inicio, 1),
        }
        return resposta
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

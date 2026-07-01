"""
repo_reader: responsavel por LER o repositorio.

Este modulo NAO fala com a LLM. Ele so coleta contexto (arquivos + commits)
e devolve isso como texto pronto pra ser colocado num prompt.

Divida em 3 tarefas:
    - listar_arquivos()       -> quais arquivos existem
    - ler_conteudo_arquivos() -> o que tem dentro deles (um trecho)
    - pegar_git_log()         -> historico de commits recentes
"""

import subprocess
from pathlib import Path

# Pastas que nao interessam pra documentacao (evite mandar isso pra LLM)
PASTAS_IGNORADAS = {".git", "node_modules", "__pycache__", ".venv", "venv"}

# Extensoes de codigo que valem a pena olhar (ajuste como quiser)
EXTENSOES_CODIGO = {".py", ".js", ".ts", ".java", ".go", ".rb", ".md"}


def listar_arquivos(caminho_repo):
    """
    Percorre o repositorio e devolve uma lista dos arquivos relevantes.

    Dicas:
    - Use Path(caminho_repo).rglob("*") pra percorrer tudo recursivamente.
    - Pule qualquer arquivo que esteja dentro de uma PASTA_IGNORADA.
    - Filtre por EXTENSOES_CODIGO pra nao pegar imagem, binario, etc.
    - Retorne uma lista de objetos Path (ou de strings, voce escolhe).
    """
    # TODO: implementar
    pass


def ler_conteudo_arquivos(lista_de_arquivos, max_chars=3000):
    """
    Le o conteudo dos arquivos (ou so um trecho) pra dar contexto pra LLM.

    Dicas:
    - Nao mande arquivos gigantes inteiros: corte em 'max_chars' por arquivo.
    - Junte tudo num texto so, marcando o nome de cada arquivo antes do conteudo.
      Ex:
          === src/main.py ===
          <conteudo aqui...>
    - Cuidado com encoding: use open(arquivo, encoding="utf-8", errors="ignore").
    - Retorne uma string unica.
    """
    # TODO: implementar
    pass


def pegar_git_log(caminho_repo, qtd_commits=20):
    """
    Roda 'git log' no repositorio e devolve os commits recentes como texto.

    Dicas:
    - Use subprocess.run(
          ["git", "-C", caminho_repo, "log", f"-{qtd_commits}",
           "--pretty=format:%h %s (%an)"],
          capture_output=True, text=True, encoding="utf-8"
      )
    - O texto do log fica em resultado.stdout.
    - Se o repo nao tiver git, trate o erro e retorne uma string vazia ou aviso.
    """
    # TODO: implementar
    pass

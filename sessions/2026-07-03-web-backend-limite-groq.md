# 2026-07-03 — Backend web (FastAPI) + correção do limite de tokens da Groq

## Contexto
A landing (`docs/index.html`) deixou de ser demo simulada e passou a chamar um backend real. Nesta sessão o foco foi: (1) diagnosticar por que alguns repositórios "não geravam" a documentação pela web e (2) commitar a camada web que estava pronta mas fora do controle de versão.

## O que foi decidido / feito
- **Diagnóstico do bug "um repo vai, outro não":** ao testar `github.com/renatoodlo/Automatizacao_estoque` (funciona) vs `github.com/GustavoGurtler/projetores-demo` (não vai), reproduzi o erro real da Groq:
  `413 - Request too large ... tokens per minute (TPM): Limit 12000, Requested 12497`.
  Causa: o plano gratuito da Groq aceita **~12.000 tokens por minuto**. O repo `projetores-demo` tem 25 arquivos relevantes (~15k tokens de contexto) contra 3 arquivos (~1,5k) do outro — então estoura o teto. Como o `chamar_llm` não tratava erro, virava HTTP 500 mudo na landing.
- **Correção em `web/app.py`:**
  - `MAX_CHARS_CONTEXTO`: `45000 → 24000` e novo `MAX_CHARS_POR_ARQUIVO = 1500` (antes 3000/arquivo). Segura o pedido abaixo do teto, contando as **duas** chamadas (README + CHANGELOG) no mesmo minuto.
  - Novo helper `gerar_com_llm()` que traduz os erros 413/429 da Groq numa resposta **HTTP 429 amigável** ("repo grande demais para o plano gratuito"), em vez de 500.
- **Verificação real:** rodei a pipeline com os limites novos contra `projetores-demo` — gerou README + CHANGELOG corretos (~6.367 tokens, dentro do limite, 3,9s). ✅

## Detalhes técnicos da camada web (que estava sem commit)
- `web/app.py` — backend **FastAPI**. Reaproveita `src/` (repo_reader, prompts, llm_client). Endpoint `POST /gerar`: recebe URL de repo público → clona raso em pasta temporária → monta contexto (com tetos) → devolve README/CHANGELOG em JSON. Chave da Groq fica **no servidor**. `normalizar_url_github()` recusa qualquer coisa que não seja `user/repo` do GitHub (anti-SSRF). CORS liberado pra landing chamar.
- `web/requirements.txt` — deps do backend (fastapi, uvicorn, etc.), separado do `requirements.txt` do CLI.
- `docs/index.html` — deixou de simular: agora faz `fetch(API_BASE + '/gerar')`, renderiza o Markdown real (mini-conversor md→html), mostra stats reais (arquivos/commits/tempo) e tem caixa de erro amigável. `API_BASE` = `127.0.0.1:8000` em dev; a URL de produção ainda é um placeholder (`TROCAR-PELA-URL-DO-BACKEND`) até o deploy.

## Git desta sessão (Lucas pediu pro Claude commitar — exceção)
- `caff2e7 feat(web): adiciona backend FastAPI que gera docs de repo publico`
- `fb20bed feat(landing): conecta a demo da landing ao backend real`
- (+ esta sessão/pendências como commit `docs:`)

## Estado ao fechar (atualizado — sessão retomada/fechada em 2026-07-04)
- Backend + landing + docs **commitados** (`caff2e7`, `fb20bed`, `8c1b68b`).
- ✅ **Push feito** — `master` sincronizado com `origin/master`.
- ✅ **Backend validado rodando LOCAL** (`uvicorn app:app --app-dir web --host 127.0.0.1 --port 8000`): `projetores-demo` → HTTP 200, README + CHANGELOG gerados.
- 🔀 **Decisão: rodar só local, sem nuvem/VPS** (combina com "custo zero"). Os itens de deploy em nuvem + `API_BASE` de produção ficaram **PAUSADOS** no `pendencias.md` (pausados, não descartados — só valem se o Lucas quiser a demo pública).
- ⚠️ Loose end desta retomada: a atualização do `pendencias.md` (run-local ✅ + itens de nuvem pausados) + este próprio arquivo ainda precisam de **commit** (o Lucas commita).
- Rebrand "Escriba" segue não propagado para README/badges; GitHub Pages ainda não ligado.

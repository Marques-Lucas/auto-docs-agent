# 🤖 Auto Docs Agent

Agente em Python que **lê um repositório de código, analisa os arquivos e o histórico de commits (`git log`) e gera automaticamente a documentação** (`README.md` e `CHANGELOG.md`) usando uma LLM.

> **Problema:** documentar dá preguiça, e a maioria dos projetos fica com um README pela metade.
> **Solução:** deixar a IA rascunhar a documentação a partir do próprio código, para o dev só revisar.

> ✅ **Status:** MVP **funcionando de ponta a ponta**. Todos os cinco módulos (`main`, `repo_reader`, `llm_client`, `prompts`, `doc_generator`) estão implementados e o agente já gerou `README.md` + `CHANGELOG.md` reais a partir de um repositório de teste, usando a Groq. Consulte o [Roadmap](#-roadmap) para os próximos passos (evoluções pós-MVP).

---

## ✨ Funcionalidades

- 📖 **Leitura do repositório** — percorre os arquivos de código relevantes, ignorando pastas de ruído (`.git`, `node_modules`, `__pycache__`, `venv`…).
- 🕓 **Análise de histórico** — coleta os commits recentes via `git log`.
- 🧠 **Geração por LLM** — envia o contexto para o modelo e recebe a documentação em Markdown.
- 📝 **Escrita automática** — salva `README.md` (e, como bônus, `CHANGELOG.md`) direto no repositório-alvo.
- 🔌 **Provedor de LLM isolado** — trocar de Groq para outro provedor mexe em um único arquivo (`llm_client.py`).

---

## 🧱 Stack

| Camada        | Tecnologia                                             |
| ------------- | ------------------------------------------------------ |
| Linguagem     | Python 3                                               |
| LLM           | [Groq](https://groq.com) (Llama 3.3 70B, plano free)   |
| Configuração  | [python-dotenv](https://pypi.org/project/python-dotenv/) |
| Histórico     | Git (`git log`)                                        |

---

## 📁 Estrutura do projeto

```
auto-docs-agent/
├── README.md              # este arquivo
├── requirements.txt       # dependências (groq, python-dotenv)
├── .env.example           # modelo do .env (copie para .env e ponha sua chave)
├── .gitignore
└── src/
    ├── main.py            # ponto de entrada (CLI)
    ├── repo_reader.py     # lê arquivos + git log (não fala com a LLM)
    ├── llm_client.py      # única parte que fala com a Groq (fácil de trocar)
    ├── prompts.py         # os moldes de prompt (README e CHANGELOG)
    └── doc_generator.py   # orquestra: contexto → prompt → LLM → escreve arquivos
```

---

## 🔄 Como funciona

```
main.py
   └─► repo_reader     → lê os arquivos + git log do repositório-alvo
   └─► prompts         → monta o pedido para a IA
   └─► llm_client      → envia para a Groq e recebe o texto
   └─► doc_generator   → salva o README.md / CHANGELOG.md
```

Cada módulo tem uma responsabilidade única, o que mantém o `llm_client` (o único acoplado ao provedor de LLM) trocável sem afetar o resto.

---

## 🚀 Instalação e uso

**Pré-requisitos:** Python 3 e Git instalados, e uma API key gratuita da Groq.

```bash
# 1. Clonar o repositório
git clone <url-do-repo>
cd auto-docs-agent

# 2. (Opcional) criar e ativar um ambiente virtual
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Configurar a chave
#    - copie .env.example para .env
#    - cole sua GROQ_API_KEY (pegue em https://console.groq.com/keys)
```

Rodando o agente apontando para um repositório qualquer:

```bash
python src/main.py <caminho_do_repositorio>

# Exemplo (Windows):
python src/main.py C:\Projetos\meu-projeto
```

Ao final, o `README.md` (e opcionalmente o `CHANGELOG.md`) é gerado dentro do repositório indicado.

---

## ⚙️ Configuração

As variáveis ficam no arquivo `.env` (veja `.env.example`):

| Variável        | Descrição                                    | Padrão                     |
| --------------- | -------------------------------------------- | -------------------------- |
| `GROQ_API_KEY`  | Sua chave da Groq (obrigatória)              | —                          |
| `GROQ_MODEL`    | Modelo usado na geração                      | `llama-3.3-70b-versatile`  |

> 🔒 O `.env` está no `.gitignore` — **nunca** suba sua API key.

---

## 🗺️ Roadmap

- [x] `llm_client.py` — implementar `chamar_llm()` (base de tudo)
- [x] `repo_reader.py` — `listar_arquivos()`, `ler_conteudo_arquivos()`, `pegar_git_log()`
- [x] `prompts.py` — `prompt_readme()` e `prompt_changelog()`
- [x] `doc_generator.py` — `gerar_readme()`, `gerar_changelog()`, `salvar_arquivo()`
- [x] `main.py` — conectar o CLI (ler o caminho de `sys.argv`)
- [x] Testar em um repositório pequeno (comparar antes/depois) — **funcionou de ponta a ponta com a Groq real** (02/07/2026)

### Evoluções (pós-MVP)

- Rodar como **GitHub Action** a cada `push`
- Sugerir **testes faltando**
- Integrar com **n8n** (executar o agente por webhook)

---

## 📄 Licença

Defina a licença do projeto (ex.: MIT) e adicione um arquivo `LICENSE`.

---

*Projeto de portfólio — construído aprendendo, commit por commit.*

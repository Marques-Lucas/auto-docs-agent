# 🤖 Auto Docs Agent

> **Um agente de IA que lê um repositório de código e escreve a documentação por você.**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![LLM](https://img.shields.io/badge/LLM-Groq%20·%20Llama%203.3%2070B-F55036)
![Custo](https://img.shields.io/badge/custo-R%240%20(plano%20free)-2ea44f)
![Status](https://img.shields.io/badge/status-MVP%20funcional-success)
![License](https://img.shields.io/badge/license-MIT-green)

Agente em Python que **lê um repositório de código, analisa os arquivos e o histórico de commits (`git log`) e gera automaticamente a documentação** (`README.md` e `CHANGELOG.md`) usando uma LLM — a **custo zero**, com o plano gratuito da Groq.

> **Problema:** documentar dá preguiça, e a maioria dos projetos fica com um README pela metade.
> **Solução:** deixar a IA rascunhar a documentação a partir do próprio código, para o dev só revisar.

---

## 🎬 Demonstração

<!-- TODO (Lucas): gravar um GIF do agente rodando e colocar em docs/demo.gif -->
<!-- Dica: use https://asciinema.org ou o ScreenToGif (Windows) e salve como docs/demo.gif -->
<!-- Depois é só descomentar a linha abaixo: -->
<!-- ![Auto Docs Agent em ação](docs/demo.gif) -->

Rodando o agente contra um repositório qualquer:

```bash
$ python src/main.py C:\Projetos\repo-de-teste
Lendo o repositorio em: C:\Projetos\repo-de-teste
README gerado em: C:\Projetos\repo-de-teste\README.md
CHANGELOG gerado em: C:\Projetos\repo-de-teste\CHANGELOG.md
Pronto!
```

<details>
<summary><b>📥 Entrada</b> — um repositório de exemplo (uma calculadora, 2 arquivos + 4 commits)</summary>

```
repo-de-teste/
├── requirements.txt
└── src/
    ├── calculadora.py   # somar, subtrair, multiplicar, dividir
    └── main.py          # CLI que chama as operações

$ git log --oneline
docs: adiciona requirements com flask
fix: trata divisao por zero na funcao dividir
feat: adiciona multiplicar e dividir
feat: cria calculadora com somar e subtrair
```
</details>

<details open>
<summary><b>📤 Saída</b> — o <code>README.md</code> gerado pela IA, sozinha</summary>

```markdown
# Calculadora Simples de Linha de Comando
Este projeto implementa uma calculadora simples que opera somas,
subtrações, multiplicações e divisões via linha de comando.

## Stack / Tecnologias Usadas
* Python

## Como Instalar e Rodar o Projeto
Para rodar o projeto, é necessário ter Python instalado no sistema.
Execute o arquivo `main.py` passando a operação e os dois números:
    python src/main.py soma 2 3

## Estrutura de Pastas e Principais Arquivos
* `src/`: pasta contendo o código-fonte do projeto
  + `calculadora.py`: funções de cálculo (somar, subtrair, multiplicar, dividir)
  + `main.py`: recebe os argumentos da linha de comando e chama as funções
```
</details>

<details>
<summary><b>📤 Saída</b> — o <code>CHANGELOG.md</code> gerado a partir do <code>git log</code></summary>

```markdown
# CHANGELOG
## Novidades
* Adicionada calculadora com somar e subtrair
* Adicionadas funcoes multiplicar e dividir
* Adicionados requirements com flask

## Correcoes
* Corrigida divisao por zero na funcao dividir
```
</details>

> 💡 Repare que o agente **não inventou** que o projeto usa Flask (o pacote estava no `requirements.txt`, mas não é usado no código). Isso é garantido por instrução explícita no *system prompt* — ver [Destaques técnicos](#-destaques-técnicos).

---

## ✨ Funcionalidades

- 📖 **Leitura do repositório** — percorre os arquivos de código relevantes, ignorando pastas de ruído (`.git`, `node_modules`, `__pycache__`, `venv`…).
- 🕓 **Análise de histórico** — coleta os commits recentes via `git log`.
- 🧠 **Geração por LLM** — envia o contexto para o modelo e recebe a documentação em Markdown.
- 📝 **Escrita automática** — salva `README.md` e `CHANGELOG.md` direto no repositório-alvo.
- 🔌 **Provedor de LLM isolado** — trocar de Groq para outro provedor mexe em um único arquivo (`llm_client.py`).

---

## 🔄 Como funciona

```
main.py  (CLI)
   │
   ├─►  repo_reader     lê os arquivos + git log do repositório-alvo
   ├─►  prompts         monta o pedido (o "molde" de texto) para a IA
   ├─►  llm_client      envia para a Groq e recebe o texto
   └─►  doc_generator   orquestra tudo e escreve o README.md / CHANGELOG.md
```

Cada módulo tem **uma responsabilidade única**, o que mantém o `llm_client` (o único acoplado ao provedor de LLM) trocável sem afetar o resto.

---

## 🧱 Stack

| Camada        | Tecnologia                                             |
| ------------- | ------------------------------------------------------ |
| Linguagem     | Python 3                                               |
| LLM           | [Groq](https://groq.com) (Llama 3.3 70B, plano free)   |
| Configuração  | [python-dotenv](https://pypi.org/project/python-dotenv/) |
| Histórico     | Git (`git log` via `subprocess`)                       |

---

## 🚀 Instalação e uso

**Pré-requisitos:** Python 3 e Git instalados, e uma API key gratuita da Groq ([pegue aqui](https://console.groq.com/keys)).

```bash
# 1. Clonar o repositório
git clone https://github.com/Marques-Lucas/auto-docs-agent.git
cd auto-docs-agent

# 2. Criar e ativar um ambiente virtual
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Configurar a chave
#    - copie .env.example para .env
#    - cole sua GROQ_API_KEY dentro
```

Rodando o agente apontando para um repositório qualquer:

```bash
python src/main.py <caminho_do_repositorio>

# Exemplo (Windows):
python src/main.py C:\Projetos\meu-projeto
```

Ao final, o `README.md` e o `CHANGELOG.md` são gerados dentro do repositório indicado.

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

## 🧠 Destaques técnicos

Decisões de arquitetura que guiaram o projeto:

- **Separação de responsabilidades (SoC).** Cada módulo faz uma coisa só. O `repo_reader` nunca fala com a IA; o `llm_client` nunca lê arquivos. Isso deixa o código fácil de testar e de entender.
- **Provedor de LLM plugável.** Toda a conversa com a IA vive em `llm_client.py`. Trocar Groq por OpenAI, Gemini ou um modelo local é mexer em **um arquivo só** — o resto do agente nem percebe.
- **Prompts fora do código.** Os "moldes" de texto ficam isolados em `prompts.py`, então dá pra afinar a qualidade da saída sem tocar na lógica.
- **Anti-alucinação.** O *system prompt* instrui o modelo a usar **apenas** o que está no contexto e a não inventar informação — comprovado no teste, em que a IA ignorou uma dependência declarada mas não usada.
- **Testável sem gastar API.** O fluxo foi validado substituindo a chamada real por um *mock*, confirmando a "encanação" (ler → montar prompt → salvar) sem consumir cota da LLM.
- **Custo zero.** Roda inteiro no plano gratuito da Groq — alinhado à proposta de ser uma ferramenta acessível para qualquer dev.

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

- [x] `llm_client.py` — `chamar_llm()` (a base: fala com a Groq)
- [x] `repo_reader.py` — `listar_arquivos()`, `ler_conteudo_arquivos()`, `pegar_git_log()`
- [x] `prompts.py` — `prompt_readme()` e `prompt_changelog()`
- [x] `doc_generator.py` — `gerar_readme()`, `gerar_changelog()`, `salvar_arquivo()`
- [x] `main.py` — CLI que lê o caminho de `sys.argv`
- [x] **Teste de ponta a ponta com a Groq real** ✅

### Evoluções (pós-MVP)

- [ ] Rodar como **GitHub Action** a cada `push`
- [ ] Sugerir **testes faltando** para o código
- [ ] Integrar com **n8n** (executar o agente por webhook)
- [ ] Flag de linha de comando para escolher o que gerar (`--readme` / `--changelog`)

---

## 👤 Autor

**Lucas Marques** — projeto de portfólio, construído aprendendo Python e Git na prática, commit por commit.

- GitHub: [@Marques-Lucas](https://github.com/Marques-Lucas)
<!-- TODO (Lucas): adicione seu LinkedIn e/ou e-mail de contato aqui -->
<!-- - LinkedIn: https://linkedin.com/in/seu-perfil -->

---

## 📄 Licença

Distribuído sob a licença **MIT** — veja o arquivo [`LICENSE`](LICENSE) para os detalhes.
</content>
</invoke>

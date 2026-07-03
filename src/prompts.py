"""
prompts: os "moldes" de texto que mandamos pra LLM.

Manter os prompts separados da logica facilita muito ajustar o resultado
(voce vai mexer bastante aqui pra afinar a qualidade do README).
"""

SYSTEM_PROMPT = (
    "Voce e um assistente que escreve documentacao tecnica clara e objetiva "
    "para repositorios de codigo. Responda SEMPRE em portugues e em Markdown, "
    "sem inventar informacoes que nao estejam no contexto fornecido."
)


def prompt_readme(contexto_do_repo):
    """
    Monta o prompt que pede um README a partir do contexto coletado.

    'contexto_do_repo' e o texto que veio do repo_reader
    (estrutura de arquivos + trechos de codigo + git log).

    Dica: peca explicitamente as secoes que voce quer, por exemplo:
        - Titulo e descricao curta do projeto
        - Stack / tecnologias usadas
        - Como instalar e rodar
        - Estrutura de pastas
    Termine o prompt colando o 'contexto_do_repo'.
    """
    texto = f"""Escreva um arquivo README.md completo, em portugues e em Markdown,
para o projeto descrito no contexto abaixo.

Inclua obrigatoriamente estas secoes:
- Titulo do projeto e uma descricao curta do que ele faz
- Stack / tecnologias usadas
- Como instalar (dependencias) e como rodar o projeto
- Estrutura de pastas e principais arquivos

Regras:
- Use apenas informacoes presentes no contexto; nao invente nada.
- Se alguma informacao nao existir no contexto, apenas omita a secao.
- Responda somente com o conteudo do README em Markdown, sem comentarios extras.

Contexto do repositorio:
{contexto_do_repo}
"""
    return texto


def prompt_changelog(git_log):
    """
    Monta o prompt que transforma o git log num CHANGELOG.md organizado.

    Dica: peca pra agrupar as mudancas (ex: Novidades, Correcoes, Melhorias)
    e usar o formato de changelog com data/versao se der.
    """
    texto = f"""Gere um arquivo CHANGELOG.md em portugues e em Markdown a partir
do historico de commits (git log) fornecido abaixo.

Regras:
- Agrupe as mudancas por tipo: Novidades, Correcoes e Melhorias.
- Reescreva cada commit em uma linha curta e clara para o usuario final.
- Quando houver datas no historico, use-as para organizar as entradas.
- Use apenas informacoes presentes no git log; nao invente nada.
- Responda somente com o conteudo do CHANGELOG em Markdown, sem comentarios extras.

Historico de commits (git log):
{git_log}
"""
    return texto

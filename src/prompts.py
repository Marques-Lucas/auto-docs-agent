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
    # TODO: retornar a string do prompt
    pass


def prompt_changelog(git_log):
    """
    Monta o prompt que transforma o git log num CHANGELOG.md organizado.

    Dica: peca pra agrupar as mudancas (ex: Novidades, Correcoes, Melhorias)
    e usar o formato de changelog com data/versao se der.
    """
    # TODO: retornar a string do prompt
    pass

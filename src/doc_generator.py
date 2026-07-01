"""
doc_generator: o "cerebro" que junta tudo.

Pega o contexto (repo_reader) -> monta o prompt (prompts) ->
chama a LLM (llm_client) -> ESCREVE os arquivos de documentacao.

Este e o modulo que amarra os outros. Comece por gerar_readme().
"""

from pathlib import Path

# TODO: descomente quando os outros modulos estiverem prontos
# from repo_reader import listar_arquivos, ler_conteudo_arquivos, pegar_git_log
# from llm_client import chamar_llm
# from prompts import prompt_readme, prompt_changelog, SYSTEM_PROMPT


def gerar_readme(caminho_repo):
    """
    Orquestra a geracao do README.md.

    Passo a passo sugerido:
        1. arquivos  = listar_arquivos(caminho_repo)
        2. conteudo  = ler_conteudo_arquivos(arquivos)
        3. log       = pegar_git_log(caminho_repo)
        4. contexto  = conteudo + "\\n\\nCommits:\\n" + log
        5. prompt    = prompt_readme(contexto)
        6. texto     = chamar_llm(prompt, system=SYSTEM_PROMPT)
        7. salvar_arquivo(Path(caminho_repo) / "README.md", texto)
    """
    # TODO: implementar
    pass


def gerar_changelog(caminho_repo):
    """
    Mesma ideia do gerar_readme, mas monta o CHANGELOG.md a partir do git log.
    """
    # TODO: implementar
    pass


def salvar_arquivo(caminho_destino, conteudo):
    """
    Helper simples pra escrever um arquivo de texto no disco.

    Dica: Path(caminho_destino).write_text(conteudo, encoding="utf-8")
    """
    # TODO: implementar
    pass

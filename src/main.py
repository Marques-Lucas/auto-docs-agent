"""
Ponto de entrada do Auto Docs Agent.

Uso (no terminal):
    python src/main.py <caminho_do_repositorio>

Exemplo:
    python src/main.py C:\\Projetos\\meu-projeto-de-teste

Fluxo geral (o que este arquivo deve orquestrar):
    1. Pegar o caminho do repositorio que o usuario passou no terminal
    2. Chamar o repo_reader pra ler estrutura + git log
    3. Chamar o doc_generator pra gerar o README (e opcionalmente o CHANGELOG)
    4. Avisar onde os arquivos foram salvos
"""

import sys

# TODO: descomente estes imports quando os modulos estiverem prontos
# from doc_generator import gerar_readme, gerar_changelog


def main():
    # TODO 1: pegar o caminho do repositorio de sys.argv.
    #         - sys.argv[0] e o nome do script; o caminho vem em sys.argv[1].
    #         - Se o usuario nao passar nada, mostre uma mensagem de ajuda e de sys.exit().

    # TODO 2: chame gerar_readme(caminho) do doc_generator.

    # TODO 3 (opcional): chame gerar_changelog(caminho) tambem.

    # TODO 4: imprima no terminal uma mensagem tipo "README gerado em ...".
    print("Auto Docs Agent - esqueleto ainda vazio. Preencha os TODOs :)")


if __name__ == "__main__":
    main()

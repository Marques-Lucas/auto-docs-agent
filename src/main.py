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

from doc_generator import gerar_readme, gerar_changelog


def main():
    # 1. Pega o caminho do repositorio que veio no terminal.
    #    sys.argv[0] e o nome do script; o caminho vem em sys.argv[1].
    if len(sys.argv) < 2:
        print("Uso: python src/main.py <caminho_do_repositorio>")
        sys.exit(1)

    caminho = sys.argv[1]

    # 2. Gera o README a partir do repositorio.
    print(f"Lendo o repositorio em: {caminho}")
    caminho_readme = gerar_readme(caminho)
    print(f"README gerado em: {caminho_readme}")

    # 3. Gera o CHANGELOG a partir do git log.
    caminho_changelog = gerar_changelog(caminho)
    print(f"CHANGELOG gerado em: {caminho_changelog}")

    print("Pronto!")


if __name__ == "__main__":
    main()

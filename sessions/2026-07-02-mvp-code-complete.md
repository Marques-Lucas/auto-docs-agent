# 2026-07-02 — MVP code-complete (prompts + doc_generator + main)

## O que foi feito
Implementados os três módulos que faltavam, fechando o MVP em código:

- `src/prompts.py` — `prompt_readme()` e `prompt_changelog()` (montam o texto do pedido com f-string tripla e colam o contexto no fim). Também corrigido um bug de indentação na docstring do módulo (linha 1 estava recuada, o que causaria `IndentationError` no import).
- `src/doc_generator.py` — `gerar_readme()`, `gerar_changelog()` e `salvar_arquivo()`. É a peça que orquestra: `repo_reader` → `prompts` → `llm_client` → escreve o arquivo. Imports reais ativados no topo. Cada `gerar_*` retorna o `Path` do arquivo gerado.
- `src/main.py` — ponto de entrada (CLI). Lê o caminho de `sys.argv[1]`; se faltar argumento, imprime ajuda e `sys.exit(1)`. Chama `gerar_readme` e `gerar_changelog` e avisa onde salvou.

## Detalhe de decisão
- Nesta sessão o Lucas pediu explicitamente para o Claude **escrever o código no lugar dele** (exceção à regra padrão de só-scaffold). Os módulos anteriores (`llm_client`, `repo_reader`) ele escreveu à mão.
- `gerar_readme`/`gerar_changelog` retornam `Path` (não estava no scaffold) pra o `main.py` poder imprimir "gerado em X" sem recalcular.

## Testes
- Testado com a `chamar_llm` **mockada** (sem gastar chamada da Groq): a orquestração roda e grava `README.md` + `CHANGELOG.md` no diretório-alvo.
- `main.py` testado nos dois caminhos: com argumento (cria os arquivos) e sem argumento (mostra ajuda, exit 1).

## Estado / o que falta
- Código completo. **Ainda não commitado** (o Lucas commita).
- Falta o **teste real de ponta a ponta** apontando pra um repositório de verdade (aí sim gastando uma chamada da Groq).

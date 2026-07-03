# auto-docs-agent — regras compartilhadas para agentes de IA

Este arquivo é a fonte da verdade das regras de organização deste projeto.
É lido tanto pelo Claude/Cowork quanto pelo Antigravity (e qualquer outra
ferramenta compatível com o padrão AGENTS.md). Se você usa outra ferramenta
com um arquivo de overrides próprio (ex: `GEMINI.md` no Antigravity), coloque
lá só as particularidades daquela ferramenta — as regras gerais ficam aqui.

## Sobre o projeto
- Nome: auto-docs-agent
- Stack: Python + SDK oficial da Groq (`groq`) + `python-dotenv`
- Modelo padrão: `llama-3.3-70b-versatile` (configurável via `GROQ_MODEL` no `.env`)
- Segredos: chave `GROQ_API_KEY` no `.env` (nunca commitar; use `.env.example` como referência)

## Registro de sessões
Sempre que o usuário definir ou decidir algo importante numa sessão de trabalho
(ex: definição de tela, fluxo de organograma, de onde vêm os dados, estrutura de
banco de dados, tabelas a criar, arquitetura, regras de negócio etc.), registre
em um novo arquivo dentro de `/sessions/`.

- Nome do arquivo: `AAAA-MM-DD-titulo-curto-da-sessao.md` (ex: `2026-07-02-tela-login.md`)
- Conteúdo do arquivo:
  - Data e um título curto
  - O que foi decidido/definido (resumo objetivo, não precisa ser um relatório longo)
  - Detalhes técnicos relevantes (tabelas, campos, endpoints, componentes, etc.)
  - Se está feito, o que falta, ou se a decisão está completa

Não crie um arquivo de sessão para toda mensagem — só quando houver uma decisão
ou definição relevante para o projeto (algo que vale a pena lembrar depois).

## Pendências
Existe um arquivo único `/pendencias.md` na raiz do projeto.

- Sempre que o usuário disser algo como "adiciona isso nas pendências", "anota
  isso pra depois", "fica pendente" etc., adicione um item novo nesse arquivo,
  no formato:
  `- [ ] descrição da pendência (adicionado em AAAA-MM-DD, sessão: nome-do-arquivo-relacionado)`
- Sempre que o usuário disser "verifica as pendências", "o que ainda falta",
  "manda as pendências" etc., leia o arquivo inteiro e devolva a lista do que
  ainda está em aberto (itens não marcados), organizada de forma clara.
- Quando uma pendência for resolvida, NÃO apague a linha: marque como concluída
  trocando `[ ]` por `[x]` e adicione a data de conclusão. Isso mantém o histórico.
- Nunca deixe de registrar uma pendência nova só porque parece pequena — é
  melhor registrar demais do que esquecer.

## Disciplina de manutenção
Este arquivo (AGENTS.md) é a fonte da verdade da organização deste projeto.
Sempre que a estrutura de pastas, convenção de nomes, ou o processo de registro
mudar, atualize este arquivo também — não deixe a prática real divergir do que
está escrito aqui. Se em algum momento um agente perceber que parou de seguir
essas regras (ex: sessões não registradas, pendências não atualizadas), avise o
usuário e corrija antes de continuar.

## MCP / conectores compartilhados
O GitHub MCP está configurado no Antigravity usando o servidor remoto oficial
do GitHub (via web, `https://api.githubcopilot.com/mcp/`), não o servidor
local via Docker — o Docker Desktop desta máquina não conseguia iniciar o
engine, então a versão web evita essa dependência.

Isso está configurado em dois lugares (o mesmo conteúdo, por consistência):

- Global do Antigravity: `~/.gemini/config/mcp_config.json` — é este que o
  Antigravity realmente usa hoje (confirmado: aparece como "github-mcp-server"
  com 44 tools habilitadas em Settings → Customizations → Installed MCP Servers).
- Local do projeto: `.agents/mcp_config.json` (nesta pasta) — mantido como
  referência/backup caso o Antigravity passe a priorizar config de projeto.

Ambos os arquivos contêm o token do GitHub em texto puro
(`Authorization: Bearer ghp_...`) — por isso `.agents/mcp_config.json` está no
`.gitignore`. Nunca remova essa linha nem suba esse arquivo com o token real
para o repositório. Se o token vazar, revogue em
https://github.com/settings/tokens e gere outro.

Não configuramos um servidor de "filesystem" — o Antigravity já tem acesso
nativo aos arquivos do projeto como IDE, então um MCP de filesystem seria
redundante.

O Cowork usa seus próprios conectores (gerenciados nas configurações do app) —
não há um arquivo de projeto equivalente a sincronizar automaticamente, então
conectores lá precisam ser configurados separadamente, direto no app.

# Regras de organização deste projeto

## Registro de sessões
Sempre que eu (o usuário) definir ou decidir algo importante nesta sessão de trabalho
(por exemplo: definição de tela, fluxo de organograma, de onde vem os dados,
estrutura de banco de dados, tabelas a criar, arquitetura, regras de negócio etc.),
registre em um novo arquivo dentro de `/sessions/`.

- Nome do arquivo: `AAAA-MM-DD-titulo-curto-da-sessao.md`
  (ex: `2026-07-02-tela-login.md`)
- Conteúdo do arquivo:
  - Data e um título curto
  - O que foi decidido/definido (resumo objetivo, não precisa ser um relatório longo)
  - Detalhes técnicos relevantes (tabelas, campos, endpoints, componentes, etc.)
  - Está feito ainda o que falta ou se decisão está completa

Não crie um arquivo de sessão para toda mensagem — só quando houver uma decisão ou
definição relevante para o projeto (algo que vale a pena lembrar depois).

## Pendências
Existe um arquivo único `/pendencias.md` na raiz do projeto.

- Sempre que eu disser algo como "adiciona isso nas pendências", "anota isso pra
  depois", "fica pendente" etc., adicione um item novo nesse arquivo, no formato:
  `- [ ] descrição da pendência (adicionado em AAAA-MM-DD, sessão: nome-do-arquivo-relacionado)`
- Sempre que eu disser "verifica as pendências", "o que ainda falta", "manda as
  pendências" etc., leia o arquivo inteiro e me devolva a lista do que ainda está
  em aberto (itens não marcados), organizada de forma clara.
- Quando uma pendência for resolvida, NÃO apague a linha: marque como concluída
  trocando `[ ]` por `[x]` e adicione a data de conclusão. Isso mantém o histórico.
- Nunca deixe de registrar uma pendência nova só porque parece pequena — é melhor
  registrar demais do que esquecer.

## Disciplina de manutenção
Este arquivo (CLAUDE.md) é a fonte da verdade da organização deste projeto.
Sempre que a estrutura de pastas, convenção de nomes, ou o processo de registro
mudar, atualize este arquivo também — não deixe a prática real divergir do que
está escrito aqui. Se em algum momento você perceber que parou de seguir essas
regras (ex: sessões não registradas, pendências não atualizadas), avise o usuário
e corrija antes de continuar.

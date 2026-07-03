# 2026-07-03 — Landing page + nome "Escriba" (protótipo web)

## O que foi decidido
- **Nome do projeto (branding):** o produto passa a se chamar **Escriba** (escriba = quem escreve por você). Decisão de branding/marketing; o repositório ainda se chama `auto-docs-agent` (rename para `escriba` ficou como pendência, não executado).
- **Landing page:** criada uma página web de apresentação/protótipo em `docs/index.html`, pensada para publicação no **GitHub Pages** (pasta `/docs`), não como Artifact do Claude (para ter URL própria, fora do `claude.ai`).

## Detalhes técnicos
- `docs/index.html` — arquivo **standalone** (sem runtime externo). Identidade visual: fundo escuro `#15171D`, roxo `#A277FF` (aprovado pelo Lucas), apoio ciano/cyan e verde. Tema único escuro (decisão deliberada).
- Elementos: hero com demo interativo fake (cola URL → "gera" README/CHANGELOG com passos animados), usando o output real do teste da calculadora.
- Movimentos de destaque (v2): (1) canvas de "tinta viva" no fundo do herói; (2) README surgindo **bloco a bloco** ("Escriba escrevendo") com pena no canto; (3) tipografia serif *Instrument Serif* (via Google Fonts) no wordmark/títulos; traço de tinta desenhando-se sob o H1. Tudo com fallback para `prefers-reduced-motion`.
- Favicon: pena em SVG inline (sem dependência externa).
- Link "GitHub" da página aponta para `auto-docs-agent` (repo atual) — trocar se renomear.

## Também nesta leva (org compartilhada com Antigravity)
- Novo `AGENTS.md` na raiz = fonte da verdade das regras (sessões, pendências, manutenção, MCP), lido tanto pelo Claude/Cowork quanto pelo **Antigravity**.
- `CLAUDE.md` enxugado: agora só aponta para `AGENTS.md`.
- `.gitignore`: passou a ignorar `.agents/mcp_config.json` (contém token do GitHub em texto puro — nunca commitar).

## Estado / o que falta
- Landing feita e revisada localmente. **Deploy no GitHub Pages ainda não feito** (comandos prontos nas pendências).
- Também entrou nesta leva o README nível-portfólio + `LICENSE` (MIT) da sessão 06, que ainda não tinham sido commitados.
- Rebrand "Escriba" ainda **não** propagado para README/CLAUDE/badges (segue "Auto Docs Agent").

# 2026-07-06 — Exploração shadcn / MagicUI / 21st.dev + nova identidade da landing

## Contexto
Continuação da sessão dos efeitos ReactBits (ver `2026-07-06-reactbits-efeitos.md`).

## O que foi feito
- **Removido o efeito "Star Border"** (borda cônica girando no botão "Gerar documentação") do `docs/index.html` — feedback do Lucas ("não gostei desse negócio girando"). CSS, HTML e a regra de `prefers-reduced-motion` correspondentes foram removidos. Os demais efeitos ReactBits (Aurora, Shiny Text, Spotlight, Click Spark) permanecem.
- **Exploração** das tecnologias pedidas pelo Lucas (21st.dev, shadcn/ui, MagicUI) via protótipos em Artifact (NÃO no repo).

## Decisão técnica importante
- **shadcn/ui, 21st.dev e MagicUI são todos React + Tailwind.** Diferente do ReactBits (efeitos canvas/CSS recriáveis em vanilla), esses são componentes React de verdade (Radix, estado, Tailwind). Usá-los "de verdade" exige **migrar a landing para React + Vite + Tailwind** — o "caminho A" antes recusado.
- **Combinado:** prototipar a identidade primeiro (sem tocar no repo); só migrar para React quando o Lucas aprovar a direção visual.

## Protótipos (Artifacts, fora do repo)
1. **shadcn + MagicUI** em tema escuro/roxo (Dot Pattern, Retro Grid, Shimmer Button, Magic Card, Number Ticker, Marquee, Bento Grid) — Lucas achou que ainda tinha "cara de IA".
2. **Nova identidade "Escriba — Oficina de Documentação"**: direção **editorial/manuscrito** — papel greige + grão, tinta preta quente, rubrica (vermelho de anotação) parcimoniosa, ouro raro; tipografia **Palatino** (serifa humanista) × Consolas mono; grade de manuscrito assimétrica com fólios/marginália/capitular; movimento sóbrio (write-on da manchete, régua que traça, number ticker, marquee de espécimes). Sem roxo/gradiente/glow/rotação. shadcn/MagicUI re-tematizados nesse mundo.

## Estado / o que falta (decisões pendentes)
- **Identidade da landing:** 3 direções prototipadas; decisão pendente (favorita atual: a editorial/manuscrito). Pode-se explorar outra pegada (brutalista/terminal, suíço) se o Lucas quiser.
- **Migração para React** (Vite + Tailwind + shadcn + MagicUI + 21st.dev): **não iniciada** — só após aprovação da identidade.
- **"getdesign.md":** não reconhecido; aguardando o Lucas esclarecer o que é para incluir na exploração.
- **Commit:** `docs/index.html` (efeitos ReactBits sem Star Border) + `pendencias.md` + arquivos de `sessions/` aguardando commit do Lucas.

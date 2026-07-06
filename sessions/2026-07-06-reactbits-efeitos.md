# 2026-07-06 — Efeitos ReactBits na landing (Aurora + brilhos)

## O que foi decidido
- **Adotar o ReactBits** (biblioteca de efeitos visuais) na landing do Escriba.
- **Caminho de integração: B — recriar os efeitos em JS/CSS puro** dentro do `docs/index.html` atual, em vez de migrar a landing para React/Vite (caminho A).
  - Motivo: o ReactBits é uma lib de componentes **React**, mas a landing é um `index.html` standalone servido no GitHub Pages (sem build). O caminho B mantém "custo zero" / sem `node_modules` / sem passo de build, e o resultado visual é equivalente. O ReactBits vira "receita/inspiração", não uma dependência instalada.
- Fluxo: **protótipo interativo primeiro** (Artifact do Claude, com todos os efeitos ligáveis ao vivo) → Lucas escolheu → integração no repo. Frontend é 100% do Claude (Lucas hands-off).

## Efeitos integrados (em `docs/index.html`)
- **Aurora** (fundo) — substituiu o antigo "fundo de tinta viva" (blobs em canvas). Cortinas radiais roxo/ciano que flutuam no topo, via `createRadialGradient` + `requestAnimationFrame`. Reaproveita o mesmo `<canvas id="ink">`.
- **Shiny Text** — brilho deslizante no eyebrow ("Documentação gerada por IA…"), via `background-clip:text` + `@keyframes shine`. Classe `.eyebrow.shiny`.
- **Star Border** — borda cônica girando no botão "Gerar documentação". Pseudo-elemento `.starwrap::before` com `conic-gradient`, reaproveitando o keyframe `spin` já existente.
- **Spotlight** — luz radial que segue o cursor sobre o card `.composer` (camada `.spot`; JS escreve `--mx`/`--my`).
- **Click Spark** — faíscas radiais disparadas no clique do botão gerar (`clickSpark()`).

## Efeitos testados mas NÃO usados (ficaram só no protótipo)
- Fundo **Threads** (linhas fluidas) e título **Scramble/Decrypted Text** (letras se assentando). Disponíveis para uso futuro se quiser.

## Detalhes técnicos / integridade
- Todos os efeitos novos respeitam `prefers-reduced-motion` (bloco `@media` estendido: shiny/star desligados, aurora desenha 1 quadro estático).
- O backend/fetch e todo o fluxo de geração (`generate()`, steps, resultado) **não foram tocados** — só a camada visual.
- Verificação: `node --check` no `<script>` (sintaxe OK); confirmado que o fundo antigo (blobs) foi removido e os 5 efeitos estão presentes. Backup = Git (arquivo estava commitado limpo antes).
- Título mantém o gradiente/sublinhado atuais (Scramble não entrou).

## Estado / o que falta
- Efeitos integrados no `docs/index.html`. **NÃO commitado** — commit é do Lucas (ele roda `git add/commit/push`).
- Falta o Lucas **abrir a landing no navegador** e confirmar visualmente (os efeitos aparecem sem backend).
- Pendências antigas seguem: ligar GitHub Pages (`/docs`), rebrand "Escriba", decidir rename do repo.

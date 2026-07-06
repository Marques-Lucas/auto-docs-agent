# Pendências do projeto

<!-- Formato: - [ ] descrição (adicionado em AAAA-MM-DD, sessão: arquivo-relacionado) -->
<!-- Ao concluir, mude [ ] para [x] e adicione a data de conclusão -->

- [ ] Publicar a landing no GitHub Pages servindo a pasta `/docs` (adicionado em 2026-07-03, sessão: 2026-07-03-landing-escriba.md)
- [x] Rodar o backend `web/` (FastAPI) localmente e validar a demo de ponta a ponta (concluído em 2026-07-03: `uvicorn app:app --app-dir web --port 8000`; testado com projetores-demo → 200 OK, sessão: 2026-07-03-web-backend-limite-groq.md)
- [ ] (PAUSADO — Lucas prefere rodar local, sem nuvem/VPS) Fazer deploy do backend `web/` em host (Render/Railway/Fly) para a demo funcionar fora do localhost; só retomar se ele quiser a demo pública (adicionado em 2026-07-03, sessão: 2026-07-03-web-backend-limite-groq.md)
- [ ] (PAUSADO — depende do deploy em nuvem acima) Preencher a URL de produção em `API_BASE` no `docs/index.html` (hoje placeholder `TROCAR-PELA-URL-DO-BACKEND`) (adicionado em 2026-07-03, sessão: 2026-07-03-web-backend-limite-groq.md)
- [ ] (PAUSADO — depende do deploy em nuvem acima) Mencionar a demo web (link do Pages) no README de portfólio (adicionado em 2026-07-03, sessão: 2026-07-03-web-backend-limite-groq.md)
- [ ] Decidir se renomeia o repositório `auto-docs-agent` → `escriba` (muda a URL do Pages e o `origin`); se sim, atualizar o link "GitHub" da landing de volta para `/escriba` (adicionado em 2026-07-03, sessão: 2026-07-03-landing-escriba.md)
- [ ] Propagar o nome "Escriba" para o resto do projeto (README, CLAUDE.md, badges) — hoje ainda diz "Auto Docs Agent" (adicionado em 2026-07-03, sessão: 2026-07-03-landing-escriba.md)
- [ ] Decidir se embute a fonte Instrument Serif no HTML (100% offline) em vez de puxar do Google Fonts (adicionado em 2026-07-03, sessão: 2026-07-03-landing-escriba.md)
- [ ] Gravar `docs/demo.gif` do agente rodando e descomentar a linha do GIF no README (adicionado em 2026-07-02, sessão: 2026-07-02 README portfólio)
- [ ] Preencher LinkedIn/e-mail na seção "Autor" do README (adicionado em 2026-07-02, sessão: 2026-07-02 README portfólio)
- [x] Adotar ReactBits na landing: integrar efeitos Aurora + Shiny Text + Star Border + Spotlight + Click Spark em `docs/index.html` via JS/CSS puro, caminho B (concluído em 2026-07-06, sessão: 2026-07-06-reactbits-efeitos.md)
- [ ] Abrir `docs/index.html` no navegador e conferir visualmente os efeitos ReactBits; depois commitar (`M docs/index.html`) e dar push (adicionado em 2026-07-06, sessão: 2026-07-06-reactbits-efeitos.md)
- [x] Remover o efeito "Star Border" (borda girando no botão) da landing (concluído em 2026-07-06, sessão: 2026-07-06-exploracao-shadcn-magicui.md)
- [ ] Decidir a IDENTIDADE VISUAL da landing entre as direções prototipadas (favorita: editorial/manuscrito "Oficina de Documentação") ou explorar outra pegada (adicionado em 2026-07-06, sessão: 2026-07-06-exploracao-shadcn-magicui.md)
- [ ] Após aprovar a identidade: migrar a landing para React + Vite + Tailwind + shadcn/ui + MagicUI (+ 21st.dev) — GitHub Pages serve o build; backend segue local (adicionado em 2026-07-06, sessão: 2026-07-06-exploracao-shadcn-magicui.md)
- [ ] Esclarecer o que é o "getdesign.md" para incluir na exploração de bibliotecas de UI (adicionado em 2026-07-06, sessão: 2026-07-06-exploracao-shadcn-magicui.md)

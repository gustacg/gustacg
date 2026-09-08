<p align="center">
  <a href="https://www.gustacg.com"><img src="https://img.shields.io/badge/Portf%C3%B3lio-0B1C3A?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfólio"></a>
  <a href="https://www.linkedin.com/in/gustacg/"><img src="https://img.shields.io/badge/LinkedIn-0B1C3A?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://wa.me/559885474582"><img src="https://img.shields.io/badge/WhatsApp-0B1C3A?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"></a>
  <a href="mailto:gustavocalixto2005@gmail.com"><img src="https://img.shields.io/badge/E--mail-0B1C3A?style=for-the-badge&logo=gmail&logoColor=white" alt="E-mail"></a>
  &nbsp;&nbsp;<a href="README.en.md">English</a>
</p>

<a href="https://www.gustacg.com">
  <img src="assets/preview-hero.png" alt="gustacg.com: Construo o sistema que roda a operação de um negócio inteiro." width="100%">
</a>

<h3 align="center">26 projetos entregues &nbsp;·&nbsp; 17 softwares ativos &nbsp;·&nbsp; 6 anos construindo</h3>

<p align="center">Sócio e CTO da KortX. Passo o dia dentro de sistema que gente de verdade usa para trabalhar: ERP, SaaS, API e atendente de IA, em produção, com cliente pagando. O banco, a regra e a interface recebem a mesma atenção, e é isso que faz o sistema parecer inteiro.</p>

<br>

<p align="center"><code>PROJETOS</code></p>
<h2 align="center">O que eu construo</h2>

<a href="https://www.gustacg.com/#projetos">
  <img src="assets/motions.gif" alt="Alpha Motos, Safari Broker, Avance, Riff, Prospecto, Ferry Boat SLZ e Crias" width="100%">
</a>

<p align="center">Quase tudo é sistema de cliente, código fechado. Cada linha abre a página do projeto no site, com todos os módulos gravados em vídeo.</p>

| Projeto | O que é | Stack | Código |
|---|---|---|---|
| [Alpha Motos](https://www.gustacg.com/projetos/alpha-motos) | ERP de uma rede de concessionárias de motos que vende parcelado: do primeiro contato à última parcela, com oficina, peças, site, portal do cliente e hub de chat com IA sobre o mesmo banco. Receita recorrente do cliente cresceu 83% desde o ar. | React, TypeScript, PostgreSQL, Deno, n8n, Sentry | Fechado, cliente |
| [Safari Broker](https://www.gustacg.com/projetos/safari-broker) | SaaS multi-tenant para imobiliárias: site próprio com domínio, CRM com funis, carteira no mapa, negociações, contratos assinados digitalmente, financeiro e hub de atendimento. R$ 29,7 mi negociados na plataforma. | React, TypeScript, PostgreSQL, Deno, Tailwind, Vercel, Sentry | Fechado, cliente |
| [Avance](https://www.gustacg.com/projetos/avance) | ERP de escola de idiomas com uma atendente de IA no WhatsApp que vende, cuida do aluno e chama uma pessoa quando precisa. Quatorze módulos em produção. | React, TypeScript, PostgreSQL, WhatsApp Cloud API, n8n, Redis, Docker Swarm | Fechado, cliente |
| [Riff](https://www.gustacg.com/projetos/riff) | API e painel para consultar multas, IPVA e licenciamento, com monitoramento de frota agendado, consulta em lote e cobrança mensal automática. R$ 2 mi em débitos apontados ao longo de 6.091 consultas. | Python, FastAPI, Playwright, PostgreSQL, React, TypeScript, Docker, Sentry | Fechado · [testar](https://riff.kortx.com.br) |
| [Prospecto](https://www.gustacg.com/projetos/prospecto) | Plataforma white-label para gestão de agências: CRM com IA, contratos digitais, propostas e financeiro, com deploy inteiro em Docker. | React, TypeScript, Node.js, Docker, PostgreSQL | [Vídeo de instalação](https://www.youtube.com/watch?v=iWFZVsUNjL4) |
| [Ferry Boat SLZ](https://www.gustacg.com/projetos/ferry-boat-slz) | MVP mobile de balsa: reserva de passagem e de veículo, fila digital com posição e embarque conferido por QR Code. | React Native, Expo, TypeScript, Zustand, PostgreSQL | [Público](https://github.com/gustacg/ferry_boat_slz) |
| [Crias](https://www.gustacg.com/projetos/crias) | Aplicativo de celular (PWA) de hábitos em grupo com jeito de RPG: check-in diário, sequência, ouro, personagem na trilha e loja de prêmios. | React, TypeScript, Vite, Tailwind, PostgreSQL, Deno, PWA | Fechado, grupo real |

<br>

<p align="center"><code>CÓDIGO</code></p>
<h2 align="center">O que eu posso mostrar</h2>

<p align="center">O que segura esses sistemas vive no banco: idempotência na venda, lock de linha para saldo, isolamento por tenant, fila com <code>for update skip locked</code>, rate limit atômico, guarda anti-SSRF antes de chamar webhook de cliente. Nada disso é de cliente, então vai saindo em peça pequena e genérica, com teste contra Postgres de verdade.</p>

| Peça | O que prova | Teste |
|---|---|---|
| [pg-queue](https://github.com/gustacg/pg-queue) | Fila de trabalho dentro do Postgres: reivindicação atômica com `skip locked`, arrendamento, backoff exponencial, fila morta e reprocesso. Uma tabela, cinco funções, worker de cinquenta linhas. | Dois trabalhadores concorrentes, 40 de 40 sem duplicata, contra `postgres:16` em container |

<br>

<p align="center"><code>ATIVIDADE</code></p>
<h2 align="center">Um ano de commits, quase todos em repositório privado</h2>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="profile-3d-contrib/profile-night-green.svg">
  <img src="profile-3d-contrib/profile-green-animate.svg" alt="Calendário de contribuições em 3D, público e privado" width="100%">
</picture>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com/?user=gustacg&theme=dark&hide_border=true&locale=pt_BR">
    <img src="https://streak-stats.demolab.com/?user=gustacg&hide_border=true&locale=pt_BR" alt="Sequência de contribuições">
  </picture>
</p>

<br>

<p align="center"><code>STACK</code></p>
<h2 align="center">Só o que está em produção e eu defendo em entrevista</h2>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=ts,react,nextjs,tailwind,nodejs,deno,python,fastapi,postgres,supabase,redis,rabbitmq&theme=dark&perline=12">
    <img src="https://skillicons.dev/icons?i=ts,react,nextjs,tailwind,nodejs,deno,python,fastapi,postgres,supabase,redis,rabbitmq&theme=light&perline=12" alt="TypeScript, React, Next.js, Tailwind, Node.js, Deno, Python, FastAPI, PostgreSQL, Supabase, Redis, RabbitMQ">
  </picture>
  <br>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=docker,nginx,aws,vercel,git,githubactions,sentry,figma,photoshop,illustrator,ae,wordpress&theme=dark&perline=12">
    <img src="https://skillicons.dev/icons?i=docker,nginx,aws,vercel,git,githubactions,sentry,figma,photoshop,illustrator,ae,wordpress&theme=light&perline=12" alt="Docker, nginx, AWS, Vercel, Git, GitHub Actions, Sentry, Figma, Photoshop, Illustrator, After Effects, WordPress">
  </picture>
</p>

<p align="center">Mais n8n, Docker Swarm, Traefik, MinIO, Meta Tech Provider, Chatwoot, React Native, Expo, PWA, RAG e embeddings.</p>

<br>

<p align="center">
  <a href="https://www.gustacg.com"><img src="https://img.shields.io/badge/Ver%20o%20portf%C3%B3lio%20completo-2063F4?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Ver o portfólio completo"></a>
  &nbsp;
  <a href="https://wa.me/559885474582"><img src="https://img.shields.io/badge/Falar%20comigo-0B1C3A?style=for-the-badge&logo=whatsapp&logoColor=white" alt="Falar comigo"></a>
</p>

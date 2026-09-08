<p align="center">
  <a href="https://www.gustacg.com/en"><img src="https://img.shields.io/badge/Portfolio-0B1C3A?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfolio"></a>
  <a href="https://www.linkedin.com/in/gustacg/"><img src="https://img.shields.io/badge/LinkedIn-0B1C3A?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://wa.me/559885474582"><img src="https://img.shields.io/badge/WhatsApp-0B1C3A?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"></a>
  <a href="mailto:gustavocalixto2005@gmail.com"><img src="https://img.shields.io/badge/E--mail-0B1C3A?style=for-the-badge&logo=gmail&logoColor=white" alt="E-mail"></a>
  &nbsp;&nbsp;<a href="README.md">Português</a>
</p>

<a href="https://www.gustacg.com/en">
  <img src="assets/preview-hero.png" alt="gustacg.com: I build the system a whole business runs on." width="100%">
</a>

<h3 align="center">26 projects delivered &nbsp;·&nbsp; 17 live software systems &nbsp;·&nbsp; 6 years building</h3>

<p align="center">Co-founder and CTO at KortX. I spend my days inside systems real people use to work: ERPs, SaaS, APIs and AI assistants, in production, with paying clients. The database, the rules and the interface get the same attention, and that is what makes a system feel whole.</p>

<br>

<p align="center"><code>WORK</code></p>
<h2 align="center">What I build</h2>

<a href="https://www.gustacg.com/en#projetos">
  <img src="assets/motions.gif" alt="Alpha Motos, Safari Broker, Avance, Riff, Prospecto, Ferry Boat SLZ and Crias" width="100%">
</a>

<p align="center">Almost all of it is client software, closed source. Every row opens the project page on the site, with all modules recorded on video.</p>

| Project | What it is | Stack | Code |
|---|---|---|---|
| [Alpha Motos](https://www.gustacg.com/en/projects/alpha-motos) | A live ERP for a motorcycle dealership network that sells in instalments: from first contact to last instalment, with workshop, parts, public site, customer portal and an AI chat hub on the same database. The client's recurring revenue grew 83% since go-live. | React, TypeScript, PostgreSQL, Deno, n8n, Sentry | Closed, client |
| [Safari Broker](https://www.gustacg.com/en/projects/safari-broker) | Multi-tenant SaaS for estate agencies: their own site on their own domain, a CRM with pipelines, a property portfolio on the map, deals, digitally signed contracts, finance and a service hub. R$ 29.7M negotiated on the platform. | React, TypeScript, PostgreSQL, Deno, Tailwind, Vercel, Sentry | Closed, client |
| [Avance](https://www.gustacg.com/en/projects/avance) | Language school ERP with an AI assistant on WhatsApp that sells, looks after the student and calls in a person when needed. Fourteen modules in production. | React, TypeScript, PostgreSQL, WhatsApp Cloud API, n8n, Redis, Docker Swarm | Closed, client |
| [Riff](https://www.gustacg.com/en/projects/riff) | An API and a panel for checking vehicle fines, road tax and licensing, with scheduled fleet monitoring, batch lookups and automatic monthly billing. R$ 2M in debts surfaced across 6,091 lookups. | Python, FastAPI, Playwright, PostgreSQL, React, TypeScript, Docker, Sentry | Closed · [try it](https://riff.kortx.com.br) |
| [Prospecto](https://www.gustacg.com/en/projects/prospecto) | White-label platform for agency management: AI-powered CRM, digital contracts, proposals and finance, fully deployed in Docker. | React, TypeScript, Node.js, Docker, PostgreSQL | [Setup video](https://www.youtube.com/watch?v=iWFZVsUNjL4) |
| [Ferry Boat SLZ](https://www.gustacg.com/en/projects/ferry-boat-slz) | Mobile MVP for a ferry: ticket and vehicle booking, a digital queue with your position, and boarding checked by QR code. | React Native, Expo, TypeScript, Zustand, PostgreSQL | [Public](https://github.com/gustacg/ferry_boat_slz) |
| [Crias](https://www.gustacg.com/en/projects/crias) | Mobile app (PWA) for group habits with an RPG feel: daily check-in, streaks, gold, a character moving along a trail and a rewards shop. | React, TypeScript, Vite, Tailwind, PostgreSQL, Deno, PWA | Closed, real group |

<br>

<p align="center"><code>CODE</code></p>
<h2 align="center">What I can show</h2>

<p align="center">What holds those systems together lives in the database: idempotency on the sale, row locks for stock balance, tenant isolation, a queue on <code>for update skip locked</code>, atomic rate limiting, an SSRF guard before calling a client's webhook. None of it belongs to a client, so it comes out as small generic pieces, each tested against a real Postgres.</p>

| Piece | What it proves | Test |
|---|---|---|
| [pg-queue](https://github.com/gustacg/pg-queue) | A job queue inside Postgres: atomic claim with `skip locked`, leases, exponential backoff, dead letter and reprocess. One table, five functions, a fifty-line worker. | Two concurrent workers, 40 of 40 with no duplicate, against `postgres:16` in a container |

<br>

<p align="center"><code>ACTIVITY</code></p>
<h2 align="center">A year of commits, almost all in private repositories</h2>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="profile-3d-contrib/profile-night-green.svg">
  <img src="profile-3d-contrib/profile-green-animate.svg" alt="3D contribution calendar, public and private" width="100%">
</picture>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com/?user=gustacg&theme=dark&hide_border=true">
    <img src="https://streak-stats.demolab.com/?user=gustacg&hide_border=true" alt="Contribution streak">
  </picture>
</p>

<br>

<p align="center"><code>STACK</code></p>
<h2 align="center">Only what shipped and I can defend in an interview</h2>

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

<p align="center">Plus n8n, Docker Swarm, Traefik, MinIO, Meta Tech Provider, Chatwoot, React Native, Expo, PWA, RAG and embeddings.</p>

<br>

<p align="center">
  <a href="https://www.gustacg.com/en"><img src="https://img.shields.io/badge/See%20the%20full%20portfolio-2063F4?style=for-the-badge&logo=googlechrome&logoColor=white" alt="See the full portfolio"></a>
  &nbsp;
  <a href="https://wa.me/559885474582"><img src="https://img.shields.io/badge/Get%20in%20touch-0B1C3A?style=for-the-badge&logo=whatsapp&logoColor=white" alt="Get in touch"></a>
</p>

---
name: cost-estimator
description: Researches the exact, current cost to build and run a website or app — hosting (Vercel, Netlify, Cloudflare), database (Neon, Supabase), domain, email, payments fees (Stripe, Mercado Pago, Pix), auth, storage — compares free and paid options and recommends the best value. Use when the user asks "quanto custa", "qual o valor", "qual é mais barato", "custo-benefício", "precisa pagar?", or before choosing where to host a project.
---

# Cost estimator

Prices change. **Never answer from memory** — fetch each provider's official pricing page
today and cite it. If a page can't be fetched, say so and mark that number as "não confirmado".

## 1. Understand the project (ask only what you can't infer)
- Type: landing page, site with booking/agenda, online store, game, app with login.
- Commercial or personal? (Matters: e.g. Vercel **Hobby is non-commercial only** —
  a client's business site needs Pro or another host that allows commercial use on free tier.)
- Expected traffic (visits/month), storage (images/videos), need for login, database, payments, email, custom domain.

## 2. Price every layer (official pages)
| Layer | Check at least |
|---|---|
| Hosting | Vercel, Netlify, Cloudflare Pages/Workers |
| Database | Neon, Supabase (free tier limits: storage, compute hours, pausing) |
| Domain (.com.br / .com) | Registro.br, Cloudflare Registrar, Porkbun — first year **and renewal** |
| Email transactional | Resend, Brevo |
| Payments | Stripe, Mercado Pago, Pix — % fee + fixed fee per transaction, payout time |
| Auth / storage / other | Only if the project needs it |

For each: free tier limits, first paid tier, what triggers the jump, overage cost.

## 3. Calculate
- Convert USD → BRL with today's rate (fetch it; state the rate and date). Mention IOF on
  international card charges (check the current percentage).
- Show **setup cost**, **monthly cost** and **yearly cost** for: (a) cheapest viable,
  (b) recommended, (c) growth scenario.
- Payments: show the fee on an example ticket (e.g. R$ 80 haircut → fee R$ X → she receives R$ Y).

## 4. Answer format (Portuguese)
1. One-line answer: "Dá para começar com R$ X/mês" (or "de graça, com estes limites…").
2. Table per scenario with sources (link per row).
3. Recommendation and why, including the gotchas (commercial-use rules, sleeping free
   databases, renewal price higher than first year).
4. Date of the research.

Optional: if the user uses Notion, add the table as a page/database there (Notion MCP).

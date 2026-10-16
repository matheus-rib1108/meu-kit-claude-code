---
name: site-fortress
description: Full security audit and hardening of the user's OWN website, web app or browser game, part by part, like a professional pentester — finds every vulnerability and bug, fixes it, and proves the fix. Use before launching any site, when the site handles logins, personal data or payments (cards, Pix), when the user asks "deixa seguro", "verifica a segurança", "procura erros", "testa como hacker", or after big changes. Defensive only — never against sites the user doesn't own.
---

# Site Fortress

Goal: leave no known hole and no known bug. Be honest with the user: nothing is
"100% secure" — the goal is that every known attack class is checked, closed and proven.

Only test systems the user owns or has written permission to test. Active tests
(phase 9) run against a **preview/staging deploy or localhost**, never against someone else's site.

Work through every phase in order. Keep `SECURITY-AUDIT.md` at the repo root: one row per
finding — `ID | fase | severidade (crítica/alta/média/baixa) | arquivo:linha | o que é | como corrigiu | prova`.
Use parallel subagents for independent phases (e.g. `security-auditor` on phases 3–6,
`code-reviewer` on 7, `qa-expert` + `webapp-testing` on 10).

## Tool map (all installed in this repo — use them, in parallel where independent)
| Phase | Skills / plugins |
|---|---|
| 0 map | `ghost-repo-context`, `audit-context-building` |
| 1 secrets | `secrets-gitleaks` |
| 2 deps | `sca-trivy`, `supply-chain-risk-auditor` |
| 3–7 code | `ghost-scan-code` (depth=full), `cybersecurity`, `owasp-security`, `semgrep`, `sharp-edges`, plugin `claude-security`, agent `security-auditor` |
| 6 payments | plugins `mercadopago` / `stripe` (their review skills) |
| 9 attack | `dast-zap`, `dast-nuclei`, `webapp-testing`, plugin `chrome-devtools-mcp` |
| 10 legal | `legal-compliance` (privacy policy, terms, cookies, LGPD) |
| 11 verify | `ghost-validate`, `fp-check`, `variant-analysis`, `ghost-report` |
Plugin `security-guidance` is always on: it warns while code is being written.

## Phase 0 — Map the attack surface
- Read routes and config: list every page, API route, server action,
  webhook, form, file upload, admin area, cron job, third-party script.
- Write who may call each one (anonymous / logged-in / owner / admin). This table drives phases 3–4.

## Phase 1 — Secrets
- `gitleaks detect --source . --log-opts="--all"` (whole git history) or `trufflehog git file://.`.
- No key in front-end code: in Next.js, anything `NEXT_PUBLIC_*` is public. Server-only keys
  stay in Vercel/hosting env vars. `.env*` in `.gitignore`.
- Any leaked secret: rotate it at the provider (deleting the commit is not enough).

## Phase 2 — Dependencies and supply chain
- `npm audit --omit=dev` / `pnpm audit`, `osv-scanner -r .`; skill `supply-chain-risk-auditor`.
- Lockfile committed, exact versions, no abandoned or typo-squatted packages, no `postinstall` surprises.

## Phase 3 — Authentication and sessions
- Use a proven provider (Neon Auth, Auth.js, Clerk, Supabase Auth). Never hand-roll password crypto.
- Passwords: argon2id/bcrypt; rate-limit login, signup, password reset; generic error messages.
- Cookies: `HttpOnly; Secure; SameSite=Lax` (or `Strict`); rotate session on login; real logout.
- Reset tokens: single-use, short-lived, random. Optional 2FA for admin.

## Phase 4 — Authorization (the #1 real-world bug)
- Every API route / server action checks **on the server** who the user is and whether
  they own the record. Hiding a button is not security.
- Test IDOR: user A changes an id in the URL/body to user B's record → must get 403/404.
- Database: least-privilege role for the app; Row-Level Security where available.

## Phase 5 — Input, injection and XSS
- Validate every input on the server with a schema (zod/valibot). Reject unknown fields.
- SQL only through parameterized queries / ORM; never string-concatenate.
- No `dangerouslySetInnerHTML`/`innerHTML`/`eval` with user data; sanitize rich text (DOMPurify).
- File uploads: check type by content, size limit, random names, store outside the app, never execute.
- SSRF: server never fetches arbitrary user-given URLs without an allow-list.
- Skills `semgrep` (run `semgrep --config auto`) and `sharp-edges` for dangerous APIs.

## Phase 6 — Payments (cards, Pix) — critical
- **The site never sees or stores card numbers.** Use hosted checkout: Stripe Checkout /
  Payment Links, Mercado Pago Checkout Pro, or the provider's hosted fields. That keeps the
  site out of most PCI-DSS scope (SAQ A). Never log, save or send card data to your server.
- Price and total are computed **on the server** from your own database — never trust an
  amount sent by the browser.
- Order is marked paid only by a **webhook whose signature is verified** (Stripe
  `constructEvent`, Mercado Pago `x-signature`), handled idempotently (same event twice = one payment).
- Secret keys server-only; test mode vs live mode keys separated; restricted keys where possible.
- Card owner (e.g. the hairdresser) configures payouts in the provider dashboard herself —
  her bank/card details never go into the code or chat.

## Phase 7 — Business logic and bugs
- Can someone book the same slot twice, use a coupon infinitely, get negative quantities,
  skip a step, replay a request? Race conditions on anything with money or limits.
- Error handling: no stack traces to users; errors logged server-side.
- Skill `systematic-debugging` for every bug found; `differential-review` on recent changes.

## Phase 8 — Headers, transport and configuration
- HTTPS only + HSTS; `Content-Security-Policy` (no `unsafe-inline` scripts if avoidable),
  `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`,
  `Permissions-Policy`, `frame-ancestors 'none'` (clickjacking).
- CORS: explicit origins, never `*` with credentials. CSRF protection on cookie-auth forms.
- Rate limiting on all public APIs and forms (e.g. Vercel Firewall / Upstash ratelimit); bot
  protection on contact/booking forms (Turnstile/hCaptcha).
- Debug mode off, source maps not public, admin routes not guessable *and* protected,
  directory listing off, `robots.txt` doesn't reveal secrets.

## Phase 9 — Attack it for real (dynamic test, own preview deploy only)
- OWASP ZAP baseline: `docker run -t ghcr.io/zaproxy/zaproxy:stable zap-baseline.py -t <preview-url>`
  (and `zap-full-scan.py` on staging).
- Playwright (`webapp-testing`): try XSS payloads in every field, IDOR swaps, expired sessions,
  direct calls to protected APIs without a cookie, uploading a `.html`/`.svg` with script.
- Check headers: `curl -sI <url>`; TLS grade via ssllabs.com; securityheaders.com.
- Optional deep test: **Shannon** (KeygraphHQ/shannon, AI pentester) against staging — needs
  Docker and an API key; the user runs it.

## Phase 10 — Privacy, legal and resilience (LGPD)
- Run the `legal-compliance` skill: privacy policy, terms, cookie consent that really blocks
  scripts until accepted, consumer info, data-deletion channel.
- Collect the minimum personal data; privacy policy page; way to delete one's data.
- Database backups on (Neon point-in-time restore / branches); tested restore.
- Error monitoring (Sentry) and uptime alert. Dependency updates (Dependabot/Renovate).
- Games: validate scores/progress on the server if there is a leaderboard or prize — the
  client can always be modified.

## Phase 11 — Fix, prove, repeat
For each finding: fix at the narrowest place (`surgical-patch`), add a test that would have
caught it, re-run that phase's check, record the proof in `SECURITY-AUDIT.md`.
Skill `fp-check` to discard false positives with evidence. Then run phases 1, 2, 5 and 9
again in full. Done only when there are **zero open critical/high findings** and every
fix has proof (`verification-before-completion`).

## Final report to the user (Portuguese, plain words)
What was checked, what was found, what was fixed, what still needs them (e.g. turn on 2FA
in the hosting account, the business owner setting up payouts), and a short checklist to
repeat before each future launch.

---
name: legal-compliance
description: Makes a website legally ready to publish in Brazil (LGPD, Marco Civil, Código de Defesa do Consumidor) and for Google (Search, Ads, Analytics, AdSense, Sign in with Google, Play) — writes and adds the privacy policy, terms of use, cookie banner with real consent, contact/business info, data-deletion request, and checks forms and third-party scripts. Use for every site that collects any data (forms, login, booking, analytics, cookies, payments) or before publishing, and when the user mentions "política de privacidade", "termos de uso", "cookies", "LGPD", "não quero ser processado", "Google pediu política".
---

# Legal compliance

Not a lawyer: generate solid documents tailored to what the site really does, and tell the
user that a business with sensitive data or high volume should have a lawyer review them.
Never copy another company's policy text.

## 1. Inventory what the site actually does (from the code, not assumptions)
List: every form field, login, booking, payment provider, cookies set, analytics/ads/pixels
(Google Analytics, Tag Manager, Meta Pixel, TikTok Pixel), embeds (YouTube, Maps, Instagram),
email provider, hosting/database location (often outside Brazil → international transfer),
who the controller is (name, CPF/CNPJ, city, contact email), retention period of each data type.

## 2. Pages to create (Portuguese, plain language, linked in the footer of every page)
- `/privacidade` — **Política de Privacidade (LGPD, Lei 13.709/2018)**: controller and contact
  (and DPO/encarregado contact or the person responsible), which data and why (one purpose
  per item), legal basis for each (consent, contract, legitimate interest, legal obligation),
  who it's shared with (each processor by name: hosting, database, payments, email,
  analytics), international transfer, retention, security measures, rights of the data
  subject (art. 18: access, correction, deletion, portability, revoke consent, info on sharing)
  and how to exercise them, cookies section, children's data (if any), date of last update.
- `/termos` — **Termos de Uso**: what the service is, rules of use, bookings/cancellation/
  no-show policy (for services), prices and payment, liability limits that are lawful under
  the CDC (don't write abusive clauses — they're void), intellectual property, forum (comarca).
- **Consumer info (Decreto 7.962/2013 for anyone selling online)**: full name/razão social,
  CPF/CNPJ, physical address, email/phone visible on the site; clear prices; right of
  withdrawal (7 days for online purchases, art. 49 CDC) where it applies.
- Data request channel: an email or form "Solicitar meus dados / Excluir meus dados".

## 3. Cookie consent that actually works
- Banner with **Aceitar / Recusar / Preferências**, equal prominence; nothing pre-ticked.
- Non-essential scripts (analytics, ads, pixels) **do not load until accepted**; store the
  choice; a footer link reopens preferences.
- Google tags: implement **Google Consent Mode v2** (`ad_storage`, `analytics_storage`,
  `ad_user_data`, `ad_personalization` default `denied`, updated on consent). Required by
  Google for ads/measurement of EU/EEA users; good practice everywhere.
- Prefer privacy-friendly analytics that need no banner when possible (e.g. Vercel Web
  Analytics, Plausible) — say this to the user.

## 4. Forms and data minimization
Only ask what is needed; mark required fields; consent checkbox (unticked) only where
consent is the legal basis, with link to the policy; no CPF unless legally needed; never
send personal data in URLs or to analytics; HTTPS everywhere (see `site-fortress`).

## 5. Google-specific checks
- Search/Business Profile: privacy policy and real contact info help trust; no deceptive content.
- Ads/AdSense/Analytics: policy must disclose Google cookies and use of data by Google
  (link to "How Google uses data when you use our partners' sites"); Consent Mode v2.
- Sign in with Google / OAuth verification / Play Store: privacy policy URL on the same domain,
  homepage explaining the app, and the policy must describe Google user data use.

## 6. Other legal risks to check
Images, fonts, music and videos must be licensed (use own photos, Unsplash/Pexels, Google
Fonts); no fake reviews; promotions/sweepstakes have rules in Brazil; client's brand/name
approved in writing; accessibility (basic WCAG) — Lei Brasileira de Inclusão.

## 7. Deliver
Pages live in the site, linked in the footer, banner working (test: refuse → no analytics
request in the network tab, via `webapp-testing`), and a short note to the user listing
what to fill in (CNPJ, address) and what a lawyer should review.

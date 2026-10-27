// Varre HTML/CSS/JSX/TSX atrás de sinais de "cara de IA". Uso: node detectar.mjs <pasta-ou-arquivo> [...]
import { readFileSync, readdirSync, statSync } from 'node:fs';
import { join, extname } from 'node:path';

export const SINAIS = [
  ['gradiente roxo/índigo', /(from|via|to)-(purple|violet|indigo|fuchsia)-\d{3}|linear-gradient\([^)]*(#(7c3aed|8b5cf6|6366f1|a855f7|9333ea|4f46e5)|purple|violet)/i],
  ['fonte padrão de IA (Inter/Geist/Space Grotesk) como única fonte', /font-family:\s*['"]?(Inter|Geist|Space Grotesk)['"]?\s*[,;]|family=(Inter|Space\+Grotesk)[:&]/i],
  ['emoji usado como ícone', /<(h[1-6]|li|span|div|p)[^>]*>\s*[\u{1F300}-\u{1FAFF}✨⚡✅]/u],
  ['texto de marketing vazio', /\b(unlock the power|supercharge|seamless(ly)?|elevate your|revolutioniz|game[- ]changer|next[- ]level|leve seu .* ao próximo nível|transforme seu negócio|solução completa|potencialize)\b/i],
  ['lorem ipsum / texto de exemplo', /lorem ipsum|Your Company|Acme Inc|John Doe/i],
  ['sombra e borda padrão de template', /\b(shadow-(lg|xl|2xl))\b[^"']*\brounded-(2xl|3xl)\b|\brounded-(2xl|3xl)\b[^"']*\bshadow-(lg|xl|2xl)\b/],
  ['orbe/blur de fundo decorativo', /blur-3xl|filter:\s*blur\((6\d|[7-9]\d|\d{3})px\)/i],
  ['grade de pontinhos de fundo', /radial-gradient\([^)]*(1px|1\.5px)[^)]*transparent/i],
  ['ícone de brilho/estrela genérico', /\b(Sparkles|SparklesIcon|lucide-sparkles)\b/],
  ['travessão longo em texto (—)', /[a-zà-ú] — [a-zà-ú]/i],
  ['depoimento/número inventado', /(\+?\d{1,3}[.,]?\d{3}\+? (clientes|usuários|users|customers) satisfeitos|5\.0 ★|★★★★★)/i],
  ['branco e preto puros', /(background(-color)?:\s*#fff(fff)?\b|color:\s*#000(000)?\b)/i],
];

const EXT = new Set(['.html', '.htm', '.css', '.jsx', '.tsx', '.js', '.ts', '.vue', '.svelte', '.astro', '.md']);
const PULAR = new Set(['node_modules', '.next', 'dist', 'build', '.git', '.vercel']);

function* arquivos(p) {
  const s = statSync(p);
  if (s.isFile()) { if (EXT.has(extname(p))) yield p; return; }
  for (const n of readdirSync(p)) if (!PULAR.has(n)) yield* arquivos(join(p, n));
}

export function varrer(texto) {
  const achados = [];
  texto.split(/\r?\n/).forEach((linha, i) => {
    if (/^\s*(\/\/|\/\*|\*)/.test(linha)) return; // comentário de código não aparece para o visitante
    for (const [nome, re] of SINAIS) if (re.test(linha)) achados.push({ nome, linha: i + 1, trecho: linha.trim().slice(0, 110) });
  });
  return achados;
}

if (process.argv[2] === '--teste') {
  const t = varrer('<h2>✨ Recursos</h2>\n<div class="bg-gradient-to-r from-purple-500 to-indigo-600">Unlock the power</div>\n<p>Texto normal</p>');
  console.assert(t.some(a => a.nome.startsWith('emoji')), 'emoji');
  console.assert(t.some(a => a.nome.startsWith('gradiente')), 'gradiente');
  console.assert(t.some(a => a.nome.startsWith('texto de marketing')), 'copy');
  console.assert(!t.some(a => a.linha === 3), 'linha limpa');
  console.log('teste ok');
} else {
  const alvos = process.argv.slice(2);
  if (!alvos.length) { console.error('Uso: node detectar.mjs <pasta-ou-arquivo>'); process.exit(1); }
  let total = 0;
  for (const a of alvos) for (const f of arquivos(a)) {
    for (const x of varrer(readFileSync(f, 'utf8'))) { total++; console.log(`${f}:${x.linha}  [${x.nome}]  ${x.trecho}`); }
  }
  console.log(total ? `\n${total} sinais. Corrija com a tabela da skill anti-cara-de-ia.` : 'Nenhum sinal automático. Faça a revisão visual mesmo assim.');
}

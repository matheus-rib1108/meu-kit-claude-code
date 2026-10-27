// Contraste WCAG 2.2 entre duas cores. Uso: node contraste.mjs #texto #fundo [#texto2 #fundo2 ...]
const lum = h => {
  const c = [1, 3, 5].map(i => parseInt(h.slice(i, i + 2), 16) / 255)
    .map(v => (v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4));
  return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
};
export const contraste = (a, b) => {
  const [x, y] = [lum(a), lum(b)];
  return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05);
};
const nota = r => (r >= 7 ? 'AAA' : r >= 4.5 ? 'AA' : r >= 3 ? 'só texto grande/borda (3:1)' : 'REPROVA');

if (process.argv[2] === '--teste') {
  console.assert(Math.abs(contraste('#000000', '#FFFFFF') - 21) < 0.01, 'preto/branco = 21');
  console.assert(Math.abs(contraste('#767676', '#FFFFFF') - 4.54) < 0.01, 'cinza 767676 = 4.54');
  console.log('teste ok');
} else {
  const a = process.argv.slice(2);
  if (a.length < 2 || a.length % 2 || !a.every(h => /^#[0-9a-fA-F]{6}$/.test(h))) {
    console.error('Uso: node contraste.mjs #RRGGBB #RRGGBB [mais pares]');
    process.exit(1);
  }
  for (let i = 0; i < a.length; i += 2) {
    const r = contraste(a[i], a[i + 1]);
    console.log(`${a[i]} sobre ${a[i + 1]}: ${r.toFixed(2)}:1  ${nota(r)}`);
  }
}

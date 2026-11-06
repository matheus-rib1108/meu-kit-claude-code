#!/usr/bin/env node
// Lista skills e agentes instalados, lendo os arquivos na hora (nunca fica desatualizado).
// Uso: node listar.mjs [--tipo skill|agente] [--busca "palavras"] [--teste]
import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { join } from 'node:path';
import { homedir } from 'node:os';
import assert from 'node:assert';

const CLAUDE = join(homedir(), '.claude');

export function lerCabecalho(texto) {
  const m = texto.replace(/\r\n/g, '\n').match(/^---\n([\s\S]*?)\n---/);
  if (!m) return {};
  const linhas = m[1].split('\n');
  const campo = (nome) => {
    const i = linhas.findIndex((l) => l.startsWith(nome + ':'));
    if (i < 0) return '';
    let v = linhas[i].slice(nome.length + 1).trim();
    if (/^[>|][+-]?$/.test(v)) {
      const resto = [];
      for (let j = i + 1; j < linhas.length && /^\s+/.test(linhas[j]); j++) resto.push(linhas[j].trim());
      v = resto.join(' ');
    }
    return v.replace(/^["']|["']$/g, '');
  };
  return { name: campo('name'), description: campo('description') };
}

function ler(caminho) {
  try { return lerCabecalho(readFileSync(caminho, 'utf8')); } catch { return {}; }
}

function pastas(dir) {
  if (!existsSync(dir)) return [];
  return readdirSync(dir, { withFileTypes: true });
}

function coletar(base, origem, prefixo = '') {
  const itens = [];
  for (const d of pastas(join(base, 'skills'))) {
    if (!d.isDirectory()) continue;
    const c = ler(join(base, 'skills', d.name, 'SKILL.md'));
    if (c.description !== undefined) itens.push({ tipo: 'skill', nome: prefixo + (c.name || d.name), origem, descricao: c.description });
  }
  for (const d of pastas(join(base, 'agents'))) {
    if (!d.name.endsWith('.md')) continue;
    const c = ler(join(base, 'agents', d.name));
    if (c.description !== undefined) itens.push({ tipo: 'agente', nome: prefixo + (c.name || d.name.slice(0, -3)), origem, descricao: c.description });
  }
  return itens;
}

export function tudo() {
  const itens = coletar(CLAUDE, 'pessoal');
  const arq = join(CLAUDE, 'plugins', 'installed_plugins.json');
  if (existsSync(arq)) {
    const { plugins = {} } = JSON.parse(readFileSync(arq, 'utf8'));
    for (const [id, instalacoes] of Object.entries(plugins)) {
      const plugin = id.split('@')[0];
      const atual = instalacoes[instalacoes.length - 1];
      if (atual?.installPath) itens.push(...coletar(atual.installPath, 'plugin ' + plugin, plugin + ':'));
    }
  }
  return itens;
}

export function buscar(itens, busca) {
  const palavras = busca.toLowerCase().split(/\s+/).filter(Boolean);
  return itens
    .map((i) => {
      const nome = i.nome.toLowerCase();
      const desc = i.descricao.toLowerCase();
      return { ...i, pontos: palavras.reduce((p, w) => p + (nome.includes(w) ? 3 : 0) + (desc.includes(w) ? 1 : 0), 0) };
    })
    .filter((i) => i.pontos > 0)
    .sort((a, b) => b.pontos - a.pontos);
}

function teste() {
  assert.deepEqual(lerCabecalho('---\nname: a\ndescription: "b c"\n---\nx'), { name: 'a', description: 'b c' });
  assert.equal(lerCabecalho('---\r\nname: a\r\ndescription: >\r\n  um\r\n  dois\r\n---\r\n').description, 'um dois');
  assert.deepEqual(lerCabecalho('sem cabecalho'), {});
  const lista = [{ nome: 'video-maker', descricao: 'faz reels' }, { nome: 'outro', descricao: 'video curto' }, { nome: 'nada', descricao: 'x' }];
  assert.deepEqual(buscar(lista, 'video').map((i) => i.nome), ['video-maker', 'outro']);
  console.log('ok');
}

const args = process.argv.slice(2);
const valor = (flag) => (args.includes(flag) ? args[args.indexOf(flag) + 1] ?? '' : null);

if (args.includes('--teste')) {
  teste();
} else {
  let itens = tudo();
  const tipo = valor('--tipo');
  const busca = valor('--busca');
  if (tipo) itens = itens.filter((i) => i.tipo === tipo);
  if (busca) itens = buscar(itens, busca);
  else itens.sort((a, b) => a.tipo.localeCompare(b.tipo) || a.nome.localeCompare(b.nome));
  const n = (t) => itens.filter((i) => i.tipo === t).length;
  console.log(`${n('skill')} skills, ${n('agente')} agentes`);
  for (const i of itens) console.log(`- [${i.tipo}] ${i.nome} (${i.origem}): ${i.descricao.slice(0, 160)}`);
}

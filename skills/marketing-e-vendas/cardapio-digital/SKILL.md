---
name: cardapio-digital
description: Monta um cardápio digital para pizzaria, lanchonete, açaí ou restaurante brasileiro — página única leve, com categorias, fotos, preços, adicionais, botão de pedido pelo WhatsApp com a mensagem já preenchida, horário e QR code para a mesa — pronta para publicar de graça. Use quando o usuário falar em cardápio digital, cardápio online, QR code de mesa, pedido pelo WhatsApp, sair do iFood, ou fizer um site para um restaurante.
---

# Cardápio digital

## 1. Dados do cliente (pergunte o que faltar)
Nome, logo, cores, WhatsApp comercial, endereço, horário, taxa e área de entrega, formas de pagamento (Pix, cartão na entrega) e os itens: categoria, nome, descrição curta, preço, tamanhos e adicionais. Se o cliente mandar foto do cardápio impresso, transcreva e **mostre a lista para ele conferir os preços** antes de montar a página.

## 2. Página
- Um arquivo HTML + CSS + JS, sem framework, abrindo rápido no 4G (imagens em WebP, até ~150 KB cada, com `loading="lazy"`).
- Topo: logo, aberto/fechado (calculado pelo horário), endereço e botão do WhatsApp.
- Menu de categorias fixo no topo, rolando até a seção.
- Cada item: foto opcional, nome, descrição, preço em R$ (`toLocaleString('pt-BR', {style:'currency', currency:'BRL'})`) e botão "adicionar".
- Carrinho simples: tamanho, adicionais, observação, nome, endereço ou retirada e pagamento → gera o texto do pedido e abre `https://wa.me/55DDDNUMERO?text=` com `encodeURIComponent`.
- Itens editáveis num único `cardapio.json`, para o dono mudar preço sem mexer no código.

## 3. Publicar e QR code
- Hospedagem grátis: GitHub Pages, Netlify ou Vercel. Domínio próprio é opcional (.com.br no Registro.br).
- Gere o QR code apontando para a URL final (biblioteca `qrcode` em Python) em PNG para impressão (mínimo de 3 × 3 cm na mesa).
- Cadastre o link no Google Meu Negócio e na bio do Instagram.

## Regras
- Preço e item conferidos pelo dono antes de publicar. Data da última atualização no rodapé.
- O site não processa pagamento com cartão: o pagamento é na entrega ou por Pix com a chave do estabelecimento.
- Acessível: contraste bom, botões de no mínimo 44 px e textos alternativos nas fotos.
- Antes de publicar, passe pela checagem de segurança e privacidade (política de privacidade, se coletar dados).

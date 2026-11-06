#!/usr/bin/env python3
"""Gera as páginas estáticas do site Drone Vision.

Uso (na raiz do repositório):  python3 tools/build.py
Edite os textos neste arquivo e rode de novo; ele recria os index.html,
o 404.html e o sitemap.xml. O GitHub Pages publica os arquivos gerados.
"""
import html, json, os, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://dronevision.com.br"
WA = "5521966810304"
WA_FMT = "(21) 96681-0304"
EMAIL = "jorge@dronevision.com.br"
INSTA = "dronevision456"
TODAY = datetime.date.today().isoformat()
OG = "/assets/img/og-dronevision.jpg"

e = lambda s: html.escape(s, quote=True)
def wa(msg="Olá! Quero um orçamento."):
    from urllib.parse import quote
    return f"https://wa.me/{WA}?text={quote(msg)}"

ICON = {
 "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3Z"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
 "ig": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>',
 "hotel": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 42V18l18-10 18 10v24"/><path d="M4 42h40M14 42V30h8v12M28 26h8M28 33h8M14 22h8"/><path d="M33 12c2-3 6-3 8 0" opacity=".6"/></svg>',
 "imoveis": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 22 24 8l18 14"/><path d="M10 19v23h28V19"/><path d="M20 42V30h8v12"/><circle cx="24" cy="22" r="3"/></svg>',
 "obras": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M10 42V8h4v34M4 42h40M14 10h28l-6 6M14 10l8 8M30 16v8"/><rect x="26" y="24" width="8" height="6"/><path d="M22 42V32h18v10"/></svg>',
 "inspecoes": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 34 14 18h26l-10 16Z"/><path d="M9 26h26M19 18l-6 16M29 18l-6 16"/><circle cx="36" cy="10" r="5"/><path d="m40 14 4 4"/></svg>',
 "agro": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 40c8-4 32-4 40 0M4 33c8-4 32-4 40 0"/><path d="M24 26V8M24 14c-5 0-8-3-8-6 5 0 8 3 8 6Zm0 4c5 0 8-3 8-6-5 0-8 3-8 6Z"/></svg>',
 "reg": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M24 4 8 10v12c0 10 7 18 16 22 9-4 16-12 16-22V10Z"/><path d="m17 24 5 5 10-10"/></svg>',
}

SERVICES = [
  {
    "slug": "hotelaria-e-pousadas", "icon": "hotel", "cat": "Hotelaria & Pousadas",
    "name": "Hotelaria e pousadas",
    "card": "Fachada, piscina, paisagem e estrutura de lazer vistas de cima, para site, OTAs e campanhas.",
    "title": "Filmagem aérea com drone para hotéis e pousadas no RJ",
    "desc": "Fotos e vídeos aéreos em 4K HDR de hotéis, pousadas e resorts no Rio de Janeiro: fachada, piscina, paisagem e entorno para site, Booking, Airbnb e campanhas.",
    "h1": "Imagens aéreas que vendem a estadia antes da reserva",
    "intro": "O hóspede escolhe pelo que vê. Do alto, o seu hotel ou pousada mostra o que a foto de solo não alcança: a piscina em relação ao jardim, a distância até a praia ou a serra, o tamanho real da área de lazer.",
    "uses": [("Site e OTAs", "Fotos de abertura para o site, Booking, Airbnb e Google, com enquadramento pensado para cada formato."),
             ("Campanhas e redes", "Vídeos curtos em 9:16 para Reels e Stories e versões horizontais para anúncios e YouTube."),
             ("Eventos e casamentos", "Registro aéreo de espaços para eventos, mostrando capacidade, acessos e cenário."),
             ("Entorno e localização", "Contexto de chegada: estrada, praia, mata ou centro, para o hóspede entender onde vai ficar.")],
    "faq": [("Qual o melhor horário para filmar uma pousada?", "Depende do que se quer destacar. O fim de tarde costuma valorizar piscina e paisagem com luz quente; a manhã favorece áreas verdes. Definimos o horário no planejamento, junto com você."),
            ("Vocês entregam material para redes sociais?", "Sim. Combinamos no orçamento os formatos de entrega, como fotos editadas, vídeo horizontal e cortes verticais para Reels e Stories.")],
  },
  {
    "slug": "imoveis", "icon": "imoveis", "cat": "Imóveis",
    "name": "Imóveis",
    "card": "Terrenos, condomínios e casas com contexto de vizinhança, acesso e vista que a foto de solo não entrega.",
    "title": "Fotos e vídeos aéreos de imóveis com drone no Rio de Janeiro",
    "desc": "Imagens aéreas de imóveis, terrenos, condomínios e lançamentos no RJ: vizinhança, acessos, vista e dimensão do lote em fotos e vídeos 4K HDR.",
    "h1": "O imóvel inteiro, com a vizinhança e a vista no mesmo quadro",
    "intro": "Para quem compra, localização é metade da decisão. A imagem aérea mostra o lote completo, o que há em volta, a distância até vias e serviços e a vista que o imóvel realmente tem.",
    "uses": [("Venda e locação", "Fotos e vídeos para anúncios em portais, site da imobiliária e redes sociais."),
             ("Terrenos e lotes", "Visão do terreno inteiro, confrontantes, acessos e topografia aparente."),
             ("Condomínios e lançamentos", "Material institucional mostrando área comum, lazer e o bairro em volta."),
             ("Vista do imóvel", "Simulação da vista em diferentes alturas para apartamentos e coberturas.")],
    "faq": [("Dá para filmar em condomínio fechado?", "Sim, com autorização da administração do condomínio e respeitando a privacidade dos moradores. Essa autorização é combinada antes do voo."),
            ("As imagens servem para portais imobiliários?", "Sim. Entregamos as fotos editadas nas proporções usadas pelos principais portais e redes.")],
  },
  {
    "slug": "obras-e-estruturas", "icon": "obras", "cat": "Obras & Estruturas",
    "name": "Obras e estruturas",
    "card": "Registro periódico do andamento, comparativo entre etapas e material para relatório de cliente.",
    "title": "Acompanhamento de obras com drone no RJ | Drone Vision",
    "desc": "Registro aéreo periódico de obras e estruturas no Rio de Janeiro: andamento por etapa, comparativos e material para relatórios a clientes e investidores.",
    "h1": "Sua obra registrada do mesmo ponto, etapa por etapa",
    "intro": "Voos repetidos dos mesmos ângulos criam uma linha do tempo visual da obra. Fica fácil comparar etapas, mostrar avanço a clientes e investidores e guardar um histórico confiável do canteiro.",
    "uses": [("Andamento periódico", "Voos em intervalos combinados, sempre dos mesmos pontos, para comparar a evolução."),
             ("Relatórios", "Imagens organizadas por data para anexar a relatórios de obra e apresentações."),
             ("Marketing do empreendimento", "Vídeos do avanço para divulgar o lançamento e manter compradores informados."),
             ("Estruturas e coberturas", "Vista geral de galpões, coberturas e estruturas metálicas.")],
    "faq": [("Com que frequência vocês fazem o registro?", "A frequência é definida com você conforme o ritmo da obra, por exemplo semanal, quinzenal ou mensal."),
            ("Vocês entregam as imagens organizadas por data?", "Sim. Cada voo é entregue identificado pela data, o que facilita montar o comparativo entre etapas.")],
  },
  {
    "slug": "inspecoes-tecnicas", "icon": "inspecoes", "cat": "Inspeções técnicas",
    "name": "Inspeções técnicas",
    "card": "Telhados, placas solares, fachadas e torres de difícil acesso, com imagem nítida e sem andaime.",
    "title": "Inspeção com drone de telhados, placas solares e fachadas | RJ",
    "desc": "Inspeção visual com drone no Rio de Janeiro: telhados, sistemas fotovoltaicos, fachadas e estruturas de difícil acesso, com imagens nítidas e sem andaime.",
    "h1": "Ver de perto o que está alto, sem subir no telhado",
    "intro": "Telhados, placas solares, fachadas e torres podem ser examinados de perto pelo drone, com segurança e sem montar andaime. As imagens ajudam o técnico responsável a avaliar o estado da estrutura e planejar a manutenção.",
    "uses": [("Telhados e coberturas", "Estado de telhas, calhas, cumeeiras e pontos de infiltração aparentes."),
             ("Sistemas fotovoltaicos", "Vista dos módulos, fixações e sujeira acumulada, antes e depois da limpeza."),
             ("Fachadas", "Fissuras, desplacamentos e pontos de atenção em prédios e muros altos."),
             ("Torres e estruturas", "Registro de antenas, torres e estruturas metálicas de difícil acesso.")],
    "faq": [("A inspeção com drone substitui o laudo técnico?", "Não. O drone gera as imagens; a avaliação e o laudo são do engenheiro ou técnico responsável. Nosso trabalho é entregar material nítido para essa análise."),
            ("Dá para inspecionar placas solares?", "Sim. É possível registrar os módulos, a fixação e o estado do telhado em volta, como no trabalho que aparece no nosso portfólio.")],
    "hero": "inspecao-telhado-solar-01",
  },
  {
    "slug": "agronegocio", "icon": "agro", "cat": "Agronegócio",
    "name": "Agronegócio",
    "card": "Visão geral de áreas de plantio, pastagens e infraestrutura rural, para acompanhamento e divulgação.",
    "title": "Imagens aéreas com drone para propriedades rurais | Drone Vision",
    "desc": "Fotos e vídeos aéreos de fazendas, sítios, plantações e pastagens no Rio de Janeiro, para acompanhamento da propriedade, venda e divulgação.",
    "h1": "A propriedade inteira em uma imagem",
    "intro": "Do alto fica claro o que no chão leva horas para percorrer: limites, áreas de plantio, pastagens, açudes, estradas internas e benfeitorias. Material útil para gestão, venda ou divulgação da propriedade.",
    "uses": [("Visão geral da propriedade", "Imagens amplas de fazendas e sítios, com limites e benfeitorias."),
             ("Acompanhamento de áreas", "Registro periódico de plantios e pastagens para comparar ao longo do tempo."),
             ("Venda de propriedades", "Fotos e vídeos para anúncio de fazendas, sítios e haras."),
             ("Eventos e turismo rural", "Material para divulgação de turismo rural, agroindústrias e eventos no campo.")],
    "faq": [("Vocês fazem mapeamento técnico ou agricultura de precisão?", "Nosso serviço é de imagens aéreas (fotos e vídeos) para acompanhamento visual e divulgação. Para levantamentos técnicos específicos, conte o que precisa pelo WhatsApp e avaliamos juntos."),
            ("Atendem fora da capital?", "Sim. A base é no Rio de Janeiro e outras regiões são atendidas sob consulta.")],
  },
]

NAV = [("/servicos/", "Serviços"), ("/regularizacao-de-drones/", "Regularização"), ("/portfolio/", "Portfólio"), ("/contato/", "Contato")]

ORG = {
  "@type": "ProfessionalService", "@id": SITE + "/#empresa", "name": "Drone Vision",
  "description": "Imagens e filmagens aéreas 4K HDR com drone e assessoria em regularização de drones e pilotos (ANAC, ANATEL e DECEA).",
  "url": SITE + "/", "logo": SITE + "/assets/img/logo-512.png", "image": SITE + "/assets/img/cidade-noite-aerea-01-1920.jpg",
  "telephone": "+55 21 96681-0304", "email": EMAIL,
  "address": {"@type": "PostalAddress", "addressLocality": "Rio de Janeiro", "addressRegion": "RJ", "addressCountry": "BR"},
  "areaServed": {"@type": "State", "name": "Rio de Janeiro"},
  "sameAs": [f"https://www.instagram.com/{INSTA}/"],
}

def crumbs_ld(trail):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": n + 1, "name": name, "item": SITE + url} for n, (url, name) in enumerate(trail)]}

def crumbs_html(trail):
    li = []
    for n, (url, name) in enumerate(trail):
        li.append(f'<li><a href="{url}">{e(name)}</a></li>' if n < len(trail) - 1 else f'<li aria-current="page">{e(name)}</li>')
    return f'<nav aria-label="Trilha"><ol class="crumbs">{"".join(li)}</ol></nav>'

def faq_ld(faq):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}

def faq_html(faq):
    return '<div class="faq">' + "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in faq) + "</div>"

def page(path, title, desc, body, ld=(), scripts=(), current="", noindex=False, preload=None, og=OG):
    url = SITE + path
    graph = {"@context": "https://schema.org", "@graph": [ORG, *ld]}
    nav = "".join(f'<a href="{u}"{" aria-current=page" if u == current else ""}>{t}</a>' for u, t in NAV)
    pre = f'<link rel="preload" as="image" href="{preload}" fetchpriority="high">' if preload else ""
    extra = "".join(f'<script src="{s}" defer></script>' for s in scripts)
    robots = '<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{robots}
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#070B14">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Drone Vision">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}{og}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@125,700..900&family=Manrope:wght@400;600;700&display=swap" rel="stylesheet">
{pre}
<link rel="stylesheet" href="/assets/css/site.css">
<script type="application/ld+json">{json.dumps(graph, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header class="site-head"><div class="wrap">
  <a class="brand" href="/" aria-label="Drone Vision, página inicial"><img src="/assets/img/logo-160.webp" width="46" height="46" alt=""><span>DRONE<b>VISION</b></span></a>
  <nav class="nav" id="nav" aria-label="Principal">{nav}<a class="btn btn-wa" href="{wa()}" target="_blank" rel="noopener">{ICON['wa']}Pedir orçamento</a></nav>
  <a class="btn btn-wa head-cta" href="{wa()}" target="_blank" rel="noopener">{ICON['wa']}Pedir orçamento</a>
  <button class="menu-btn" type="button" aria-label="Abrir menu" aria-controls="nav" aria-expanded="false"><i></i><i></i><i></i></button>
</div></header>
<main id="conteudo">
{body}
</main>
<footer class="site-foot"><div class="wrap">
  <div><img src="/assets/img/logo-160.webp" width="72" height="72" alt="Drone Vision" loading="lazy"><p>Soluções aéreas e imagens corporativas. Filmagens 4K HDR e regularização de drones no Rio de Janeiro.</p></div>
  <div><h2>Serviços</h2><ul>{"".join(f'<li><a href="/servicos/{s["slug"]}/">{e(s["name"])}</a></li>' for s in SERVICES)}<li><a href="/regularizacao-de-drones/">Regularização de drones</a></li></ul></div>
  <div><h2>Site</h2><ul><li><a href="/">Início</a></li><li><a href="/servicos/">Serviços</a></li><li><a href="/portfolio/">Portfólio</a></li><li><a href="/contato/">Contato</a></li></ul></div>
  <div><h2>Contato</h2><ul><li><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp {WA_FMT}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="https://www.instagram.com/{INSTA}/" target="_blank" rel="noopener">Instagram @{INSTA}</a></li><li><p>Rio de Janeiro, RJ</p></li></ul></div>
  <div class="copy"><p>© <span data-year>{datetime.date.today().year}</span> Drone Vision. Todos os direitos reservados.</p><p>ANAC · ANATEL · DECEA</p></div>
</div></footer>
<a class="wa-float" href="{wa()}" target="_blank" rel="noopener" aria-label="Conversar no WhatsApp">{ICON['wa']}</a>
<svg id="mini" viewBox="0 0 72 44" aria-hidden="true">
  <path d="M36 30 L58 44 L14 44Z" fill="#38B6E0" opacity=".12"/>
  <g stroke="#9fdcf2" stroke-width="2.4" stroke-linecap="round"><path d="M36 20 L12 12M36 20 L60 12"/></g>
  <ellipse cx="36" cy="21" rx="11" ry="6" fill="#dff3fb"/><ellipse cx="36" cy="19.5" rx="7" ry="3" fill="#38B6E0"/>
  <circle cx="36" cy="28" r="3.4" fill="#0E1525" stroke="#38B6E0" stroke-width="1.6"/><circle cx="36" cy="28" r="1" fill="#38B6E0"/>
  <g fill="#38B6E0"><ellipse class="rot" cx="12" cy="9" rx="10" ry="1.6"/><ellipse class="rot" cx="60" cy="9" rx="10" ry="1.6"/></g>
  <circle cx="12" cy="12" r="2" fill="#dff3fb"/><circle cx="60" cy="12" r="2" fill="#dff3fb"/>
</svg>
<script src="/assets/js/site.js" defer></script>{extra}
</body>
</html>
"""

def write(path, content):
    out = os.path.join(ROOT, path.strip("/"), "index.html") if path.endswith("/") else os.path.join(ROOT, path.strip("/"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f: f.write(content)

def pic(name, alt, sizes="100vw", lazy=True, cls=""):
    l = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    return (f'<img{f" class={cls}" if cls else ""} src="/assets/img/{name}-1920.webp" srcset="/assets/img/{name}-960.webp 960w, /assets/img/{name}-1920.webp 1920w" '
            f'sizes="{sizes}" width="1920" height="1080" alt="{e(alt)}"{l}>')

def cards(items):
    return '<ul class="cards">' + "".join(
        f'<li class="rv" style="--d:{n}"><a class="card" href="/servicos/{s["slug"]}/">{ICON[s["icon"]].replace("<svg", "<svg class=\"ic\"", 1)}<h3>{e(s["name"])}</h3><p>{e(s["card"])}</p><span class="link">Ver serviço</span></a></li>'
        for n, s in enumerate(items)) + "</ul>"

STEPS = [("Briefing", "Você conta o que precisa, onde e para que vai usar as imagens. Respondemos com proposta e prazo."),
         ("Planejamento", "Definimos horário, ângulos e altitude e verificamos o espaço aéreo e as autorizações do local."),
         ("Voo", "Operação no local com equipamento cadastrado e piloto habilitado, captando em 4K HDR."),
         ("Entrega", "Fotos tratadas e vídeos editados nos formatos combinados, prontos para site, redes e relatórios.")]

def flight(alt=False):
    li = "".join(f'<li class="rv" style="--d:{n}"><h3>{e(t)}</h3><p>{e(d)}</p></li>' for n, (t, d) in enumerate(STEPS))
    return f"""<div class="flight">
  <svg class="route" viewBox="0 0 1160 60" preserveAspectRatio="none" aria-hidden="true">
    <path d="M26 2 C 140 50, 230 -46, 322 2 S 520 50, 618 2 S 820 -46, 914 2 S 1100 50, 1160 30"/>
    <path class="trail" d="M26 2 C 140 50, 230 -46, 322 2 S 520 50, 618 2 S 820 -46, 914 2 S 1100 50, 1160 30"/>
    <g class="route-drone" fill="#38B6E0"><rect x="10" y="10" width="16" height="8" rx="4"/><rect x="0" y="6" width="12" height="2" rx="1"/><rect x="24" y="6" width="12" height="2" rx="1"/></g>
  </svg>
  <ol class="steps">{li}</ol>
</div>"""

def band(title="Vamos colocar seu projeto no ar?", text="Conte o que precisa pelo WhatsApp e receba uma proposta.", msg="Olá! Quero um orçamento."):
    return f"""<section class="band"><div class="wrap">
  <div class="rv"><h2>{e(title)}</h2><p class="lead">{e(text)}</p></div>
  <div class="cta rv" style="--d:1"><a class="btn btn-wa" href="{wa(msg)}" target="_blank" rel="noopener">{ICON['wa']}Falar no WhatsApp</a><a class="btn btn-ghost" href="/contato/">Outros contatos</a></div>
</div></section>"""

PORT = json.load(open(os.path.join(ROOT, "portfolio.json"), encoding="utf-8"))

def strip():
    imgs = [p for p in PORT if p["type"] == "image"][:4]
    vid = next((p for p in PORT if p["type"] == "video"), None)
    figs = []
    if vid:
        figs.append(f'<figure class="rv"><video src="{vid["url"]}" poster="{vid["thumb"]}" muted loop playsinline autoplay preload="none" aria-label="{e(vid["title"])}"></video><figcaption>{e(vid["title"])}</figcaption></figure>')
    for n, p in enumerate(imgs[:4 if not vid else 4]):
        figs.append(f'<figure class="rv" style="--d:{n+1}"><img src="{p["thumb"]}" width="960" height="540" alt="{e(p["title"])}" loading="lazy" decoding="async"><figcaption>{e(p["cat"])}</figcaption></figure>')
    return '<div class="strip">' + "".join(figs[:5]) + "</div>"

# ---------------- HOME ----------------
home = f"""<section class="hero">
  <div class="hero-bg">{pic("cidade-noite-aerea-01", "", lazy=False)}</div>
  <div class="hud" aria-hidden="true"><i class="a"></i><i class="b"></i><i class="c"></i><i class="d"></i><span class="scan"></span><span class="cross"></span>
    <small class="rec">REC 4K HDR</small><small class="clk" id="clk">00:00:00</small><small class="bat">GPS ● ● ● ●</small><small class="alt">ALT <b id="alt">120</b> m</small></div>
  <div class="wrap">
    <span class="eyebrow rv">Filmagem aérea com drone · Rio de Janeiro</span>
    <h1 class="rv" style="--d:1">O ângulo que sua obra, seu hotel e sua lavoura <span class="hl">ainda não mostraram.</span></h1>
    <p class="sub rv" style="--d:2">Imagens e filmagens aéreas em 4K HDR, com operação e documentação regulatória resolvidas por quem entende de espaço aéreo.</p>
    <div class="cta rv" style="--d:3"><a class="btn btn-wa" href="{wa()}" target="_blank" rel="noopener">{ICON['wa']}Falar no WhatsApp</a><a class="btn btn-ghost" href="/portfolio/">Ver portfólio</a></div>
  </div>
  <span class="scroll-cue" aria-hidden="true"></span>
</section>

<div class="stats"><div class="wrap"><ul>
  <li class="rv"><b>4K HDR</b><span>Imagem com faixa dinâmica ampla, pronta para cinema e web</span></li>
  <li class="rv" style="--d:1"><b>5 segmentos</b><span>Hotelaria, imóveis, obras, inspeções e agro</span></li>
  <li class="rv" style="--d:2"><b>3 órgãos</b><span>ANAC, ANATEL e DECEA tratados por nós</span></li>
  <li class="rv" style="--d:3"><b>RJ</b><span>Base no Rio de Janeiro, outras regiões sob consulta</span></li>
</ul></div></div>

<section id="servicos"><div class="wrap">
  <span class="eyebrow rv">Serviços</span>
  <h2 class="rv">Quem contrata a Drone Vision</h2>
  <p class="lead rv">Cada segmento pede um tipo de imagem diferente. Planejamos o voo para o resultado que você vai usar.</p>
  {cards(SERVICES)}
</div></section>

<section class="alt"><div class="wrap">
  <span class="eyebrow rv">Como trabalhamos</span>
  <h2 class="rv">Do briefing à entrega, em quatro etapas</h2>
  {flight()}
</div></section>

<section><div class="wrap">
  <span class="eyebrow rv">Portfólio</span>
  <h2 class="rv">Um pouco do que já foi registrado do ar</h2>
  {strip()}
  <p style="margin-top:1.8rem" class="rv"><a class="link" href="/portfolio/">Ver o portfólio completo</a></p>
</div></section>

<section class="alt"><div class="wrap split">
  <div>
    <span class="eyebrow rv">Regularização</span>
    <h2 class="rv">Drone e piloto em dia com ANAC, ANATEL e DECEA</h2>
    <p class="lead rv">Além de voar, ajudamos quem tem drone a operar dentro da lei: cadastro do equipamento, homologação e orientação para a habilitação e o acesso ao espaço aéreo.</p>
    <div class="cta rv" style="margin-top:2rem"><a class="btn btn-cy" href="/regularizacao-de-drones/">Entender a regularização</a></div>
  </div>
  <aside class="box rv" style="--d:1">{ICON['reg'].replace('<svg', '<svg style="width:48px;height:48px;color:var(--cyan);margin-bottom:1rem"', 1)}
    <h3>Por que regularizar?</h3>
    <p>Operar drone sem cadastro e homologação pode resultar em <b>apreensão do equipamento</b>, multa e responsabilização civil.</p>
    <div class="tags"><span>ANAC</span><span>ANATEL</span><span>DECEA</span></div>
  </aside>
</div></section>

{band()}
"""
write("/", page("/", "Drone Vision | Filmagem aérea com drone 4K HDR no Rio de Janeiro",
  "Fotos e filmagens aéreas com drone em 4K HDR para hotelaria, imóveis, obras, inspeções e agro no Rio de Janeiro, com assessoria em ANAC, ANATEL e DECEA.",
  home, ld=[{"@type": "WebSite", "@id": SITE + "/#site", "url": SITE + "/", "name": "Drone Vision", "inLanguage": "pt-BR", "publisher": {"@id": SITE + "/#empresa"}}],
  preload="/assets/img/cidade-noite-aerea-01-1920.webp"))

# ---------------- SERVIÇOS (hub) ----------------
REG_CARD = '<li class="rv" style="--d:5"><a class="card" href="/regularizacao-de-drones/">' + ICON["reg"].replace("<svg", '<svg class="ic"', 1) + '<h3>Regularização de drones</h3><p>Cadastro na ANAC, homologação na ANATEL e orientação sobre habilitação de piloto e acesso ao espaço aéreo.</p><span class="link">Ver serviço</span></a></li>'
HUB_CARDS = cards(SERVICES).replace("</ul>", REG_CARD + "</ul>")
trail = [("/", "Início"), ("/servicos/", "Serviços")]
body = f"""<section class="page-hero"><div class="wrap">
  {crumbs_html(trail)}
  <span class="eyebrow rv">Serviços</span>
  <h1 class="rv">Filmagem e fotografia aérea com drone para cada tipo de negócio</h1>
  <p class="lead rv">Escolha o segmento para ver como as imagens aéreas são usadas, o que entregamos e as dúvidas mais comuns.</p>
</div></section>
<section><div class="wrap">
  {HUB_CARDS}
</div></section>
<section class="alt"><div class="wrap">
  <span class="eyebrow rv">Como trabalhamos</span>
  <h2 class="rv">Do briefing à entrega</h2>
  {flight()}
</div></section>
{band()}"""
write("/servicos/", page("/servicos/", "Serviços de filmagem aérea com drone no RJ | Drone Vision",
  "Filmagem e fotografia aérea com drone para hotelaria, imóveis, obras, inspeções técnicas e agronegócio no Rio de Janeiro, além de regularização de drones.",
  body, ld=[crumbs_ld(trail)], current="/servicos/"))

# ---------------- SERVIÇOS (páginas) ----------------
for s in SERVICES:
    path = f"/servicos/{s['slug']}/"
    trail = [("/", "Início"), ("/servicos/", "Serviços"), (path, s["name"])]
    hero_img = s.get("hero")
    hero = (f'<section class="page-hero has-img"><div class="ph-img">{pic(hero_img, "", lazy=False)}</div><div class="wrap">' if hero_img
            else '<section class="page-hero"><div class="wrap">')
    rel = [p for p in PORT if p["cat"] == s["cat"]]
    gallery = ""
    if len(rel) >= 3:
        figs = "".join(f'<figure class="rv" style="--d:{n}"><img src="{p["thumb"]}" width="960" height="540" alt="{e(p["title"])}" loading="lazy" decoding="async"><figcaption>{e(p["title"])}</figcaption></figure>' for n, p in enumerate(rel[:3]))
        gallery = f"""<section><div class="wrap"><span class="eyebrow rv">Do nosso portfólio</span><h2 class="rv">Trabalhos neste segmento</h2><div class="strip three">{figs}</div><p style="margin-top:1.8rem" class="rv"><a class="link" href="/portfolio/">Ver portfólio completo</a></p></div></section>"""
    others = [o for o in SERVICES if o is not s]
    msg = f"Olá! Quero um orçamento de imagens aéreas para {s['name'].lower()}."
    body = f"""{hero}
  {crumbs_html(trail)}
  <span class="eyebrow rv">{e(s['name'])}</span>
  <h1 class="rv">{e(s['h1'])}</h1>
  <p class="lead rv">{e(s['intro'])}</p>
  <div class="cta rv" style="margin-top:2rem"><a class="btn btn-wa" href="{wa(msg)}" target="_blank" rel="noopener">{ICON['wa']}Pedir orçamento</a><a class="btn btn-ghost" href="/portfolio/">Ver portfólio</a></div>
</div></section>
<section><div class="wrap">
  <span class="eyebrow rv">Aplicações</span>
  <h2 class="rv">Onde as imagens aéreas fazem diferença</h2>
  <ul class="uses">{"".join(f'<li class="rv" style="--d:{n}"><b>{e(t)}</b><span>{e(d)}</span></li>' for n, (t, d) in enumerate(s["uses"]))}</ul>
</div></section>
{gallery}
<section class="alt"><div class="wrap">
  <span class="eyebrow rv">Como trabalhamos</span>
  <h2 class="rv">Do briefing à entrega</h2>
  {flight()}
</div></section>
<section><div class="wrap split">
  <div><span class="eyebrow rv">Dúvidas frequentes</span><h2 class="rv">Perguntas sobre {e(s['name'].lower())}</h2>{faq_html(s['faq'])}</div>
  <aside class="box rv" style="--d:1"><h3>Outros serviços</h3><ul class="ck" style="margin:1rem 0 0">{"".join(f'<li><a class="link" href="/servicos/{o["slug"]}/">{e(o["name"])}</a></li>' for o in others)}<li><a class="link" href="/regularizacao-de-drones/">Regularização de drones</a></li></ul></aside>
</div></section>
{band(msg=msg)}"""
    ld = [crumbs_ld(trail), faq_ld(s["faq"]),
          {"@type": "Service", "name": s["title"].split(" | ")[0], "serviceType": "Filmagem aérea com drone", "description": s["desc"],
           "provider": {"@id": SITE + "/#empresa"}, "areaServed": {"@type": "State", "name": "Rio de Janeiro"}, "url": SITE + path}]
    write(path, page(path, s["title"], s["desc"], body, ld=ld, current="/servicos/",
                     preload=f"/assets/img/{hero_img}-1920.webp" if hero_img else None))

# ---------------- REGULARIZAÇÃO ----------------
REG_FAQ = [
  ("Preciso cadastrar meu drone na ANAC?", "Em regra, sim. A ANAC exige o cadastro de drones acima do peso mínimo previsto na regulamentação, por meio do sistema SISANT. Ajudamos a verificar o enquadramento do seu equipamento e a fazer o cadastro."),
  ("O que é a homologação na ANATEL?", "Drones usam radiofrequência no controle e na transmissão de imagem. Por isso o equipamento precisa estar homologado pela ANATEL. Orientamos o processo para linhas DJI e para montagens personalizadas."),
  ("Para que serve o DECEA?", "O DECEA controla o espaço aéreo brasileiro. Dependendo do local e do tipo de voo, é preciso solicitar acesso ao espaço aéreo pelo sistema do DECEA antes de voar. Explicamos como fazer a solicitação."),
  ("Quem voa por lazer também precisa regularizar?", "As exigências variam conforme o peso do drone e o tipo de uso. Mesmo no uso recreativo há regras de cadastro e de espaço aéreo. Conte qual é o seu equipamento e indicamos o caminho."),
]
trail = [("/", "Início"), ("/regularizacao-de-drones/", "Regularização de drones")]
body = f"""<section class="page-hero"><div class="wrap">
  {crumbs_html(trail)}
  <span class="eyebrow rv">Regularização</span>
  <h1 class="rv">Regularização de drones e pilotos: ANAC, ANATEL e DECEA</h1>
  <p class="lead rv">Voe com segurança e dentro da lei. Consultoria completa para regularizar equipamentos e adequar pilotos junto aos órgãos reguladores brasileiros.</p>
  <div class="cta rv" style="margin-top:2rem"><a class="btn btn-cy" href="{wa('Olá! Quero solicitar consultoria de regularização de drone.')}" target="_blank" rel="noopener">Solicitar consultoria</a></div>
</div></section>
<section><div class="wrap split">
  <div>
    <span class="eyebrow rv">O que fazemos</span>
    <h2 class="rv">Três órgãos, um só atendimento</h2>
    <ul class="ck">
      <li class="rv"><b>Cadastro de drone na ANAC</b><span>Assessoria no registro do equipamento no SISANT e obtenção da certidão de cadastro.</span></li>
      <li class="rv" style="--d:1"><b>Homologação ANATEL</b><span>Adequação e certificação de radiofrequência para equipamentos, incluindo linhas DJI e montagens personalizadas.</span></li>
      <li class="rv" style="--d:2"><b>Habilitação de piloto e DECEA</b><span>Orientação sobre a prova da ANAC, a habilitação do piloto e a solicitação de acesso ao espaço aéreo junto ao DECEA.</span></li>
    </ul>
  </div>
  <aside class="box rv" style="--d:1"><h3>Por que regularizar?</h3>
    <p>A operação de aeronaves não tripuladas sem a devida homologação e cadastro pode resultar em <b>apreensão do equipamento</b>, multa e responsabilização civil.</p>
    <p>Garanta que seus voos, comerciais ou recreativos, estejam resguardados legalmente.</p>
    <div class="tags"><span>ANAC</span><span>ANATEL</span><span>DECEA</span></div>
  </aside>
</div></section>
<section class="alt"><div class="wrap">
  <span class="eyebrow rv">Dúvidas frequentes</span>
  <h2 class="rv">Perguntas sobre regularização</h2>
  {faq_html(REG_FAQ)}
  <p class="note rv" style="margin-top:1.5rem">As regras dos órgãos reguladores podem mudar. Na consultoria, conferimos sempre a regulamentação em vigor para o seu caso.</p>
</div></section>
{band("Seu drone está regularizado?", "Conte o modelo do equipamento e como pretende voar. Indicamos o que falta.", "Olá! Quero solicitar consultoria de regularização de drone.")}"""
write("/regularizacao-de-drones/", page("/regularizacao-de-drones/", "Regularização de drones: ANAC, ANATEL e DECEA | Drone Vision",
  "Consultoria para regularizar drones e pilotos: cadastro na ANAC (SISANT), homologação ANATEL e orientação sobre espaço aéreo no DECEA. Atendimento no Rio de Janeiro.",
  body, ld=[crumbs_ld(trail), faq_ld(REG_FAQ), {"@type": "Service", "name": "Regularização de drones e pilotos", "serviceType": "Consultoria regulatória de drones",
  "provider": {"@id": SITE + "/#empresa"}, "areaServed": {"@type": "Country", "name": "Brasil"}, "url": SITE + "/regularizacao-de-drones/"}],
  current="/regularizacao-de-drones/"))

# ---------------- PORTFÓLIO ----------------
def item_html(p):
    from datetime import date
    y, m, _ = p["date"].split("-")
    meses = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
    sm = f'{p["cat"]} · {meses[int(m)-1]} de {y}'
    pl = '<span class="pl"></span>' if p["type"] == "video" else ""
    return f'<figure class="item"><div class="ph"><img src="{p["thumb"]}" width="960" height="540" alt="{e(p["title"])}" loading="lazy" decoding="async">{pl}</div><h3>{e(p["title"])}</h3><small>{e(sm)}</small></figure>'

trail = [("/", "Início"), ("/portfolio/", "Portfólio")]
body = f"""<section class="page-hero"><div class="wrap">
  {crumbs_html(trail)}
  <span class="eyebrow rv">Portfólio</span>
  <h1 class="rv">Um pouco do que já foi registrado do ar</h1>
  <p class="lead rv">Seleção de sobrevoos e trabalhos da Drone Vision. Clique para ampliar as fotos e assistir aos vídeos.</p>
</div></section>
<section style="padding-top:2rem"><div class="wrap">
  <div class="bar">
    <span role="group" aria-label="Tipo" style="display:contents"><button type="button" data-f="all" aria-pressed="true">Todos</button><button type="button" data-f="image" aria-pressed="false">Fotos</button><button type="button" data-f="video" aria-pressed="false">Vídeos</button></span>
    <select id="catf" aria-label="Filtrar por categoria"><option value="">Todas as categorias</option></select>
  </div>
  <div class="grid" id="grid" aria-live="polite">{"".join(item_html(p) for p in PORT)}</div>
  <div class="cta" style="margin-top:2.5rem"><a class="btn btn-ghost" href="https://www.instagram.com/{INSTA}/" target="_blank" rel="noopener">{ICON['ig']}Veja mais no Instagram</a></div>
  <p class="copy" style="border:0;margin-top:2rem;padding:0"><button type="button" class="note" data-admin style="background:none;border:0;cursor:pointer;padding:0">Área administrativa</button></p>
</div></section>
<dialog id="lb" aria-label="Visualização da mídia"><button class="btn btn-ghost sm x" id="lbx" type="button">Fechar</button><div id="lbc"></div><p id="lbt"></p></dialog>
<aside id="panel" aria-label="Painel administrativo" aria-hidden="true">
  <div class="ph-head"><h2>Painel Drone Vision</h2><button class="btn btn-ghost sm" id="pc" type="button">Fechar</button></div>
  <form id="lock"><label>Senha do painel<input type="password" id="pw" autocomplete="current-password" required></label><button class="btn btn-cy" type="submit">Entrar</button><p class="note" id="lmsg"></p></form>
  <div id="app">
    <h3>1. Enviar mídia</h3>
    <div class="two"><label>Cloud name<input id="cn" autocomplete="off"></label><label>Upload preset (unsigned)<input id="up" autocomplete="off"></label></div>
    <div class="two"><label>Título do próximo envio<input id="tt" placeholder="ex.: Pousada em Penedo"></label><label>Categoria<select id="tc"></select></label></div>
    <button class="btn btn-cy" id="send" type="button">Enviar fotos e vídeos</button>
    <p id="msg" role="status"></p>
    <label style="margin-top:1.2rem">Ou adicionar por link do Cloudinary<input id="lk" placeholder="https://res.cloudinary.com/.../upload/..."></label><button class="btn btn-ghost sm" id="addlk" type="button">Adicionar link</button>
    <h3>2. Gerenciar itens</h3>
    <div id="list"></div>
    <h3>3. Publicar para todos</h3>
    <p class="note" style="margin-bottom:.8rem">A lista editada fica só neste navegador. Exporte o <b>portfolio.json</b> e suba para a raiz do repositório para o público ver.</p>
    <div class="cta"><button class="btn btn-cy sm" id="exp" type="button">Exportar portfolio.json</button><label class="btn btn-ghost sm" style="margin:0;cursor:pointer">Importar JSON<input id="imp" type="file" accept=".json" hidden></label><button class="btn btn-ghost sm" id="reset" type="button">Descartar rascunho local</button></div>
  </div>
</aside>
<script src="https://upload-widget.cloudinary.com/global/all.js" async></script>
{band()}"""
gal_ld = {"@type": "CollectionPage", "name": "Portfólio Drone Vision", "url": SITE + "/portfolio/", "hasPart": [
  ({"@type": "VideoObject", "name": p["title"], "contentUrl": SITE + p["url"], "thumbnailUrl": SITE + p["thumb"], "uploadDate": p["date"], "description": p["title"]}
   if p["type"] == "video" else {"@type": "ImageObject", "name": p["title"], "contentUrl": SITE + p["url"], "thumbnailUrl": SITE + p["thumb"], "datePublished": p["date"]})
  for p in PORT if not p["url"].startswith("http")]}
write("/portfolio/", page("/portfolio/", "Portfólio de fotos e vídeos aéreos com drone | Drone Vision",
  "Veja fotos e vídeos aéreos feitos pela Drone Vision no Rio de Janeiro: inspeções de telhados e placas solares, sobrevoos urbanos noturnos e mais.",
  body, ld=[crumbs_ld(trail), gal_ld], scripts=["/assets/js/portfolio.js"], current="/portfolio/"))

# ---------------- CONTATO ----------------
trail = [("/", "Início"), ("/contato/", "Contato")]
opts = "".join(f"<option>{e(s['name'])}</option>" for s in SERVICES) + "<option>Regularização de drone</option><option>Outro</option>"
body = f"""<section class="page-hero"><div class="wrap">
  {crumbs_html(trail)}
  <span class="eyebrow rv">Contato</span>
  <h1 class="rv">Fale com a Drone Vision</h1>
  <p class="lead rv">O jeito mais rápido é o WhatsApp. Preencha o formulário e a mensagem já sai pronta, ou escolha outro canal.</p>
</div></section>
<section><div class="wrap contact-grid">
  <div>
    <h2 class="rv" style="font-size:1.6rem">Canais</h2>
    <ul class="channels">
      <li class="rv"><a href="{wa()}" target="_blank" rel="noopener">{ICON['wa']}<div><b>WhatsApp</b><span>{WA_FMT}</span></div></a></li>
      <li class="rv" style="--d:1"><a href="mailto:{EMAIL}">{ICON['mail']}<div><b>E-mail</b><span>{EMAIL}</span></div></a></li>
      <li class="rv" style="--d:2"><a href="https://www.instagram.com/{INSTA}/" target="_blank" rel="noopener">{ICON['ig']}<div><b>Instagram</b><span>@{INSTA}</span></div></a></li>
    </ul>
    <p class="note rv" style="margin-top:1.5rem">Base no Rio de Janeiro, RJ. Outras regiões sob consulta.</p>
  </div>
  <form class="wa-form rv" id="wa-form" data-wa="{WA}" style="--d:1">
    <h2 style="font-size:1.6rem;margin-bottom:1.4rem">Pedir orçamento</h2>
    <label>Seu nome<input name="nome" required autocomplete="name"></label>
    <label>Serviço<select name="servico" required>{opts}</select></label>
    <label>Local do voo (bairro, cidade)<input name="local" autocomplete="address-level2"></label>
    <label>Conte um pouco do que precisa<textarea name="mensagem"></textarea></label>
    <button class="btn btn-wa" type="submit">{ICON['wa']}Enviar pelo WhatsApp</button>
    <p class="note" style="margin-top:.8rem">Ao enviar, o WhatsApp abre com a mensagem preenchida. Nada é guardado neste site.</p>
  </form>
</div></section>"""
write("/contato/", page("/contato/", "Contato e orçamento | Drone Vision – filmagem aérea no RJ",
  "Peça orçamento de filmagem aérea com drone ou de regularização de drones. WhatsApp (21) 96681-0304, e-mail jorge@dronevision.com.br e Instagram @dronevision456.",
  body, ld=[crumbs_ld(trail), {"@type": "ContactPage", "url": SITE + "/contato/", "about": {"@id": SITE + "/#empresa"}}], current="/contato/"))

# ---------------- 404 ----------------
body = f"""<section class="lost"><div class="wrap">
  <p class="code" aria-hidden="true">404</p>
  <h1 style="font-size:clamp(1.8rem,4vw,2.6rem);margin:1rem auto">Perdemos o sinal desta página</h1>
  <p class="lead" style="margin-inline:auto">O endereço pode ter mudado com o novo site. Volte para a base e siga por lá.</p>
  <div class="cta" style="justify-content:center;margin-top:2rem"><a class="btn btn-cy" href="/">Voltar ao início</a><a class="btn btn-ghost" href="/servicos/">Ver serviços</a></div>
</div></section>"""
write("/404.html", page("/404.html", "Página não encontrada | Drone Vision", "Esta página não existe.", body, noindex=True))

# ---------------- sitemap e robots ----------------
urls = ["/", "/servicos/"] + [f"/servicos/{s['slug']}/" for s in SERVICES] + ["/regularizacao-de-drones/", "/portfolio/", "/contato/"]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f"  <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n"
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(sm)
open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
print("ok:", len(urls), "páginas + 404")

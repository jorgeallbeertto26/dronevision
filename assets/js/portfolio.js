/* Drone Vision — portfólio, lightbox e painel administrativo
   CONFIGURAÇÃO
   cloud/preset: Cloudinary (preset "unsigned").
   passHash: SHA-256 da senha do painel (digite uma senha no painel, copie o hash que aparecer e cole aqui). */
const CFG = { cloud: "iwmbn2fr", preset: "", tag: "dronevision-portfolio", passHash: "" };
const CATS = ["Imagens aéreas", "Hotelaria & Pousadas", "Imóveis", "Obras & Estruturas", "Inspeções técnicas", "Agronegócio"];

(() => {
  const $ = s => document.querySelector(s);
  const grid = $("#grid");
  if (!grid) return;
  const st = { get(k) { try { return localStorage.getItem(k) } catch (e) { return null } }, set(k, v) { try { localStorage.setItem(k, v) } catch (e) {} } };
  const opts = (sel, first) => { sel.innerHTML = (first ? `<option value="">${first}</option>` : "") + CATS.map(c => `<option>${c}</option>`).join("") };
  opts($("#catf"), "Todas as categorias"); opts($("#tc"));

  const isCloud = u => /res\.cloudinary\.com/.test(u);
  const opt = (i, w = 1200) => {
    if (!isCloud(i.url)) return w <= 1000 && i.thumb ? i.thumb : (i.type === "video" ? (i.thumb || "") : i.url);
    return i.type === "video"
      ? i.url.replace("/upload/", `/upload/so_0,w_${w},c_limit,q_auto:good,f_jpg/`).replace(/\.\w+$/, ".jpg")
      : i.url.replace("/upload/", `/upload/f_auto,q_auto:${w >= 1800 ? "best" : "good"},w_${w},c_limit/`);
  };
  const fmt = d => d ? new Date(d + "T12:00").toLocaleDateString("pt-BR", { month: "long", year: "numeric" }) : "";

  let items = [], type = "all", cat = "";
  const save = () => st.set("dv2", JSON.stringify(items));

  function render() {
    const list = items.filter(i => (type === "all" || i.type === type) && (!cat || i.cat === cat));
    grid.replaceChildren();
    if (!list.length) { grid.innerHTML = `<div class="empty">${items.length ? "Nenhuma mídia nesta seleção ainda." : "Estamos atualizando o portfólio. Peça pelo WhatsApp exemplos de trabalhos recentes."}</div>`; return }
    list.forEach(i => {
      const f = document.createElement("figure"); f.className = "item"; f.tabIndex = 0;
      f.innerHTML = `<div class="ph"><img loading="lazy" decoding="async" alt=""><span class="pl" hidden></span></div><h3></h3><small></small>`;
      const im = f.querySelector("img"); im.src = opt(i, 800); im.alt = i.title || "Imagem aérea";
      f.querySelector(".pl").hidden = i.type !== "video";
      f.querySelector("h3").textContent = i.title || i.cat;
      f.querySelector("small").textContent = [i.cat, fmt(i.date)].filter(Boolean).join(" · ");
      const open = () => lightbox(i);
      f.addEventListener("click", open); f.addEventListener("keydown", e => e.key === "Enter" && open());
      grid.append(f);
    });
  }
  function lightbox(i) {
    const m = document.createElement(i.type === "video" ? "video" : "img");
    if (i.type === "video") { m.src = i.url; m.controls = true; m.autoplay = true; m.playsInline = true; m.muted = true }
    else { m.src = opt(i, 2400); m.alt = i.title || "" }
    $("#lbc").replaceChildren(m); $("#lbt").textContent = [i.title, i.cat].filter(Boolean).join(" · "); $("#lb").showModal();
  }
  $("#lbx").addEventListener("click", () => $("#lb").close());
  $("#lb").addEventListener("close", () => $("#lbc").replaceChildren());
  $("#lb").addEventListener("click", e => { if (e.target === $("#lb")) $("#lb").close() });
  document.querySelectorAll(".bar button").forEach(b => b.addEventListener("click", () => {
    type = b.dataset.f; document.querySelectorAll(".bar button").forEach(x => x.setAttribute("aria-pressed", x === b)); render();
  }));
  $("#catf").addEventListener("change", e => { cat = e.target.value; render() });

  async function fromCloud() {
    const out = [];
    for (const t of ["image", "video"]) {
      try {
        const r = await fetch(`https://res.cloudinary.com/${CFG.cloud}/${t}/list/${CFG.tag}.json`);
        if (!r.ok) continue;
        (await r.json()).resources.forEach(x => out.push({ type: t, url: `https://res.cloudinary.com/${CFG.cloud}/${t}/upload/v${x.version}/${x.public_id}.${x.format}`, title: "", cat: "Imagens aéreas", date: (x.created_at || "").slice(0, 10) }));
      } catch (e) {}
    }
    return out.sort((a, b) => b.date.localeCompare(a.date));
  }
  async function boot() {
    let local = []; try { local = JSON.parse(st.get("dv2") || "[]") } catch (e) {}
    if (local.length) items = local;
    else { try { const r = await fetch("/portfolio.json", { cache: "no-cache" }); if (r.ok) items = await r.json() } catch (e) {} }
    if (!items.length && CFG.cloud) items = await fromCloud();
    render(); drawList();
  }
  boot();

  /* ---------- painel admin ---------- */
  const panel = $("#panel"), msg = $("#msg");
  const sha = async s => [...new Uint8Array(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s)))].map(b => b.toString(16).padStart(2, "0")).join("");
  const show = on => { panel.classList.toggle("on", on); panel.setAttribute("aria-hidden", !on); if (on) $("#pw").focus() };
  document.querySelectorAll("[data-admin]").forEach(b => b.addEventListener("click", () => show(true)));
  $("#pc").addEventListener("click", () => show(false));
  if (location.hash === "#admin") show(true);
  addEventListener("hashchange", () => { if (location.hash === "#admin") show(true) });
  addEventListener("keydown", e => { if (e.key === "Escape") show(false) });
  $("#lock").addEventListener("submit", async e => {
    e.preventDefault(); const h = await sha($("#pw").value), lm = $("#lmsg");
    if (!CFG.passHash) lm.textContent = "Senha ainda não definida no site. Hash para colar em CFG.passHash (assets/js/portfolio.js): " + h;
    else if (h !== CFG.passHash) { lm.textContent = "Senha incorreta."; return }
    $("#lock").style.display = "none"; $("#app").style.display = "block";
  });
  $("#cn").value = CFG.cloud || st.get("dv_cloud") || ""; $("#up").value = CFG.preset || st.get("dv_preset") || "";
  function drawList() {
    const l = $("#list"); l.replaceChildren();
    if (!items.length) { l.innerHTML = '<p class="note">Nenhum item ainda.</p>'; return }
    items.forEach((i, n) => {
      const r = document.createElement("div"); r.className = "row";
      r.innerHTML = `<img alt=""><div class="f"><input aria-label="Título"><button class="btn btn-ghost sm" type="button">Excluir</button><select aria-label="Categoria"></select></div>`;
      r.querySelector("img").src = opt(i, 120);
      const inp = r.querySelector("input"), sel = r.querySelector("select"); opts(sel); sel.value = i.cat; inp.value = i.title || "";
      inp.addEventListener("change", () => { i.title = inp.value; save(); render() });
      sel.addEventListener("change", () => { i.cat = sel.value; save(); render() });
      r.querySelector("button").addEventListener("click", () => { items.splice(n, 1); save(); render(); drawList() });
      l.append(r);
    });
  }
  $("#send").addEventListener("click", () => {
    const cloud = $("#cn").value.trim(), preset = $("#up").value.trim();
    if (!cloud || !preset) { msg.textContent = "Preencha Cloud name e Upload preset."; return }
    if (!window.cloudinary) { msg.textContent = "O widget ainda está carregando. Tente de novo."; return }
    st.set("dv_cloud", cloud); st.set("dv_preset", preset);
    cloudinary.createUploadWidget({ cloudName: cloud, uploadPreset: preset, sources: ["local", "camera", "url"], multiple: true, resourceType: "auto", tags: [CFG.tag],
      clientAllowedFormats: ["jpg", "jpeg", "png", "webp", "mp4", "mov", "webm"], language: "pt" }, (err, res) => {
      if (err) { msg.textContent = "Falha no envio. Confira o Cloud name e se o preset é unsigned."; return }
      if (res && res.event === "success" && !items.some(x => x.url === res.info.secure_url)) {
        items.unshift({ type: res.info.resource_type === "video" ? "video" : "image", url: res.info.secure_url, title: $("#tt").value.trim(), cat: $("#tc").value, date: new Date().toISOString().slice(0, 10) });
        save(); render(); drawList(); msg.textContent = "Enviado e já exibido no portfólio (só neste navegador até exportar).";
      }
    }).open();
  });
  $("#addlk").addEventListener("click", () => {
    const u = $("#lk").value.trim();
    if (!/^https:\/\/res\.cloudinary\.com\/.+\/upload\//.test(u)) { msg.textContent = "Cole uma URL do Cloudinary (res.cloudinary.com/.../upload/...)."; return }
    if (items.some(x => x.url === u)) { msg.textContent = "Esse link já está na lista."; return }
    items.unshift({ type: /\/video\/upload\//.test(u) ? "video" : "image", url: u, title: $("#tt").value.trim(), cat: $("#tc").value, date: new Date().toISOString().slice(0, 10) });
    save(); render(); drawList(); $("#lk").value = ""; msg.textContent = "Adicionado ao portfólio.";
  });
  $("#exp").addEventListener("click", () => {
    const a = document.createElement("a"); a.href = URL.createObjectURL(new Blob([JSON.stringify(items, null, 2)], { type: "application/json" })); a.download = "portfolio.json"; a.click();
    msg.textContent = "Suba o portfolio.json para a raiz do repositório.";
  });
  $("#imp").addEventListener("change", async e => { try { items = JSON.parse(await e.target.files[0].text()); save(); render(); drawList(); msg.textContent = "Importado." } catch (x) { msg.textContent = "Arquivo inválido." } });
  $("#reset").addEventListener("click", () => { st.set("dv2", "[]"); items = []; boot(); msg.textContent = "Rascunho local descartado; carregando o portfolio.json do site." });
})();

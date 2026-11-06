/* Drone Vision — comportamento comum a todas as páginas */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const calm = matchMedia("(prefers-reduced-motion: reduce)").matches;
  document.documentElement.classList.add("js");

  $$("[data-year]").forEach(e => e.textContent = new Date().getFullYear());

  /* menu mobile */
  const btn = $(".menu-btn"), nav = $("#nav");
  if (btn && nav) {
    const set = on => { btn.setAttribute("aria-expanded", on); nav.classList.toggle("open", on) };
    btn.addEventListener("click", () => set(btn.getAttribute("aria-expanded") !== "true"));
    nav.addEventListener("click", e => { if (e.target.closest("a")) set(false) });
    addEventListener("keydown", e => { if (e.key === "Escape") set(false) });
  }

  /* revelação ao rolar */
  const rv = $$(".rv");
  if ("IntersectionObserver" in window && !calm) {
    const io = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target) }
    }), { rootMargin: "0px 0px -8% 0px", threshold: .08 });
    rv.forEach(e => io.observe(e));
  } else rv.forEach(e => e.classList.add("in"));

  /* brilho que segue o mouse nos cartões */
  $$(".card").forEach(c => c.addEventListener("pointermove", e => {
    const r = c.getBoundingClientRect();
    c.style.setProperty("--mx", (e.clientX - r.left) + "px");
    c.style.setProperty("--my", (e.clientY - r.top) + "px");
  }));

  /* visor: altitude oscilando e cronômetro de gravação */
  const altEl = $("#alt"), clk = $("#clk");
  if (altEl) {
    let alt = 120;
    setInterval(() => { alt = Math.max(96, Math.min(120, alt + Math.round((Math.random() - .5) * 4))); altEl.textContent = alt }, 1200);
  }
  if (clk) {
    const t0 = Date.now(), p = n => String(n).padStart(2, "0");
    setInterval(() => { const s = Math.floor((Date.now() - t0) / 1000); clk.textContent = `${p(Math.floor(s / 3600))}:${p(Math.floor(s / 60) % 60)}:${p(s % 60)}` }, 1000);
  }

  /* rota de voo desenhada conforme a rolagem */
  const route = $(".flight");
  if (route && !calm) {
    const trail = $(".trail", route), drone = $(".route-drone", route);
    if (trail) {
      const len = trail.getTotalLength();
      trail.style.strokeDasharray = len; trail.style.strokeDashoffset = len;
      const tick = () => {
        const r = route.getBoundingClientRect(), vh = innerHeight;
        const k = Math.min(1, Math.max(0, (vh * .85 - r.top) / (r.height + vh * .3)));
        trail.style.strokeDashoffset = len * (1 - k);
        if (drone) { const p = trail.getPointAtLength(len * k); drone.setAttribute("transform", `translate(${p.x - 18} ${p.y - 14})`) }
      };
      addEventListener("scroll", () => requestAnimationFrame(tick), { passive: true });
      addEventListener("resize", tick); tick();
    }
  }

  /* formulário de contato: monta a mensagem e abre o WhatsApp */
  const form = $("#wa-form");
  if (form) form.addEventListener("submit", e => {
    e.preventDefault();
    const f = new FormData(form), linhas = [
      "Olá, Drone Vision! Vim pelo site.",
      `Nome: ${f.get("nome")}`,
      `Serviço: ${f.get("servico")}`,
      f.get("local") ? `Local: ${f.get("local")}` : "",
      f.get("mensagem") ? `Mensagem: ${f.get("mensagem")}` : ""
    ].filter(Boolean);
    window.open(`https://wa.me/${form.dataset.wa}?text=${encodeURIComponent(linhas.join("\n"))}`, "_blank", "noopener");
  });

  /* mini drone que passeia pela tela e acompanha o cursor */
  const dr = $("#mini");
  if (dr) {
    if (calm) dr.style.display = "none";
    else {
      let x = innerWidth * .6, y = 140, mx = null, my = null;
      addEventListener("pointermove", e => { if (e.pointerType === "mouse") { mx = e.clientX; my = e.clientY } }, { passive: true });
      addEventListener("pointerleave", () => { mx = my = null });
      (function loop(t) {
        const w = innerWidth, h = innerHeight;
        let tx = w * (.5 + .38 * Math.sin(t / 5200)), ty = h * (.32 + .2 * Math.sin(t / 2600)) + 30 * Math.sin(t / 900);
        if (mx !== null) { tx = tx * .55 + (mx + 70) * .45; ty = ty * .55 + (my - 60) * .45 }
        const px = x; x += (tx - x) * .02; y += (ty - y) * .02;
        const vx = x - px;
        dr.style.transform = `translate(${x - 36}px,${y - 22 + 4 * Math.sin(t / 260)}px) rotate(${Math.max(-16, Math.min(16, vx * 5))}deg)`;
        requestAnimationFrame(loop);
      })(0);
    }
  }
})();

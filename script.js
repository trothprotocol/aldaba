(function () {
  "use strict";

  /* Reveal styles apply only once this file is running, so a script that
     never loads leaves every section plainly visible. */
  document.documentElement.classList.add("js");

  /* ======================================================================
     Language
     Both languages live in one document. Every translatable node carries
     data-en and data-es. English is primary.
     ====================================================================== */

  var LANGS = ["en", "es"];
  var KEY = "aldaba:lang";

  function storedLang() {
    var saved;
    try { saved = window.localStorage.getItem(KEY); } catch (e) { saved = null; }
    return LANGS.indexOf(saved) > -1 ? saved : "en";
  }

  function applyLang(lang) {
    document.documentElement.lang = lang;

    Array.prototype.forEach.call(
      document.querySelectorAll("[data-" + lang + "]"),
      function (el) {
        var value = el.getAttribute("data-" + lang);
        if (el.tagName === "TITLE") document.title = value;
        else if (el.tagName === "META") el.setAttribute("content", value);
        else el.innerHTML = value;
      }
    );

    Array.prototype.forEach.call(
      document.querySelectorAll("[data-" + lang + "-label]"),
      function (el) {
        el.setAttribute("aria-label", el.getAttribute("data-" + lang + "-label"));
      }
    );

    Array.prototype.forEach.call(
      document.querySelectorAll(".lang__opt"),
      function (btn) {
        btn.setAttribute("aria-pressed", String(btn.dataset.lang === lang));
      }
    );

    syncMenuLabels();

    try { window.localStorage.setItem(KEY, lang); } catch (e) {}
  }

  Array.prototype.forEach.call(
    document.querySelectorAll(".lang__opt"),
    function (btn) {
      btn.addEventListener("click", function () { applyLang(btn.dataset.lang); });
    }
  );

  /* ======================================================================
     Header state
     Turns solid only after the hero, so the full-bleed image is never
     clipped by a white bar.
     ====================================================================== */

  var header = document.getElementById("header");
  var hero = document.querySelector(".hero");

  /* Las páginas interiores no tienen portada: el encabezado ya es sólido. */
  if (header && hero) {
    var onScroll = function () {
      var threshold = hero.offsetHeight - header.offsetHeight - 8;
      header.classList.toggle("is-solid", window.scrollY > threshold);
      /* La frase bajo el logotipo se retira apenas la página se mueve. */
      header.classList.toggle("is-moved", window.scrollY > 24);
    };

    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll);
  }

  /* ======================================================================
     Menu
     ====================================================================== */

  var trigger = document.getElementById("menu-trigger");
  var closeBtn = document.getElementById("menu-close");
  var menu = document.getElementById("menu");
  var scrim = document.getElementById("scrim");

  var LABELS = {
    en: { open: "Open menu", close: "Close menu" },
    es: { open: "Abrir menú", close: "Cerrar menú" }
  };

  function syncMenuLabels() {
    if (!trigger || !closeBtn) return;
    var lang = document.documentElement.lang === "es" ? "es" : "en";
    trigger.setAttribute("aria-label", LABELS[lang].open);
    closeBtn.setAttribute("aria-label", LABELS[lang].close);
  }

  function setMenu(open) {
    document.body.classList.toggle("menu-open", open);
    trigger.setAttribute("aria-expanded", String(open));
    menu.setAttribute("aria-hidden", String(!open));
    document.body.style.overflow = open ? "hidden" : "";

    if (open) {
      window.setTimeout(function () { closeBtn.focus(); }, 60);
    } else {
      trigger.focus();
    }
  }

  /* El menú solo existe en la portada */
  if (trigger && closeBtn && menu && scrim) {
    trigger.addEventListener("click", function () { setMenu(true); });
    closeBtn.addEventListener("click", function () { setMenu(false); });

    /* The dimmed sliver closes the menu */
    scrim.addEventListener("click", function () { setMenu(false); });

    /* Following a link closes it too */
    menu.addEventListener("click", function (event) {
      if (event.target.closest(".lang")) return;
      if (event.target.closest(".menu__lang")) return;
      if (event.target.closest("a")) setMenu(false);
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && document.body.classList.contains("menu-open")) {
        setMenu(false);
      }
    });

    /* Keep focus inside the menu while it is open */
    menu.addEventListener("keydown", function (event) {
      if (event.key !== "Tab") return;
      var focusable = menu.querySelectorAll("a[href], button");
      if (!focusable.length) return;
      var first = focusable[0];
      var last = focusable[focusable.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    });
  }

  /* ======================================================================
     Enquiry form
     No backend yet. The form composes a WhatsApp message so nothing is
     silently lost. Replace WHATSAPP with the real number before launch.
     ====================================================================== */

  var WHATSAPP = "50200000000"; // TODO: número real

  var FIELDS = {
    enquiry: [
      ["name", "Name", "Nombre"],
      ["email", "Email", "Correo"],
      ["dates", "Dates", "Fechas"],
      ["guests", "Guests", "Huéspedes"]
    ],
    "house-enquiry": [
      ["house", "House", "Casa"],
      ["name", "Name", "Nombre"],
      ["email", "Email", "Correo"],
      ["dates", "Dates", "Fechas"],
      ["guests", "Guests", "Huéspedes"],
      ["budget", "Budget", "Presupuesto"]
    ],
    "owner-enquiry": [
      ["name", "Name", "Nombre"],
      ["phone", "Phone", "Teléfono"],
      ["email", "Email", "Correo"],
      ["place", "Where the house is", "Dónde está la casa"],
      ["listing", "Listing", "Anuncio"]
    ]
  };

  Object.keys(FIELDS).forEach(function (id) {
    var form = document.getElementById(id);
    if (!form) return;

    form.addEventListener("submit", function (event) {
      event.preventDefault();

      var data = new FormData(form);
      var es = document.documentElement.lang === "es";
      var owner = id === "owner-enquiry";

      var lines = [
        owner
          ? "Solicitud de análisis desde aldaba.gt"
          : (es ? "Consulta desde aldaba.gt" : "Enquiry from aldaba.gt"),
        ""
      ];

      FIELDS[id].forEach(function (field) {
        lines.push((es || owner ? field[2] : field[1]) + ": " + (data.get(field[0]) || "-"));
      });

      var message = data.get("message");
      if (message) lines.push("", message);

      window.open(
        "https://wa.me/" + WHATSAPP + "?text=" + encodeURIComponent(lines.join("\n")),
        "_blank",
        "noopener"
      );
    });
  });

  /* ======================================================================
     Programmes
     Three ways to spend the same week. One panel at a time; arrow keys move
     between the tabs the way a native tablist does.
     ====================================================================== */

  Array.prototype.forEach.call(
    document.querySelectorAll("[data-prog]"),
    function (group) {
      var tabs = group.querySelectorAll(".prog__tab");
      var panels = group.querySelectorAll(".prog__panel");
      if (!tabs.length) return;

      function select(index) {
        Array.prototype.forEach.call(tabs, function (tab, i) {
          var on = i === index;
          tab.setAttribute("aria-selected", String(on));
          tab.tabIndex = on ? 0 : -1;
          panels[i].hidden = !on;
        });
      }

      Array.prototype.forEach.call(tabs, function (tab, i) {
        tab.addEventListener("click", function () { select(i); });
        tab.addEventListener("keydown", function (event) {
          var next = null;
          if (event.key === "ArrowRight") next = (i + 1) % tabs.length;
          if (event.key === "ArrowLeft") next = (i - 1 + tabs.length) % tabs.length;
          if (next === null) return;
          event.preventDefault();
          select(next);
          tabs[next].focus();
        });
      });

      select(0);
    }
  );

  /* ======================================================================
     Arrival
     Sections rise once, the first time they are seen.
     ====================================================================== */

  var reveals = document.querySelectorAll(".reveal");

  if (!window.IntersectionObserver ||
      window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    Array.prototype.forEach.call(reveals, function (el) { el.classList.add("is-in"); });
  } else {
    var seen = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-in");
        seen.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -12% 0px", threshold: 0.05 });

    Array.prototype.forEach.call(reveals, function (el) { seen.observe(el); });

    /* Belt and braces: if the observer never fires, because the tab was
       restored in the background or the page was never scrolled, nothing
       stays invisible. */
    window.setTimeout(function () {
      Array.prototype.forEach.call(reveals, function (el) { el.classList.add("is-in"); });
    }, 3000);
  }

  /* Start.
     Solo las páginas bilingües cambian de idioma. Las páginas de un solo
     idioma, como la de propietarios, conservan el lang del documento. */
  if (document.querySelector("[data-en]")) {
    applyLang(storedLang());
  } else {
    syncMenuLabels();
  }
})();

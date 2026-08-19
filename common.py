"""
Shared pieces for the generated pages.

The houses and destinations are defined once, in build-houses.py and
build-destinations.py. Everything that has to list them, the footer above all,
reads them from here so a new house appears everywhere at once.
"""

import html
import importlib.util
import os

ROOT = os.path.dirname(os.path.abspath(__file__))


def _load(filename, attr):
    spec = importlib.util.spec_from_file_location(filename.replace("-", "_"),
                                                  os.path.join(ROOT, filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, attr)


def houses():
    return _load("build-houses.py", "HOUSES")


def destinations():
    return _load("build-destinations.py", "DESTINATIONS")


def house_name(h):
    return h["name"] + (" (test)" if h.get("test") else "")


def t(en, es):
    return 'data-en="{}" data-es="{}">{}'.format(
        html.escape(en, quote=True), html.escape(es, quote=True), html.escape(en)
    )


def footer_html(prefix=""):
    """The footer carries the whole collection, the way aman.com does."""
    house_links = "\n".join(
        '            <li><a href="{p}houses/{slug}.html">{name}</a></li>'.format(
            p=prefix, slug=h["slug"], name=html.escape(house_name(h))
        )
        for h in houses()
    )

    dest_links = "\n".join(
        '            <li><a href="{p}destinations/{slug}.html" {label}</a></li>'.format(
            p=prefix, slug=d["slug"], label=t(d["name_en"], d["name_es"])
        )
        for d in destinations()
    )

    return '''  <!-- footer:start -->
  <footer class="footer">
    <div class="wrap">

      <div class="footer__cols">
        <div class="footer__col">
          <p class="eyebrow footer__head" {houses_head}</p>
          <ul class="footer__list">
{house_links}
          </ul>
        </div>

        <div class="footer__col">
          <p class="eyebrow footer__head" {dest_head}</p>
          <ul class="footer__list">
{dest_links}
          </ul>
        </div>

        <div class="footer__col">
          <p class="eyebrow footer__head" {ald_head}</p>
          <ul class="footer__list">
            <li><a href="{p}about.html" {about}</a></li>
            <li><a href="{p}journal/acatenango.html" {journal}</a></li>
            <li><a href="{p}index.html#concierge" {concierge}</a></li>
            <li><a href="{p}index.html#contact" {contact}</a></li>
            <li><a href="{p}propietarios.html" rel="nofollow" {owners}</a></li>
          </ul>
        </div>
      </div>

      <div class="footer__bar">
        <p class="footer__mark"><img class="wordmark__img" src="{p}img/brand/wordmark-ink.png" alt="" aria-hidden="true"><span class="sr-only">Aldaba</span></p>
        <p class="footer__tag">Well received.</p>
        <p class="footer__fine" {fine}</p>
      </div>

    </div>
  </footer>
  <!-- footer:end -->
'''.format(
        p=prefix,
        house_links=house_links,
        dest_links=dest_links,
        houses_head=t("Houses", "Casas"),
        dest_head=t("Destinations", "Destinos"),
        ald_head=t("Aldaba", "Aldaba"),
        about=t("About us", "Quiénes somos"),
        journal=t("Journal", "Diario"),
        concierge=t("Concierge", "Concierge"),
        contact=t("Contact us", "Contáctenos"),
        owners=t("Property owners", "Propietarios"),
        fine=t("Houses in Guatemala.", "Casas en Guatemala."),
    )

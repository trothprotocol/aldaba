#!/usr/bin/env python3
"""
Aldaba | about

One page, generated so it carries the same shell and footer as everything
else. Guest-facing: what Aldaba is, who stands behind it, and nothing about
commissions or how the business is run.
"""

import os
import common
from common import t

ROOT = os.path.dirname(os.path.abspath(__file__))

PAGE = {
    "title_en": "Aldaba | About us",
    "title_es": "Aldaba | Quiénes somos",
    "desc_en": "A small collection of houses in Guatemala, kept and hosted by the people who know the country best.",

    "head_en": "We keep a small number of houses, and we answer for all of them.",
    "head_es": "Cuidamos unas pocas casas, y respondemos por todas.",

    "lead_en": "Aldaba is a Guatemalan company. We take on houses one at a time, hold every one of them to the same standard, and stay on the end of the telephone for the whole of your stay.",
    "lead_es": "Aldaba es una empresa guatemalteca. Tomamos las casas de una en una, sostenemos todas al mismo estándar, y nos quedamos al otro lado del teléfono durante toda su estadía.",

    "body_en": [
        "The name is the iron knocker on a colonial door, the one you lift to say you have arrived. Everything we do sits behind that idea: somebody is expecting you, the door is open, and the house is ready before you reach it.",
        "We are not a listings site and we are not an agency. Every house in the collection is one we operate, with a team we have trained and a standard we verify before each arrival. If a house cannot hold that standard, it leaves the collection.",
    ],
    "body_es": [
        "El nombre es la aldaba de hierro en una puerta colonial, la que uno levanta para anunciar que llegó. Todo lo que hacemos vive detrás de esa idea: alguien lo espera, la puerta está abierta, y la casa está lista antes de que usted llegue.",
        "No somos un portal de anuncios ni una agencia. Cada casa de la colección la operamos nosotros, con un equipo que formamos y un estándar que verificamos antes de cada llegada. Si una casa no puede sostener ese estándar, sale de la colección.",
    ],

    "points_en": [
        ("Few houses", "We would rather have four houses we can answer for than forty we cannot."),
        ("One standard", "Twelve things are checked in every house before every arrival. The list does not bend for a busy week."),
        ("People from here", "The teams are local, the guides are local, and the person who answers the telephone at two in the morning is in Guatemala."),
        ("One number", "For the drive from the airport, the table you forgot to book, and everything after that."),
    ],
    "points_es": [
        ("Pocas casas", "Preferimos cuatro casas por las que podemos responder que cuarenta por las que no."),
        ("Un solo estándar", "Doce cosas se revisan en cada casa antes de cada llegada. La lista no se dobla por una semana llena."),
        ("Gente de aquí", "Los equipos son de aquí, los guías son de aquí, y quien contesta el teléfono a las dos de la mañana está en Guatemala."),
        ("Un número", "Para el viaje desde el aeropuerto, la mesa que se le olvidó reservar, y todo lo que venga después."),
    ],

    "partners_en": "We work with Carma Group, whose companies have moved travellers through this country for decades: Hertz Guatemala, Maya Trails and Trip18. The cars, the drivers and the days out are theirs, which is why we can promise them rather than recommend them.",
    "partners_es": "Trabajamos con Carma Group, cuyas empresas llevan décadas moviendo viajeros por este país: Hertz Guatemala, Maya Trails y Trip18. Los carros, los choferes y los días de paseo son de ellos, y por eso los podemos prometer en lugar de recomendarlos.",
}


def build():
    p = PAGE
    page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title {t(p['title_en'], p['title_es'])}</title>
  <meta name="description" content="{p['desc_en']}">
  <link rel="stylesheet" href="styles.css">
</head>
<body>

  <a class="skip" href="#content" {t("Skip to content", "Saltar al contenido")}</a>

  <header class="header is-solid" id="header">
    <div class="wrap header__bar">
      <a class="menu-trigger" href="index.html"
         data-en-label="Back to home" data-es-label="Volver al inicio" aria-label="Back to home">
        <span class="menu-trigger__word">&larr; Aldaba</span>
      </a>
      <a class="wordmark" href="index.html"
         data-en-label="Aldaba, home" data-es-label="Aldaba, inicio"
         aria-label="Aldaba, home"><span class="wordmark__pair"><img class="wordmark__img wordmark__img--light" src="img/brand/wordmark-light.png" alt="" aria-hidden="true"><img class="wordmark__img wordmark__img--ink" src="img/brand/wordmark-ink.png" alt="" aria-hidden="true"></span></a>
      <div class="header__right">
        <div class="lang" role="group"
             data-en-label="Language" data-es-label="Idioma" aria-label="Language">
          <button class="lang__opt" type="button" data-lang="en" aria-pressed="true">EN</button>
          <button class="lang__opt" type="button" data-lang="es" aria-pressed="false">ES</button>
        </div>
        <a class="reserve" href="index.html#contact" {t("Contact us", "Contáctenos")}</a>
      </div>
    </div>
  </header>

  <main id="content">

    <section class="wrap page-head reveal">
      <p class="eyebrow page-head__eyebrow" {t("About us", "Quiénes somos")}</p>
      <h1 class="page-head__title" {t(p['head_en'], p['head_es'])}</h1>
      <p class="page-head__lead" {t(p['lead_en'], p['lead_es'])}</p>
    </section>

    <section class="section reveal">
      <div class="wrap">
        <p class="section__lead" {t(p['body_en'][0], p['body_es'][0])}</p>
        <p class="section__lead" {t(p['body_en'][1], p['body_es'][1])}</p>
      </div>
    </section>

    <section class="section section--alt reveal">
      <div class="wrap">
        <p class="eyebrow section__eyebrow" {t("How we work", "Cómo trabajamos")}</p>
        <h2 class="section__title" {t("Four rules we do not bend.", "Cuatro reglas que no doblamos.")}</h2>

        <ul class="grid">
{chr(10).join('          <li class="grid__item"><h3 class="grid__title" ' + t(en[0], es[0]) + '</h3><p class="grid__text" ' + t(en[1], es[1]) + '</p></li>' for en, es in zip(p['points_en'], p['points_es']))}
        </ul>
      </div>
    </section>

    <section class="section reveal">
      <div class="wrap">
        <p class="eyebrow section__eyebrow" {t("Operated with", "Operado con")}</p>
        <h2 class="section__title" {t("Sixty years of moving travellers through this country.", "Sesenta años moviendo viajeros por este país.")}</h2>
        <p class="section__lead" {t(p['partners_en'], p['partners_es'])}</p>

        <div class="operated">
          <ul class="operated__names">
            <li class="operated__name"><img class="logo" src="img/logos/carma-group.webp" alt="Carma Group" width="794" height="208" loading="lazy"></li>
            <li class="operated__name"><img class="logo" src="img/logos/hertz.webp" alt="Hertz Guatemala" width="761" height="267" loading="lazy"></li>
            <li class="operated__name"><img class="logo" src="img/logos/maya-trails.webp" alt="Maya Trails" width="794" height="140" loading="lazy"></li>
            <li class="operated__name"><img class="logo logo--tall" src="img/logos/trip18.webp" alt="Trip18" width="1200" height="1107" loading="lazy"></li>
          </ul>
        </div>

        <p class="page-head__cta">
          <a class="btn-solid" href="index.html#contact" {t("Tell us when you are coming", "Díganos cuándo viene")}</a>
        </p>
      </div>
    </section>

  </main>

{common.footer_html("")}
  <script src="script.js"></script>
</body>
</html>
"""
    with open(os.path.join(ROOT, "about.html"), "w", encoding="utf-8") as fh:
        fh.write(page)
    print("wrote about.html")


if __name__ == "__main__":
    build()

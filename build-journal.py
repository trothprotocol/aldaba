#!/usr/bin/env python3
"""
Aldaba | journal

Short pieces about the country, each one ending where it should: the days we
arrange around it, and the houses it suits. Source of truth for journal/*.html.

    python3 build-journal.py
"""

import os
import html

import common
from common import t

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "journal")

POSTS = [
    {
        "slug": "acatenango",
        "cat_en": "On foot", "cat_es": "A pie",
        "title_en": "The hour before the volcano wakes",
        "title_es": "La hora antes de que despierte el volcán",
        "lead_en": "Why the walk starts in the dark, and what the light does to the ridge at ten past five.",
        "lead_es": "Por qué la caminata empieza a oscuras, y lo que hace la luz sobre la cresta a las cinco y diez.",
        "image": "img/hero-fuego-poster.jpg",
        "image_pos": "center 45%",
        "alt_en": "A walker on the ridge with Fuego erupting behind",
        "alt_es": "Un caminante en la cresta con el Fuego haciendo erupción detrás",

        "body_en": [
            "It begins at a gate above La Soledad, in a field of maize, at an hour that feels far too civilised for what follows. The first two hours are the hardest, straight up through farmland with no view to distract you. Then the forest closes over, the air cools, and the ground turns to volcanic sand that gives back half of every step.",
            "Camp is at three thousand six hundred metres, on the shoulder facing Fuego. This is the reason people come. Every twenty minutes or so the mountain across the saddle clears its throat, and after dark you stop talking mid-sentence to watch it throw orange up into the cloud. Nobody sleeps much, and nobody minds.",
            "At four you climb the last four hundred metres in the dark, in single file, in the cold, wondering why. At ten past five the sun comes up somewhere over Honduras and the entire chain of volcanoes lays itself out below you in silhouette, and the question answers itself.",
            "What we change is everything either side of that. Your own guide, not a group of eighteen. The camp already standing when you arrive, with tents that keep the wind out and a bag rated for the temperature it actually is up there. Somebody else carrying the water. And at the end of it, a car at the trailhead, a house with the fire already lit, and a bath deep enough to matter.",
        ],
        "body_es": [
            "Empieza en un portón arriba de La Soledad, en una milpa, a una hora que se siente demasiado civilizada para lo que viene. Las primeras dos horas son las más duras, directo hacia arriba entre terrenos de siembra y sin vista que lo distraiga. Después se cierra el bosque, el aire enfría, y el suelo se vuelve arena volcánica que devuelve la mitad de cada paso.",
            "El campamento está a tres mil seiscientos metros, en el hombro que ve al Fuego. Esa es la razón por la que la gente sube. Cada veinte minutos el volcán de enfrente se aclara la garganta, y ya de noche uno deja las frases a medias para verlo tirar naranja contra la nube. Nadie duerme mucho, y a nadie le importa.",
            "A las cuatro se suben los últimos cuatrocientos metros a oscuras, en fila, con frío, preguntándose por qué. A las cinco y diez el sol sale por algún lugar sobre Honduras y toda la cadena de volcanes se tiende abajo en silueta, y la pregunta se contesta sola.",
            "Lo que nosotros cambiamos es todo lo que rodea eso. Un guía suyo, no un grupo de dieciocho. El campamento ya montado al llegar, con carpas que detienen el viento y bolsas para la temperatura que de verdad hace allá arriba. Alguien más cargando el agua. Y al final, un carro en el camino, una casa con el fuego ya encendido, y una tina lo bastante honda para que cuente.",
        ],

        "arrange_en": [
            ("The guide", "One guide for your group and nobody else's, who has walked this mountain since he was a boy."),
            ("The camp", "Standing before you reach it, on the shoulder facing Fuego, with dinner cooked at altitude and coffee at four."),
            ("Both ends", "A driver to the trailhead and back, and a house waiting with the fire lit and the bath run."),
        ],
        "arrange_es": [
            ("El guía", "Un guía para su grupo y para nadie más, que camina este cerro desde niño."),
            ("El campamento", "Montado antes de que usted llegue, en el hombro que ve al Fuego, con cena a esa altura y café a las cuatro."),
            ("Los dos extremos", "Un chofer al camino y de regreso, y una casa esperando con el fuego encendido y la tina lista."),
        ],

        "note_en": "It is 3,976 metres, cold enough at camp to see your breath, and roughly ten hours of walking across two days. It is not technical and it is not gentle. December to April is driest.",
        "note_es": "Son 3,976 metros, frío suficiente en el campamento para ver el aliento, y unas diez horas de caminata en dos días. No es técnico y no es suave. De diciembre a abril es lo más seco.",

        "houses": ["ja", "tinamit"],
        "houses_note_en": "Antigua for the night before, because the trailhead is twenty minutes from the door. The city for the night after, because the flight home is always early.",
        "houses_note_es": "Antigua para la noche anterior, porque el inicio del camino está a veinte minutos de la puerta. La capital para la noche siguiente, porque el vuelo de regreso siempre es temprano.",
    },
]


def head(post):
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title {t("Aldaba | " + post['title_en'], "Aldaba | " + post['title_es'])}</title>
  <meta name="description" content="{html.escape(post['lead_en'], quote=True)}">
  <link rel="stylesheet" href="../styles.css">
</head>
<body>

  <a class="skip" href="#content" {t("Skip to content", "Saltar al contenido")}</a>

  <header class="header" id="header">
    <div class="wrap header__bar">
      <a class="menu-trigger" href="../index.html"
         data-en-label="Back to home" data-es-label="Volver al inicio" aria-label="Back to home">
        <span class="menu-trigger__word">&larr; Aldaba</span>
      </a>
      <a class="wordmark" href="../index.html"
         data-en-label="Aldaba, home" data-es-label="Aldaba, inicio"
         aria-label="Aldaba, home"><span class="wordmark__pair"><img class="wordmark__img wordmark__img--light" src="../img/brand/wordmark-light.png" alt="" aria-hidden="true"><img class="wordmark__img wordmark__img--ink" src="../img/brand/wordmark-ink.png" alt="" aria-hidden="true"></span></a>
      <div class="header__right">
        <div class="lang" role="group"
             data-en-label="Language" data-es-label="Idioma" aria-label="Language">
          <button class="lang__opt" type="button" data-lang="en" aria-pressed="true">EN</button>
          <button class="lang__opt" type="button" data-lang="es" aria-pressed="false">ES</button>
        </div>
        <a class="reserve" href="../index.html#contact" {t("Enquire", "Consultar")}</a>
      </div>
    </div>
  </header>

  <main id="content">

    <section class="hero hero--page">
      <div class="hero__media" style="background-image:linear-gradient(180deg, rgba(0,0,0,0.38) 0%, rgba(0,0,0,0.12) 40%, rgba(0,0,0,0.72) 100%), url('../{post['image']}'); background-position:center, {post['image_pos']};" role="img"
           data-en-label="{html.escape(post['alt_en'], quote=True)}" data-es-label="{html.escape(post['alt_es'], quote=True)}" aria-label="{html.escape(post['alt_en'], quote=True)}"></div>

      <div class="wrap hero__body">
        <article class="feature">
          <p class="eyebrow feature__eyebrow" {t(post['cat_en'], post['cat_es'])}</p>
          <h1 class="feature__title" {t(post['title_en'], post['title_es'])}</h1>
          <p class="feature__text" {t(post['lead_en'], post['lead_es'])}</p>
        </article>
      </div>
    </section>
"""


def article(post):
    paras = "\n".join(
        '        <p class="prose__p" {}</p>'.format(t(en, es))
        for en, es in zip(post["body_en"], post["body_es"])
    )
    return f"""
    <section class="section reveal">
      <div class="wrap prose">
{paras}

        <p class="prose__note" {t(post['note_en'], post['note_es'])}</p>
      </div>
    </section>
"""


def arrange(post):
    items = "\n".join(
        '          <li class="grid__item">\n'
        '            <h3 class="grid__title" {title}</h3>\n'
        '            <p class="grid__text" {text}</p>\n'
        "          </li>".format(title=t(en[0], es[0]), text=t(en[1], es[1]))
        for en, es in zip(post["arrange_en"], post["arrange_es"])
    )
    return """
    <section class="section section--alt reveal">
      <div class="wrap">
        <p class="eyebrow section__eyebrow" {eyebrow}</p>
        <h2 class="section__title" {title}</h2>

        <ul class="grid grid--three">
{items}
        </ul>
      </div>
    </section>
""".format(
        eyebrow=t("What we arrange", "Lo que arreglamos"),
        title=t("The mountain is the same. The week around it is not.",
                "El cerro es el mismo. La semana alrededor no."),
        items=items,
    )


def houses(post):
    listed = [h for h in common.houses() if h["slug"] in post["houses"]]
    cards = "\n".join(
        '''          <li class="card">
            <a class="card__link" href="../houses/{slug}.html">
              <div class="card__media" style="background-image:url('../{img}'); background-position:center 55%;" aria-hidden="true"></div>
              <p class="eyebrow card__cat" {place}</p>
              <h3 class="card__title">{name}</h3>
              <p class="card__more" {more}</p>
            </a>
          </li>'''.format(
            slug=h["slug"], img=h["image"], name=html.escape(common.house_name(h)),
            place=t(h["place_en"], h["place_es"]),
            more=t("See the house", "Ver la casa"),
        )
        for h in listed
    )
    return """
    <section class="section reveal">
      <div class="wrap">
        <p class="eyebrow section__eyebrow" {eyebrow}</p>
        <h2 class="section__title" {title}</h2>
        <p class="section__lead" {note}</p>

        <ul class="journal journal--pair">
{cards}
        </ul>

        <p class="page-head__cta">
          <a class="btn-solid" href="../index.html#contact" {cta}</a>
        </p>
      </div>
    </section>

  </main>
""".format(
        eyebrow=t("Where to sleep", "Dónde dormir"),
        title=t("The houses this walk fits into.", "Las casas en las que cabe esta caminata."),
        note=t(post["houses_note_en"], post["houses_note_es"]),
        cards=cards,
        cta=t("Tell us when you are coming", "Díganos cuándo viene"),
    )


def build():
    os.makedirs(OUT, exist_ok=True)
    for post in POSTS:
        page = head(post) + article(post) + arrange(post) + houses(post) \
            + common.footer_html("../") + """
  <script src="../script.js"></script>
</body>
</html>
"""
        path = os.path.join(OUT, post["slug"] + ".html")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(page)
        print("wrote", os.path.relpath(path, ROOT))


if __name__ == "__main__":
    build()

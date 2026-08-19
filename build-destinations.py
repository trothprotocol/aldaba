#!/usr/bin/env python3
"""
Aldaba | destination pages

Source of truth for destinations/*.html. Edit this file, then run:

    python3 build-destinations.py

Voice rules, from the project notes: the guest side evokes and never explains
the service, never quotes figures, never sells management. Short declaratives.
Both languages live in one document (data-en / data-es), English primary.
"""

import os
import html

import common

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "destinations")

DESTINATIONS = [
    {
        "slug": "antigua",
        "image": "img/antigua-arch.jpg",
        "image_pos": "center 62%",
        "alt_en": "The Santa Catalina arch with Agua behind it at dawn",
        "alt_es": "El arco de Santa Catalina con el Agua detrás al amanecer",
        "eyebrow_en": "Guatemala", "eyebrow_es": "Guatemala",
        "name_en": "Antigua", "name_es": "Antigua",
        "title_en": "A city that keeps its own hours.",
        "title_es": "Una ciudad que lleva sus propias horas.",
        "lead_en": "Cobbled, low, and held between three volcanoes. Best understood before eight in the morning.",
        "lead_es": "Empedrada, baja, sostenida entre tres volcanes. Se entiende mejor antes de las ocho de la mañana.",
        "body_en": [
            "Antigua is small enough to cross on foot in twenty minutes and old enough that the crossing takes an hour. Doors open onto courtyards you were not expecting. Bells carry. In the late afternoon the light comes down the slope of Agua and lands on the ruins, and the people who live here stop for it.",
            "It is a working coffee region as much as a colonial one. Fincas on the hillsides, a Semana Santa that lays sawdust carpets down every street, and the road to Acatenango leaving from the edge of town. Most people come for three nights and wish they had taken five.",
        ],
        "body_es": [
            "Antigua es lo bastante pequeña para cruzarla a pie en veinte minutos y lo bastante antigua para que el cruce tome una hora. Las puertas abren a patios que uno no esperaba. Las campanas se oyen de lejos. Por la tarde la luz baja por la ladera del Agua y cae sobre las ruinas, y quien vive aquí se detiene a mirarla.",
            "Es una región cafetalera tanto como colonial. Fincas en las laderas, una Semana Santa que tiende alfombras de aserrín por cada calle, y el camino al Acatenango saliendo de la orilla del pueblo. Casi todos vienen tres noches y desearían haber tomado cinco.",
        ],
        "days_en": [
            ("Before the city wakes", "The half hour when the streets belong to the bread vans and the light is still coming in sideways."),
            ("A morning on the slope", "A family that has grown the same hillside for four generations, and coffee drunk about nine metres from where it was picked."),
            ("The ridge", "Acatenango, walked slowly, with the camp already standing when you arrive and Fuego across the saddle after dark."),
            ("The table", "A long dinner in a courtyard, cooked where you are sitting, running later than anybody planned."),
        ],
        "days_es": [
            ("Antes de que despierte la ciudad", "La media hora en que las calles son de las panaderías y la luz todavía entra de lado."),
            ("Una mañana en la ladera", "Una familia que ha cultivado la misma ladera durante cuatro generaciones, y café tomado a nueve metros de donde se cortó."),
            ("La cresta", "El Acatenango, caminado sin prisa, con el campamento ya montado al llegar y el Fuego enfrente cuando cae la noche."),
            ("La mesa", "Una cena larga en un patio, cocinada donde uno está sentado, que termina más tarde de lo que nadie tenía previsto."),
        ],
        "facts_en": [
            ("Getting here", "About fifty minutes from the airport in Guatemala City."),
            ("Best months", "November to April. Dry, clear, and cold enough at night to want the fireplace."),
            ("One week to know about", "Semana Santa, the week before Easter. The most beautiful and the most crowded the city gets."),
        ],
        "facts_es": [
            ("Cómo se llega", "Unos cincuenta minutos desde el aeropuerto de la Ciudad de Guatemala."),
            ("Mejores meses", "De noviembre a abril. Seco, despejado y con noches lo bastante frías para querer chimenea."),
            ("Una semana que conviene saber", "Semana Santa. La más hermosa y la más llena del año."),
        ],
    },
    {
        "slug": "atitlan",
        "image": "img/lake.jpg",
        "image_pos": "center 52%",
        "alt_en": "Lake Atitlán with its volcanoes at dawn",
        "alt_es": "El lago de Atitlán y sus volcanes al amanecer",
        "eyebrow_en": "Guatemala", "eyebrow_es": "Guatemala",
        "name_en": "Lake Atitlán", "name_es": "Lago de Atitlán",
        "title_en": "Three volcanoes, and water that changes by the hour.",
        "title_es": "Tres volcanes, y un agua que cambia a cada hora.",
        "lead_en": "Mornings are still. Afternoons are not. Everything worth doing here is arranged around that one fact.",
        "lead_es": "Las mañanas son quietas. Las tardes no. Todo lo que vale la pena aquí se organiza alrededor de ese solo hecho.",
        "body_en": [
            "There is no road that matters. The villages sit around the shore and you move between them by boat, which changes how a day feels before it has begun. Santiago is not San Marcos and neither is Santa Catarina; the languages change, the weaving changes, the hour people eat changes.",
            "Around one in the afternoon the xocomil comes down off the ridges and the lake turns. Locals plan their crossings before it and their afternoons after it. So do we.",
        ],
        "body_es": [
            "No hay carretera que importe. Los pueblos se sientan alrededor de la orilla y uno se mueve entre ellos en lancha, lo que cambia el día antes de que empiece. Santiago no es San Marcos, y Santa Catarina tampoco; cambia el idioma, cambia el tejido, cambia la hora a la que se come.",
            "Cerca de la una de la tarde baja el xocomil desde las crestas y el lago se voltea. Aquí la gente cruza antes de esa hora y descansa después. Nosotros también.",
        ],
        "days_en": [
            ("The crossing at dawn", "Glass water, the volcanoes still grey, and a boat that leaves when you are ready rather than when it fills."),
            ("Santiago", "A town that has kept its own language and its own saint, seen with somebody who is from there."),
            ("The water before noon", "Kayaks, a swim off the rocks, and back on the terrace by the time the wind arrives."),
            ("Dusk", "A temazcal heated on the shore, and dinner cooked by a family who have fed people on this lake for a long time."),
        ],
        "days_es": [
            ("El cruce al amanecer", "El agua como un vidrio, los volcanes todavía grises, y una lancha que sale cuando usted está listo y no cuando se llena."),
            ("Santiago", "Un pueblo que ha conservado su idioma y su santo, visto con alguien de allí."),
            ("El agua antes del mediodía", "Kayaks, un clavado desde las piedras, y de vuelta en la terraza antes de que llegue el viento."),
            ("El atardecer", "Un temazcal calentado en la orilla, y una cena hecha por una familia que lleva mucho tiempo dando de comer en este lago."),
        ],
        "facts_en": [
            ("Getting here", "About three hours from Guatemala City, or an hour and a half from Antigua."),
            ("Best months", "November to March, when the mornings are clearest."),
            ("How the day runs", "Arrive at the lake before noon. The afternoon wind decides the rest."),
        ],
        "facts_es": [
            ("Cómo se llega", "Unas tres horas desde la Ciudad de Guatemala, o hora y media desde Antigua."),
            ("Mejores meses", "De noviembre a marzo, cuando las mañanas son más limpias."),
            ("Cómo corre el día", "Llegar al lago antes del mediodía. El viento de la tarde decide lo demás."),
        ],
    },
    {
        "slug": "rio-dulce",
        "image": "img/rio-dulce.jpg",
        "image_pos": "center 55%",
        "alt_en": "The river opening out towards the Caribbean",
        "alt_es": "El río abriéndose hacia el Caribe",
        "eyebrow_en": "Guatemala", "eyebrow_es": "Guatemala",
        "name_en": "Río Dulce", "name_es": "Río Dulce",
        "title_en": "A river that runs to the Caribbean.",
        "title_es": "Un río que va a dar al Caribe.",
        "lead_en": "Green water, a gorge with herons standing in it, and a town at the far end where the country stops speaking Spanish.",
        "lead_es": "Agua verde, un cañón con garzas paradas adentro, y un pueblo al final donde el país deja de hablar español.",
        "body_en": [
            "The river leaves the lake and cuts through a limestone gorge for half a day, walls two hundred feet up on both sides with vines coming down them. Boats are the road. Houses stand on stilts at the edge of the water and nobody is in a hurry about anything.",
            "At the mouth is Livingston, Garífuna, reachable only by water, with its own language, its own drums and its own way of cooking fish in coconut. It does not feel like the rest of the country because it is not.",
        ],
        "body_es": [
            "El río sale del lago y corta un cañón de caliza durante media jornada, con paredes de sesenta metros a los dos lados y bejucos cayendo por ellas. Las lanchas son la carretera. Las casas se paran sobre pilotes al filo del agua y nadie tiene prisa por nada.",
            "En la desembocadura está Livingston, garífuna, a la que solo se llega por agua, con su idioma, sus tambores y su manera de cocinar el pescado en coco. No se siente como el resto del país porque no lo es.",
        ],
        "days_en": [
            ("Down the gorge", "Two hours of walls, herons and cormorants, with the engine off for the part that deserves it."),
            ("Livingston", "Lunch that takes the afternoon, in a town you can only arrive at by boat."),
            ("The hot springs", "Water that comes out of the bank warm, at the one bend where it does."),
            ("Nothing at all", "The day with no plan in it, which on this river is the one people talk about afterwards."),
        ],
        "days_es": [
            ("Cañón abajo", "Dos horas de paredes, garzas y cormoranes, con el motor apagado en la parte que lo merece."),
            ("Livingston", "Un almuerzo que se lleva la tarde, en un pueblo al que solo se llega en lancha."),
            ("Las aguas calientes", "Agua que sale tibia de la orilla, en la única curva donde ocurre."),
            ("Nada", "El día sin plan, que en este río es del que la gente habla después."),
        ],
        "facts_en": [
            ("Getting here", "Four and a half hours by road from Guatemala City, or a short flight to the coast."),
            ("Best months", "January to April, driest and clearest on the water."),
            ("How you move", "By boat, almost entirely. Bring less than you think."),
        ],
        "facts_es": [
            ("Cómo se llega", "Cuatro horas y media por carretera desde la Ciudad de Guatemala, o un vuelo corto a la costa."),
            ("Mejores meses", "De enero a abril, los más secos y limpios sobre el agua."),
            ("Cómo se mueve uno", "En lancha, casi siempre. Traiga menos de lo que cree."),
        ],
    },
    {
        "slug": "ciudad",
        "image": "img/ciudad.jpg",
        "image_pos": "center 45%",
        "alt_en": "Guatemala City above its ravines at the end of the day",
        "alt_es": "La Ciudad de Guatemala sobre sus barrancos al final del día",
        "eyebrow_en": "Guatemala", "eyebrow_es": "Guatemala",
        "name_en": "Guatemala City", "name_es": "Ciudad de Guatemala",
        "title_en": "The first night, and the last one.",
        "title_es": "La primera noche, y la última.",
        "lead_en": "Where the flights land. Worth a day at each end of the trip rather than none at all.",
        "lead_es": "Donde aterrizan los vuelos. Vale un día a cada extremo del viaje, en lugar de ninguno.",
        "body_en": [
            "Most people drive straight out of it, which is a way of missing the best food in the country. Zona 4 was warehouses ten years ago and is now where people eat late; Zona 10 is quieter and older about it. Either way you are half an hour from the airport.",
            "There are two small museums worth the morning, one for textiles and one for the ceramics, and a market that is not staged for anyone. Then a car at whatever hour the flight actually leaves.",
        ],
        "body_es": [
            "Casi todos salen de ella de inmediato, que es una manera de perderse la mejor comida del país. La Zona 4 eran bodegas hace diez años y hoy es donde se cena tarde; la Zona 10 es más callada y más antigua en eso. En cualquier caso está a media hora del aeropuerto.",
            "Hay dos museos pequeños que valen la mañana, uno de textiles y otro de cerámica, y un mercado que no está montado para nadie. Después, un carro a la hora a la que de verdad sale el vuelo.",
        ],
        "days_en": [
            ("Dinner, late", "The one meal that tells you what the country actually cooks, eaten at the hour the city eats it."),
            ("Two museums, one morning", "Textiles and ceramics, both small, both worth more time than they take."),
            ("The market", "Loud, unstaged, and the right place to buy the thing you will actually keep."),
            ("The way out", "A car at the hour the flight leaves, however unreasonable that hour is."),
        ],
        "days_es": [
            ("Cenar tarde", "La comida que explica lo que de verdad se cocina en el país, a la hora en que la ciudad la come."),
            ("Dos museos, una mañana", "Textiles y cerámica, los dos pequeños, los dos mejores de lo que aparentan."),
            ("El mercado", "Ruidoso, sin montaje, y el lugar correcto para comprar lo único que va a conservar."),
            ("La salida", "Un carro a la hora del vuelo, por poco razonable que sea esa hora."),
        ],
        "facts_en": [
            ("Getting here", "Every international flight arrives here. La Aurora sits inside the city."),
            ("Onward", "Fifty minutes to Antigua, three hours to the lake."),
            ("How long", "A night at each end is enough, and more than most people give it."),
        ],
        "facts_es": [
            ("Cómo se llega", "Todos los vuelos internacionales llegan aquí. La Aurora está dentro de la ciudad."),
            ("Hacia dónde sigue", "Cincuenta minutos a Antigua, tres horas al lago."),
            ("Cuánto tiempo", "Una noche a cada extremo basta, y es más de lo que casi nadie le da."),
        ],
    },
]


def t(en, es):
    """A translatable node's attributes plus its English default text."""
    return 'data-en="{}" data-es="{}">{}'.format(
        html.escape(en, quote=True), html.escape(es, quote=True), html.escape(en)
    )


def head(d):
    title_en = "Aldaba | {}".format(d["name_en"])
    title_es = "Aldaba | {}".format(d["name_es"])
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title {t(title_en, title_es)}</title>
  <meta name="description" content="{html.escape(d['lead_en'], quote=True)}"
        data-en="{html.escape(d['lead_en'], quote=True)}"
        data-es="{html.escape(d['lead_es'], quote=True)}">
  <link rel="stylesheet" href="../styles.css">
</head>
<body>

  <a class="skip" href="#content" {t("Skip to content", "Saltar al contenido")}</a>
"""


def header_and_menu():
    return """
  <header class="header" id="header">
    <div class="wrap header__bar">

      <button class="menu-trigger" id="menu-trigger" type="button"
              aria-controls="menu" aria-expanded="false"
              data-en-label="Open menu" data-es-label="Abrir menú" aria-label="Open menu">
        <span class="menu-trigger__bars" aria-hidden="true"></span>
        <span class="menu-trigger__word" data-en="Menu" data-es="Menú">Menu</span>
      </button>

      <a class="wordmark" href="../index.html"
         data-en-label="Aldaba, home" data-es-label="Aldaba, inicio"
         aria-label="Aldaba, home"><span class="wordmark__pair"><img class="wordmark__img wordmark__img--light" src="../img/brand/wordmark-light.png" alt="" aria-hidden="true"><img class="wordmark__img wordmark__img--ink" src="../img/brand/wordmark-ink.png" alt="" aria-hidden="true"></span></a>

      <div class="header__right">
        <div class="lang" role="group"
             data-en-label="Language" data-es-label="Idioma" aria-label="Language">
          <button class="lang__opt" type="button" data-lang="en" aria-pressed="true">EN</button>
          <button class="lang__opt" type="button" data-lang="es" aria-pressed="false">ES</button>
        </div>
        <a class="reserve" href="../index.html#contact" data-en="Reserve" data-es="Reservar">Reserve</a>
      </div>

    </div>
  </header>

  <div class="scrim" id="scrim"></div>

  <nav class="menu" id="menu" data-en-label="Main" data-es-label="Principal" aria-label="Main" aria-hidden="true">

    <div class="menu__head">
      <a class="menu__wordmark" href="../index.html"
         data-en-label="Aldaba, home" data-es-label="Aldaba, inicio"
         aria-label="Aldaba, home"><img class="wordmark__img" src="../img/brand/wordmark-ink.png" alt="" aria-hidden="true"></a>

      <button class="menu__close" id="menu-close" type="button"
              data-en-label="Close menu" data-es-label="Cerrar menú" aria-label="Close menu">
        <span class="menu__close-mark" aria-hidden="true"></span>
      </button>
    </div>

    <ul class="menu__list">
      <li><a class="menu__link" href="../index.html#destinations" data-en="Destinations" data-es="Destinos">Destinations</a></li>
      <li><a class="menu__link" href="../index.html#houses" data-en="Houses" data-es="Casas">Houses</a></li>
      <li><a class="menu__link" href="../about.html" data-en="About us" data-es="Quiénes somos">About us</a></li>
      <li><a class="menu__link" href="../index.html#concierge" data-en="Concierge" data-es="Concierge">Concierge</a></li>
      <li><a class="menu__link" href="../index.html#journal" data-en="Journal" data-es="Diario">Journal</a></li>
      <li><a class="menu__link" href="../index.html#contact" data-en="Contact us" data-es="Contáctenos">Contact us</a></li>
    </ul>

    <div class="menu__lang" role="group" data-en-label="Language" data-es-label="Idioma" aria-label="Language">
      <button class="lang__opt" type="button" data-lang="en" aria-pressed="true">EN</button>
      <button class="lang__opt" type="button" data-lang="es" aria-pressed="false">ES</button>
    </div>

    <div class="menu__quick">
      <a href="../index.html#destinations" data-en="Reserve" data-es="Reservar">Reserve</a>
      <a href="../index.html#contact">WhatsApp</a>
    </div>

  </nav>
"""


def hero(d):
    if d["image"]:
        media = (
            '      <div class="hero__media" style="background-image:'
            'linear-gradient(180deg, rgba(0,0,0,0.40) 0%, rgba(0,0,0,0.10) 38%, rgba(0,0,0,0.72) 100%),'
            "url('../{img}'); background-position:center, {pos};\" role=\"img\"\n"
            '           data-en-label="{alt_en}" data-es-label="{alt_es}" aria-label="{alt_en}"></div>'
        ).format(img=d["image"], pos=d["image_pos"],
                 alt_en=html.escape(d["alt_en"], quote=True),
                 alt_es=html.escape(d["alt_es"], quote=True))
        cls = "hero hero--page"
    else:
        # No licensed photograph for this destination yet. The plain panel is
        # deliberate rather than broken; swap in an image and it disappears.
        media = '      <div class="hero__media hero__media--plain" aria-hidden="true"></div>'
        cls = "hero hero--page hero--plain"

    return f"""
  <main id="content">

    <section class="{cls}">
{media}

      <div class="wrap hero__body">
        <article class="feature">
          <p class="eyebrow feature__eyebrow" {t(d['eyebrow_en'], d['eyebrow_es'])}</p>
          <h1 class="feature__title" {t(d['name_en'], d['name_es'])}</h1>
          <p class="feature__text" {t(d['lead_en'], d['lead_es'])}</p>
        </article>
      </div>
    </section>
"""


def place(d):
    paras = "\n".join(
        '        <p class="section__lead" {}</p>'.format(t(en, es))
        for en, es in zip(d["body_en"], d["body_es"])
    )
    return f"""
    <section class="section reveal">
      <div class="wrap">
        <p class="eyebrow section__eyebrow" {t("The place", "El lugar")}</p>
        <h2 class="section__title" {t(d['title_en'], d['title_es'])}</h2>
{paras}
      </div>
    </section>
"""


def days(d):
    items = []
    for i, ((en_t, en_x), (es_t, es_x)) in enumerate(zip(d["days_en"], d["days_es"]), 1):
        items.append(
            '          <li class="grid__item">\n'
            '            <span class="grid__num">{n:02d}</span>\n'
            '            <h3 class="grid__title" {title}</h3>\n'
            '            <p class="grid__text" {text}</p>\n'
            "          </li>".format(n=i, title=t(en_t, es_t), text=t(en_x, es_x))
        )
    return """
    <section class="section reveal">
      <div class="wrap">
        <p class="eyebrow section__eyebrow" {eyebrow}</p>
        <h2 class="section__title" {title}</h2>
        <p class="section__lead" {lead}</p>

        <ul class="grid">
{items}
        </ul>
      </div>
    </section>
""".format(
        eyebrow=t("The days", "Los días"),
        title=t("What a few days here look like.", "Cómo se ven unos días aquí."),
        lead=t(
            "Written for the house you are staying in, never off a list.",
            "Se escriben para la casa donde usted se queda, nunca de una lista.",
        ),
        items="\n".join(items),
    )


def facts(d):
    rows = []
    for (en_t, en_x), (es_t, es_x) in zip(d["facts_en"], d["facts_es"]):
        rows.append(
            '          <li class="fact">\n'
            '            <p class="eyebrow fact__label" {label}</p>\n'
            '            <p class="fact__text" {text}</p>\n'
            "          </li>".format(label=t(en_t, es_t), text=t(en_x, es_x))
        )
    return """
    <section class="section section--alt reveal">
      <div class="wrap">
        <p class="eyebrow section__eyebrow" {eyebrow}</p>
        <h2 class="section__title" {title}</h2>

        <ul class="facts">
{rows}
        </ul>
      </div>
    </section>
""".format(
        eyebrow=t("Practical", "Lo práctico"),
        title=t("Worth knowing before you choose dates.", "Conviene saberlo antes de elegir fechas."),
        rows="\n".join(rows),
    )


def houses(d):
    """Houses we have here, or the plate that stands in until we do."""
    listed = [h for h in common.houses() if h["destination_slug"] == d["slug"]]

    if not listed:
        body = """        <div class="soon">
          <p class="eyebrow soon__label" {soon}</p>
          <p class="soon__text" {text}</p>
        </div>""".format(
            soon=t("Opening soon", "Muy pronto"),
            text=t(
                "The first houses in {} open later this year. Tell us when you are thinking of coming and we will write to you before they are listed anywhere.".format(d["name_en"]),
                "Las primeras casas en {} abren este año. Díganos cuándo piensa venir y le escribimos antes de que aparezcan en ningún lado.".format(d["name_es"]),
            ),
        )
    else:
        cards = "\n".join(
            '''          <li class="card">
            <a class="card__link" href="../houses/{slug}.html">
              <div class="card__media" style="background-image:url(\'../{img}\'); background-position:{pos};" aria-hidden="true"></div>
              <h3 class="card__title">{name}</h3>
              <p class="card__text" {line}</p>
              <p class="card__more" {more}</p>
            </a>
          </li>'''.format(
                slug=h["slug"], img=h["image"], pos="center 55%",
                name=html.escape(common.house_name(h)),
                line=t(h["lead_en"], h["lead_es"]),
                more=t("See the house", "Ver la casa"),
            )
            for h in listed
        )
        body = '''        <ul class="journal">
{cards}
        </ul>'''.format(cards=cards)

    return """
    <section class="section section--alt reveal">
      <div class="wrap">
        <p class="eyebrow section__eyebrow" {eyebrow}</p>
        <h2 class="section__title" {title}</h2>

{body}

        <p class="page-head__cta">
          <a class="btn-solid" href="../index.html#contact" {cta}</a>
        </p>
      </div>
    </section>
""".format(
        eyebrow=t("Houses", "Casas"),
        title=t(
            "We are taking on very few houses here.",
            "Aquí estamos tomando muy pocas casas.",
        ),
        body=body,
        cta=t("Tell us when you are coming", "Díganos cuándo viene"),
    )


def other_destinations(current):
    cards = []
    for o in DESTINATIONS:
        if o["slug"] == current["slug"]:
            continue
        media = (
            '            <div class="card__media" style="background-image:url(\'../{img}\'); background-position:{pos};" aria-hidden="true"></div>'.format(
                img=o["image"], pos=o["image_pos"]
            )
            if o["image"]
            else '            <div class="card__media card__media--plain" aria-hidden="true"></div>'
        )
        cards.append(
            '          <li class="card">\n'
            '            <a class="card__link" href="{slug}.html">\n'
            "{media}\n"
            '              <h3 class="card__title" {title}</h3>\n'
            '              <p class="card__more" {more}</p>\n'
            "            </a>\n"
            "          </li>".format(
                slug=o["slug"], media=media,
                title=t(o["name_en"], o["name_es"]),
                more=t("Discover", "Descubrir"),
            )
        )
    return """
    <section class="section reveal">
      <div class="wrap">
        <p class="eyebrow section__eyebrow" {eyebrow}</p>
        <h2 class="section__title" {title}</h2>

        <ul class="journal">
{cards}
        </ul>
      </div>
    </section>

  </main>
""".format(
        eyebrow=t("Elsewhere", "En otra parte"),
        title=t("The rest of the world of Aldaba.", "El resto del mundo de Aldaba."),
        cards="\n".join(cards),
    )


def footer():
    return common.footer_html("../") + """
  <script src="../script.js"></script>
</body>
</html>
"""


def build():
    os.makedirs(OUT, exist_ok=True)
    for d in DESTINATIONS:
        page = (
            head(d)
            + header_and_menu()
            + hero(d)
            + place(d)
            + houses(d)
            + days(d)
            + facts(d)
            + other_destinations(d)
            + footer()
        )
        path = os.path.join(OUT, d["slug"] + ".html")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(page)
        print("wrote", os.path.relpath(path, ROOT))


if __name__ == "__main__":
    build()

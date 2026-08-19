#!/usr/bin/env python3
"""
Aldaba | house pages

Source of truth for houses/*.html. Edit this file, then run:

    python3 build-houses.py

Rules the template enforces, from the project notes: no nightly rate anywhere
public, inquiry rather than booking, services named but never bundled into the
house, guest voice throughout. Everything a house needs lives in one entry in
HOUSES below, so the next house is a copy of this dict and nothing else.

Choq' is a test listing. Aldaba does not manage this house, the photograph is
stock, and the name carries "(test)" so it cannot be mistaken for real
inventory. Bedroom counts and practical details are placeholders.
"""

import os
import html

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "houses")

HOUSES = [
    {
        "slug": "choq",
        "test": True,
        "name": "Aldaba Choq'",
        "destination_slug": "atitlan",
        "place_en": "Lake Atitlán", "place_es": "Lago de Atitlán",
        "image": "img/houses/choq-01.jpg",
        "alt_en": "A bedroom opening onto a deck above Lake Atitlán",
        "alt_es": "Una habitación que abre a una terraza sobre el lago de Atitlán",

        "lead_en": "You wake with the lake already in the room. The wall folds away and there is nothing between the bed and the water.",
        "lead_es": "Uno despierta con el lago ya adentro. La pared se recoge y entre la cama y el agua no queda nada.",

        "body_en": [
            "The light comes first. It lifts off the water at six, crosses the deck and climbs the ceiling, and it wakes you before any alarm would. Most people lie there and let it. Then the sound arrives, or rather the lack of it: water against the rock below, an outboard somewhere far off, and after that nothing at all.",
            "By two the wind is up and the lake has changed its mind, and so has the room. The house was built to sit inside that rhythm rather than shut it out. Concrete, wood, glass, and very little else. It is small on purpose. Four people, two rooms, one long table, and no reason to be anywhere by any particular hour.",
        ],
        "body_es": [
            "Primero llega la luz. Se levanta del agua a las seis, cruza la terraza y sube por el techo, y despierta a uno antes que cualquier alarma. Casi todos se quedan quietos y la dejan. Después llega el sonido, o más bien su ausencia: el agua contra la roca, un motor lejísimos, y después nada.",
            "Para las dos el viento ya subió, el lago cambió de opinión y la habitación también. La casa está hecha para vivir dentro de ese ritmo y no para taparlo. Concreto, madera, vidrio, y muy poco más. Es pequeña a propósito. Cuatro personas, dos cuartos, una mesa larga, y ninguna razón para estar en ningún lado a ninguna hora.",
        ],

        "stats_en": [("Guests", "4"), ("Bedrooms", "2"), ("Baths", "2"), ("Arrival", "By boat")],
        "stats_es": [("Huéspedes", "4"), ("Habitaciones", "2"), ("Baños", "2"), ("Llegada", "En lancha")],

        "rooms_en": [
            ("The glass room", "You sleep with the corner open. At six the lake is in the room with you and the floor runs straight on out to the deck."),
            ("The deck", "Warm boards underfoot, a metre of air, then water. In shade by four, and the best place in the house to do nothing."),
            ("The second room", "Set back and quieter, for whoever would rather the light arrived later."),
            ("The kitchen", "Small, well used, and stocked before you arrive with what you told us you like. The coffee is grown on the ridge above the house."),
            ("The dock", "Where the boat comes and goes, and where the swim happens, usually before anyone has bothered to dress."),
            ("The house team", "A housekeeper and a caretaker from the village, who will know your name by the second morning and your coffee by the third."),
        ],
        "rooms_es": [
            ("La habitación de vidrio", "Uno duerme con la esquina abierta. A las seis el lago está adentro con usted y el piso sigue de largo hasta la terraza."),
            ("La terraza", "Tablas tibias bajo los pies, un metro de aire, y después agua. Con sombra a las cuatro, y el mejor lugar de la casa para no hacer nada."),
            ("La segunda habitación", "Retirada y más callada, para quien prefiere que la luz llegue más tarde."),
            ("La cocina", "Pequeña, bien usada, y surtida antes de que llegue con lo que nos dijo que le gusta. El café se cultiva en la ladera de arriba."),
            ("El muelle", "Por donde va y viene la lancha, y donde ocurre el clavado, casi siempre antes de que alguien se haya vestido."),
            ("La casa", "Una camarista y un encargado del pueblo, que para la segunda mañana saben su nombre y para la tercera saben su café."),
        ],

        "programmes": [
            {
                "key": "ascent",
                "name_en": "Ascent", "name_es": "Ascenso",
                "title_en": "Come home tired.",
                "title_es": "Volver cansado.",
                "text_en": "Out on the water before it is awake, up something steep after, and the good kind of ache by dinner.",
                "text_es": "Al agua antes de que despierte, a algo empinado después, y el buen cansancio a la hora de la cena.",
                "beats_en": [
                    ("Before light", "Out across the lake while it is still glass, San Pedro going pink on the far side, and nobody else awake to see it."),
                    ("The day", "Up the volcano with a guide of your own, or the long paddle to the cliffs and back before the wind."),
                    ("After dark", "Dinner on the deck, and an alarm nobody argues with."),
                ],
                "beats_es": [
                    ("Antes de la luz", "Cruzar el lago mientras todavía es un vidrio, con el San Pedro poniéndose rosado al otro lado."),
                    ("El día", "Subir el volcán con un guía propio, o remar hasta los peñascos y volver antes del viento."),
                    ("De noche", "Cena en la terraza, y una alarma que nadie discute."),
                ],
            },
            {
                "key": "stillness",
                "name_en": "Stillness", "name_es": "Reposo",
                "title_en": "Nothing before ten.",
                "title_es": "Nada antes de las diez.",
                "text_en": "The house was built for this one. The wall stays open, the day stays empty, and the hardest decision is whether to swim before or after coffee.",
                "text_es": "La casa está hecha para este. La pared se queda abierta, el día se queda vacío, y la decisión más difícil es si nadar antes o después del café.",
                "beats_en": [
                    ("The morning", "Coffee on the deck with the wall folded back, and the lake entirely yours until the first boat crosses."),
                    ("The day", "A temazcal heated on the shore, hands that know what they are doing, and long gaps between things."),
                    ("After dark", "One table, cooked in the house, and the doors left open."),
                ],
                "beats_es": [
                    ("La mañana", "Café en la terraza con la pared recogida, y el lago para usted hasta que pase la primera lancha."),
                    ("El día", "Un temazcal calentado en la orilla, manos que saben lo que hacen, y espacios largos entre una cosa y otra."),
                    ("De noche", "Una sola mesa, cocinada en la casa, y las puertas abiertas."),
                ],
            },
            {
                "key": "root",
                "name_en": "Root", "name_es": "Raíz",
                "title_en": "The lake, from the people who live on it.",
                "title_es": "El lago, de la mano de quien vive en él.",
                "text_en": "Twelve villages, three languages, and a kitchen where the recipe is older than the question you asked in it.",
                "text_es": "Doce pueblos, tres idiomas, y una cocina donde la receta es más vieja que la pregunta que usted hizo adentro.",
                "beats_en": [
                    ("The morning", "Santiago at market hour, with somebody who is from there and is known there."),
                    ("The day", "Weaving where it is actually done, and a kitchen older than the language you are asking in."),
                    ("After dark", "What a family from the next village along cooks for itself, at the hour they eat it."),
                ],
                "beats_es": [
                    ("La mañana", "Santiago a la hora del mercado, con alguien de allí y conocido allí."),
                    ("El día", "Tejido donde de verdad se teje, y una cocina más antigua que el idioma en que usted pregunta."),
                    ("De noche", "Lo que cocina para sí misma una familia del pueblo de al lado, a la hora en que lo comen."),
                ],
            },
        ],

        "facts_en": [
            ("Getting here", "About three hours from Guatemala City to the shore, then twelve minutes by private boat. Arrive before noon."),
            ("Worth knowing", "The last stretch is on the water, so bags travel by boat and there is no road to the door."),
            ("Not here", "No television and no pool. The lake is thirty seconds away and cold."),
        ],
        "facts_es": [
            ("Cómo se llega", "Unas tres horas de la Ciudad de Guatemala a la orilla, y doce minutos en lancha privada. Conviene llegar antes del mediodía."),
            ("Conviene saber", "El último tramo es sobre el agua: las maletas van en lancha y no hay carretera hasta la puerta."),
            ("Lo que no hay", "Ni televisión ni piscina. El lago está a treinta segundos y está frío."),
        ],
    },
]


def t(en, es):
    return 'data-en="{}" data-es="{}">{}'.format(
        html.escape(en, quote=True), html.escape(es, quote=True), html.escape(en)
    )


def display_name(h):
    return h["name"] + (" (test)" if h.get("test") else "")


def head(h):
    name = display_name(h)
    robots = '  <meta name="robots" content="noindex, nofollow">\n' if h.get("test") else ""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Aldaba | {html.escape(name)}</title>
{robots}  <meta name="description" content="{html.escape(h['lead_en'], quote=True)}">
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
        <a class="reserve" href="#enquire" data-en="Enquire" data-es="Consultar">Enquire</a>
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
      <li><a class="menu__link" href="../index.html#experiences" data-en="Experiences" data-es="Experiencias">Experiences</a></li>
      <li><a class="menu__link" href="../index.html#concierge" data-en="Concierge" data-es="Concierge">Concierge</a></li>
      <li><a class="menu__link" href="../index.html#contact" data-en="Contact us" data-es="Contáctenos">Contact us</a></li>
    </ul>

    <div class="menu__lang" role="group" data-en-label="Language" data-es-label="Idioma" aria-label="Language">
      <button class="lang__opt" type="button" data-lang="en" aria-pressed="true">EN</button>
      <button class="lang__opt" type="button" data-lang="es" aria-pressed="false">ES</button>
    </div>

    <div class="menu__quick">
      <a href="#enquire" data-en="Enquire" data-es="Consultar">Enquire</a>
      <a href="../index.html#contact">WhatsApp</a>
    </div>

  </nav>
"""


def hero(h):
    name = display_name(h)
    return """
  <main id="content">

    <section class="hero hero--page">
      <div class="hero__media" style="background-image:linear-gradient(180deg, rgba(0,0,0,0.34) 0%, rgba(0,0,0,0.08) 40%, rgba(0,0,0,0.70) 100%), url('../{img}'); background-position:center, center 55%;" role="img"
           data-en-label="{alt_en}" data-es-label="{alt_es}" aria-label="{alt_en}"></div>

      <div class="wrap hero__body">
        <article class="feature">
          <p class="eyebrow feature__eyebrow" {place}</p>
          <h1 class="feature__title">{name}</h1>
          <p class="feature__text" {lead}</p>
        </article>
      </div>
    </section>
""".format(
        img=h["image"], name=html.escape(name),
        alt_en=html.escape(h["alt_en"], quote=True), alt_es=html.escape(h["alt_es"], quote=True),
        place=t(h["place_en"], h["place_es"]), lead=t(h["lead_en"], h["lead_es"]),
    )


def house(h):
    paras = "\n".join(
        '        <p class="section__lead" {}</p>'.format(t(en, es))
        for en, es in zip(h["body_en"], h["body_es"])
    )
    stats = "\n".join(
        '          <li class="stat">\n'
        '            <p class="stat__value" {val}</p>\n'
        '            <p class="stat__label" {label}</p>\n'
        "          </li>".format(val=t(en[1], es[1]), label=t(en[0], es[0]))
        for en, es in zip(h["stats_en"], h["stats_es"])
    )
    return """
    <section class="section reveal">
      <div class="wrap">
        <p class="eyebrow section__eyebrow" {eyebrow}</p>
        <h2 class="section__title" {title}</h2>
{paras}

        <ul class="stats">
{stats}
        </ul>
      </div>
    </section>
""".format(
        eyebrow=t("The house", "La casa"),
        title=t("Wake up on the water.", "Despertar sobre el agua."),
        paras=paras, stats=stats,
    )


def rooms(h):
    items = "\n".join(
        '          <li class="grid__item">\n'
        '            <h3 class="grid__title" {title}</h3>\n'
        '            <p class="grid__text" {text}</p>\n'
        "          </li>".format(title=t(en[0], es[0]), text=t(en[1], es[1]))
        for en, es in zip(h["rooms_en"], h["rooms_es"])
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
        eyebrow=t("Inside", "Adentro"),
        title=t("Six things you will remember.", "Seis cosas que se le van a quedar."),
        items=items,
    )


def days(h):
    """Three programmes, one panel at a time. Aman does not sell the same days
    at every property, and neither do we."""
    tabs, panels = [], []

    for i, prog in enumerate(h["programmes"]):
        pid = prog["key"]
        tabs.append(
            '''            <button class="prog__tab" type="button" role="tab" id="tab-{pid}"
                    aria-controls="panel-{pid}" aria-selected="{sel}" {name}</button>'''.format(
                pid=pid, sel="true" if i == 0 else "false",
                name=t(prog["name_en"], prog["name_es"]),
            )
        )

        beats = "\n".join(
            '''              <li class="prog__beat">
                <p class="prog__when" {when}</p>
                <p class="prog__what" {what}</p>
              </li>'''.format(when=t(en[0], es[0]), what=t(en[1], es[1]))
            for en, es in zip(prog["beats_en"], prog["beats_es"])
        )

        panels.append(
            '''          <div class="prog__panel" role="tabpanel" id="panel-{pid}" aria-labelledby="tab-{pid}"{hidden}>
            <div class="prog__intro">
              <h3 class="prog__title" {title}</h3>
              <p class="prog__text" {text}</p>
            </div>
            <ul class="prog__beats">
{beats}
            </ul>
          </div>'''.format(
                pid=pid, hidden="" if i == 0 else " hidden",
                title=t(prog["title_en"], prog["title_es"]),
                text=t(prog["text_en"], prog["text_es"]),
                beats=beats,
            )
        )

    return """
    <section class="section reveal">
      <div class="wrap">
        <p class="eyebrow section__eyebrow" {eyebrow}</p>
        <h2 class="section__title" {title}</h2>
        <p class="section__lead" {lead}</p>

        <div class="prog" data-prog>
          <div class="prog__tabs" role="tablist"
               data-en-label="Programmes" data-es-label="Programas" aria-label="Programmes">
{tabs}
          </div>

{panels}
        </div>
      </div>
    </section>


""".format(
        eyebrow=t("Programmes", "Programas"),
        title=t("Three ways to spend the same week.", "Tres maneras de pasar la misma semana."),
        lead=t(
            "Written for this house. Arranged by us, charged only if you want it, and never bundled into the house.",
            "Escritos para esta casa. Los arreglamos nosotros, se cobran solo si usted los quiere, y nunca van incluidos en la casa.",
        ),
        tabs="\n".join(tabs),
        panels="\n\n".join(panels),
    )


def facts(h):
    rows = "\n".join(
        '          <li class="fact">\n'
        '            <p class="eyebrow fact__label" {label}</p>\n'
        '            <p class="fact__text" {text}</p>\n'
        "          </li>".format(label=t(en[0], es[0]), text=t(en[1], es[1]))
        for en, es in zip(h["facts_en"], h["facts_es"])
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
        title=t("Before you choose dates.", "Antes de elegir fechas."),
        rows=rows,
    )


def enquire(h):
    return """
    <section class="section reveal" id="enquire">
      <div class="wrap">
        <p class="eyebrow section__eyebrow" {eyebrow}</p>
        <h2 class="section__title" {title}</h2>
        <p class="section__lead" {lead}</p>

        <div class="contact">
          <form class="contact__form" id="house-enquiry" novalidate>
            <input type="hidden" name="house" value="{name}">

            <label class="field">
              <span class="field__label" {f_name}</span>
              <input class="field__input" type="text" name="name" autocomplete="name" required>
            </label>

            <div class="field field--pair">
              <label>
                <span class="field__label" {f_email}</span>
                <input class="field__input" type="email" name="email" autocomplete="email">
              </label>
              <label>
                <span class="field__label" {f_dates}</span>
                <input class="field__input" type="text" name="dates" placeholder="—">
              </label>
            </div>

            <div class="field field--pair">
              <label>
                <span class="field__label" {f_guests}</span>
                <input class="field__input" type="text" name="guests" placeholder="—">
              </label>
              <label>
                <span class="field__label" {f_budget}</span>
                <input class="field__input" type="text" name="budget" placeholder="—">
              </label>
            </div>

            <label class="field">
              <span class="field__label" {f_more}</span>
              <textarea class="field__area" name="message" rows="3"></textarea>
            </label>

            <button class="btn-solid" type="submit" {send}</button>
          </form>

          <aside class="contact__aside">
            <div class="aside__row">
              <p class="eyebrow aside__label">WhatsApp</p>
              <p class="aside__value">+502 0000 0000</p>
            </div>
            <div class="aside__row">
              <p class="eyebrow aside__label" {a_reply}</p>
              <p class="aside__value" {a_reply_v}</p>
              <p class="aside__note" {a_note}</p>
            </div>
          </aside>
        </div>
      </div>
    </section>

  </main>
""".format(
        eyebrow=t("Enquire", "Consultar"),
        title=t("Tell us when you are coming.", "Díganos cuándo viene."),
        lead=t(
            "Dates, how many of you, and what you want the days to feel like. A person answers, and nothing is charged online.",
            "Fechas, cuántos vienen, y cómo quiere que se sientan los días. Contesta una persona, y no se cobra nada en línea.",
        ),
        name=html.escape(display_name(h), quote=True),
        f_name=t("Your name", "Su nombre"),
        f_email=t("Email", "Correo"),
        f_dates=t("Dates", "Fechas"),
        f_guests=t("Guests", "Huéspedes"),
        f_budget=t("Budget for the stay", "Presupuesto para la estadía"),
        f_more=t("Anything else", "Algo más"),
        send=t("Send enquiry", "Enviar consulta"),
        a_reply=t("Reply", "Respuesta"),
        a_reply_v=t("Within one working day", "En un día hábil"),
        a_note=t(
            "We hold dates for 48 hours while you decide.",
            "Sostenemos las fechas 48 horas mientras usted decide.",
        ),
    )


def footer(h):
    return """
  <footer class="footer">
    <div class="wrap footer__bar">
      <p class="footer__mark"><img class="wordmark__img" src="../img/brand/wordmark-ink.png" alt="" aria-hidden="true"><span class="sr-only">Aldaba</span></p>
      <p class="footer__tag">Well received.</p>
      <nav class="footer__links" data-en-label="Secondary" data-es-label="Secundario" aria-label="Secondary">
        <a href="../destinations/{dest}.html" {back}</a>
        <a href="../index.html#contact" {contact}</a>
        <a href="../propietarios.html" rel="nofollow" {owners}</a>
      </nav>
    </div>
  </footer>

  <script src="../script.js"></script>
</body>
</html>
""".format(
        dest=h["destination_slug"],
        back=t("Back to " + h["place_en"], "Volver a " + h["place_es"]),
        contact=t("Contact us", "Contáctenos"),
        owners=t("Property owners", "Propietarios"),
    )


def build():
    os.makedirs(OUT, exist_ok=True)
    for h in HOUSES:
        page = (head(h) + header_and_menu() + hero(h) + house(h) + rooms(h)
                + days(h) + facts(h) + enquire(h) + footer(h))
        path = os.path.join(OUT, h["slug"] + ".html")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(page)
        print("wrote", os.path.relpath(path, ROOT))


if __name__ == "__main__":
    build()

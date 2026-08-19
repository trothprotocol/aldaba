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

import common

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "houses")

HOUSES = [
    {
        "slug": "choq",
        "house_title_en": "Wake up on the water.",
        "house_title_es": "Despertar sobre el agua.",
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
    {
        "slug": "ja",
        "house_title_en": "The doors open, and stay open.",
        "house_title_es": "Las puertas se abren, y se quedan abiertas.",
        "test": True,
        "name": "Aldaba Ja'",
        "destination_slug": "antigua",
        "place_en": "Antigua", "place_es": "Antigua",
        "image": "img/houses/ja-01.jpg",
        "alt_en": "A lit house opening onto its garden at dusk",
        "alt_es": "Una casa encendida abriéndose al jardín al anochecer",

        "lead_en": "The whole ground floor opens, and the garden becomes another room. Agua stands over the wall at the end of it.",
        "lead_es": "Toda la planta baja se abre y el jardín se vuelve otro cuarto. El Agua se levanta detrás del muro del fondo.",

        "body_en": [
            "It is a quiet street ten minutes on foot from the arch, which is the correct distance: close enough to walk in for dinner, far enough that the bells arrive softened. Behind the wall the house turns its back on all of it and looks at the volcano instead.",
            "Everything happens on the ground floor. The kitchen opens to the terrace, the terrace opens to the grass, and by the second evening nobody is bothering to close anything. Four bedrooms upstairs, each with a bath, each cool enough at night to want the blanket.",
        ],
        "body_es": [
            "Es una calle callada a diez minutos a pie del arco, que es la distancia correcta: cerca para ir caminando a cenar, lejos para que las campanas lleguen suaves. Detrás del muro la casa le da la espalda a todo eso y mira al volcán.",
            "Todo pasa en la planta baja. La cocina abre a la terraza, la terraza abre al pasto, y para la segunda noche ya nadie se molesta en cerrar nada. Cuatro habitaciones arriba, cada una con baño, y noches lo bastante frescas para querer la cobija.",
        ],

        "stats_en": [("Guests", "8"), ("Bedrooms", "4"), ("Baths", "4"), ("Arrival", "By car")],
        "stats_es": [("Huéspedes", "8"), ("Habitaciones", "4"), ("Baños", "4"), ("Llegada", "En carro")],

        "rooms_en": [
            ("The long doors", "The ground floor folds open across its whole width. Most mornings it never gets closed again."),
            ("The garden", "Grass, old trees, and the volcano standing behind the far wall as though it were part of the property."),
            ("The kitchen", "Where everyone ends up, whether or not a chef is cooking in it that night."),
            ("The fire", "Lit at six by someone who knows how, because Antigua is colder after dark than anyone expects."),
            ("Four rooms upstairs", "Thick walls, cool floors, and shutters that keep the light out until you decide otherwise."),
            ("The house team", "A housekeeper and a caretaker who will have your coffee right by the second morning."),
        ],
        "rooms_es": [
            ("Las puertas largas", "La planta baja se abre de lado a lado. Casi todas las mañanas ya no se vuelve a cerrar."),
            ("El jardín", "Pasto, árboles viejos, y el volcán parado detrás del muro del fondo como si fuera parte del terreno."),
            ("La cocina", "Donde termina todo el mundo, cocine o no un chef esa noche."),
            ("El fuego", "Encendido a las seis por alguien que sabe hacerlo, porque Antigua es más fría de noche de lo que cualquiera espera."),
            ("Cuatro cuartos arriba", "Paredes gruesas, pisos frescos, y postigos que dejan la luz afuera hasta que usted decida."),
            ("La casa", "Una camarista y un encargado que para la segunda mañana ya le dan bien el café."),
        ],

        "programmes": [
            {
                "key": "ascent",
                "name_en": "Ascent", "name_es": "Ascenso",
                "title_en": "Come home tired.",
                "title_es": "Volver cansado.",
                "text_en": "The trailhead is twenty minutes from the door, and the fire will be lit when you get back.",
                "text_es": "El inicio del camino está a veinte minutos de la puerta, y el fuego estará encendido cuando vuelva.",
                "beats_en": [
                    ("Before light", "Acatenango, with the camp already standing and Fuego throwing light across the saddle after dark."),
                    ("The day", "Coffee slopes on foot, or the old road to the ridge, with somebody who has walked it since he was a boy."),
                    ("After dark", "Back through the arch for dinner, and a fire someone else lit."),
                ],
                "beats_es": [
                    ("Antes de la luz", "El Acatenango, con el campamento ya montado y el Fuego tirando luz sobre la silla cuando cae la noche."),
                    ("El día", "Laderas de café a pie, o el camino viejo a la cresta, con alguien que lo camina desde niño."),
                    ("De noche", "De vuelta por el arco a cenar, y un fuego que encendió otro."),
                ],
            },
            {
                "key": "stillness",
                "name_en": "Stillness", "name_es": "Reposo",
                "title_en": "Nothing before ten.",
                "title_es": "Nada antes de las diez.",
                "text_en": "A garden, a wall, and a volcano. The city can wait until the light goes long.",
                "text_es": "Un jardín, un muro y un volcán. La ciudad puede esperar a que la luz se alargue.",
                "beats_en": [
                    ("The morning", "Breakfast under the trees, and the doors open before anybody is dressed."),
                    ("The day", "A massage in the garden, an afternoon in the shade, and nowhere at all to be."),
                    ("After dark", "A chef in the kitchen, one long table, and the fire going down slowly."),
                ],
                "beats_es": [
                    ("La mañana", "Desayuno bajo los árboles, y las puertas abiertas antes de que nadie se haya vestido."),
                    ("El día", "Un masaje en el jardín, una tarde a la sombra, y ningún lugar donde estar."),
                    ("De noche", "Un chef en la cocina, una sola mesa larga, y el fuego bajando despacio."),
                ],
            },
            {
                "key": "root",
                "name_en": "Root", "name_es": "Raíz",
                "title_en": "A working coffee town, not a film set.",
                "title_es": "Un pueblo cafetalero de verdad, no un set.",
                "text_en": "The city is four hundred years old and still doing what it always did.",
                "text_es": "La ciudad tiene cuatrocientos años y sigue haciendo lo que siempre hizo.",
                "beats_en": [
                    ("The morning", "A finca at picking time with the family who own the slope, and coffee drunk metres from the tree."),
                    ("The day", "The market before the tour buses, and a workshop where the jade is still cut by hand."),
                    ("After dark", "Somebody's kitchen rather than a restaurant, at the hour they actually eat."),
                ],
                "beats_es": [
                    ("La mañana", "Una finca en corte con la familia dueña de la ladera, y café tomado a metros del árbol."),
                    ("El día", "El mercado antes de los buses, y un taller donde el jade todavía se corta a mano."),
                    ("De noche", "La cocina de alguien y no un restaurante, a la hora en que de verdad se cena."),
                ],
            },
        ],

        "facts_en": [
            ("Getting here", "Fifty minutes from the airport, door to door, with a driver waiting however late you land."),
            ("Best months", "November to April. Cold at night, which is what the fire is for."),
            ("One week to know about", "Semana Santa. The most beautiful week of the year here, and the fullest."),
        ],
        "facts_es": [
            ("Cómo se llega", "Cincuenta minutos del aeropuerto, de puerta a puerta, con un chofer esperando por tarde que aterrice."),
            ("Mejores meses", "De noviembre a abril. Frío de noche, que es para lo que está la chimenea."),
            ("Una semana que conviene saber", "Semana Santa. La semana más hermosa del año aquí, y la más llena."),
        ],
    },
    {
        "slug": "ki",
        "house_title_en": "Under twenty feet of palm.",
        "house_title_es": "Bajo seis metros de palma.",
        "test": True,
        "name": "Aldaba Ki'",
        "destination_slug": "rio-dulce",
        "place_en": "Río Dulce", "place_es": "Río Dulce",
        "image": "img/houses/ki-01.jpg",
        "alt_en": "A bedroom under a high thatched roof, open to the trees",
        "alt_es": "Una habitación bajo un techo alto de palma, abierta a los árboles",

        "lead_en": "A room under a high roof of palm, open on two sides, with the river moving somewhere below the trees.",
        "lead_es": "Un cuarto bajo un techo alto de palma, abierto por dos lados, con el río moviéndose en algún lugar bajo los árboles.",

        "body_en": [
            "You arrive by boat because there is no other way, and that changes the register of the whole week before you have unpacked. The house stands back in the trees on its own stretch of bank, hardwood and thatch, built high so the air moves through it.",
            "At six the howler monkeys start somewhere upriver and the birds answer, and it is the loudest the place will get all day. After that it is water, insects and rain on the palm, which is the sound most people say they came back for.",
        ],
        "body_es": [
            "Uno llega en lancha porque no hay otra manera, y eso cambia el tono de toda la semana antes de deshacer la maleta. La casa está retirada entre los árboles, en su propio tramo de orilla, de madera dura y palma, levantada para que el aire la atraviese.",
            "A las seis empiezan los saraguates río arriba y contestan los pájaros, y es lo más ruidoso que se pone el lugar en todo el día. Después es agua, insectos y lluvia sobre la palma, que es el sonido por el que casi todos dicen que volvieron.",
        ],

        "stats_en": [("Guests", "6"), ("Bedrooms", "3"), ("Baths", "3"), ("Arrival", "By boat")],
        "stats_es": [("Huéspedes", "6"), ("Habitaciones", "3"), ("Baños", "3"), ("Llegada", "En lancha")],

        "rooms_en": [
            ("Under the palm", "Twenty feet of thatch above the bed, open on two sides, with mosquito nets that are actually beautiful."),
            ("The deck over the water", "Where breakfast happens, and where somebody always ends up asleep in the afternoon."),
            ("The dock", "Your own boat, and a captain who knows which channels are worth the detour."),
            ("The kitchen", "River fish, coconut, and whatever came up from Livingston that morning."),
            ("The hammocks", "Four of them. This is not a joke about doing nothing; it is the actual plan."),
            ("The house team", "A cook and a caretaker who live along the bank and have done all their lives."),
        ],
        "rooms_es": [
            ("Bajo la palma", "Seis metros de techo sobre la cama, abierta por dos lados, con mosquiteros que de verdad son bonitos."),
            ("La terraza sobre el agua", "Donde se desayuna, y donde siempre termina alguien dormido por la tarde."),
            ("El muelle", "Su propia lancha, y un capitán que sabe qué canales valen el desvío."),
            ("La cocina", "Pescado de río, coco, y lo que haya subido de Livingston esa mañana."),
            ("Las hamacas", "Cuatro. No es un chiste sobre no hacer nada; es el plan de verdad."),
            ("La casa", "Una cocinera y un encargado que viven en la orilla y siempre han vivido ahí."),
        ],

        "programmes": [
            {
                "key": "ascent",
                "name_en": "Ascent", "name_es": "Ascenso",
                "title_en": "Everything here is reached by water.",
                "title_es": "Aquí todo se alcanza por agua.",
                "text_en": "Kayaks at dawn, the gorge at speed, and a beach at the end of it.",
                "text_es": "Kayaks al amanecer, el cañón a toda velocidad, y una playa al final.",
                "beats_en": [
                    ("Before light", "Out on the water while the mist is still sitting on it, and the birds are the only traffic."),
                    ("The day", "Down the gorge, out to the cays, and a swim where the river finally turns to sea."),
                    ("After dark", "Back late, salt on everything, and dinner that was swimming this morning."),
                ],
                "beats_es": [
                    ("Antes de la luz", "Al agua mientras la neblina todavía está encima, con los pájaros como único tráfico."),
                    ("El día", "Cañón abajo, salir a los cayos, y un clavado donde el río por fin se hace mar."),
                    ("De noche", "Volver tarde, sal en todo, y una cena que esta mañana estaba nadando."),
                ],
            },
            {
                "key": "stillness",
                "name_en": "Stillness", "name_es": "Reposo",
                "title_en": "The hammock is the itinerary.",
                "title_es": "La hamaca es el itinerario.",
                "text_en": "Rain on palm, a book you will not finish, and a river that does the moving for you.",
                "text_es": "Lluvia sobre la palma, un libro que no va a terminar, y un río que se mueve por usted.",
                "beats_en": [
                    ("The morning", "The hot springs on the bank, reached before anybody else is awake to reach them."),
                    ("The day", "Nothing, deliberately, interrupted only by lunch and possibly a swim."),
                    ("After dark", "The generator off, the lamps low, and more stars than anyone is ready for."),
                ],
                "beats_es": [
                    ("La mañana", "Las aguas calientes de la orilla, alcanzadas antes de que nadie más despierte para alcanzarlas."),
                    ("El día", "Nada, a propósito, interrumpido solo por el almuerzo y quizá un clavado."),
                    ("De noche", "La planta apagada, las lámparas bajas, y más estrellas de las que uno tiene previstas."),
                ],
            },
            {
                "key": "root",
                "name_en": "Root", "name_es": "Raíz",
                "title_en": "Where the country stops speaking Spanish.",
                "title_es": "Donde el país deja de hablar español.",
                "text_en": "Livingston is Garífuna, reachable only by water, and unlike anywhere else in Guatemala.",
                "text_es": "Livingston es garífuna, solo se llega por agua, y no se parece a ningún otro lugar de Guatemala.",
                "beats_en": [
                    ("The morning", "Downriver to Livingston, with the drums audible before the dock is."),
                    ("The day", "Fish cooked in coconut, and an afternoon that takes itself as long as it wants."),
                    ("After dark", "Back up the river in the dark, which is the part people remember."),
                ],
                "beats_es": [
                    ("La mañana", "Río abajo a Livingston, con los tambores oyéndose antes que el muelle."),
                    ("El día", "Pescado en coco, y una tarde que se toma todo el tiempo que quiere."),
                    ("De noche", "De regreso río arriba a oscuras, que es la parte que la gente recuerda."),
                ],
            },
        ],

        "facts_en": [
            ("Getting here", "Four and a half hours by road from the city, or a short flight, then twenty minutes by boat."),
            ("Best months", "January to April, driest and clearest on the water."),
            ("Worth knowing", "There is no road to the door and the phone signal comes and goes. That is the point."),
        ],
        "facts_es": [
            ("Cómo se llega", "Cuatro horas y media por carretera desde la capital, o un vuelo corto, y veinte minutos en lancha."),
            ("Mejores meses", "De enero a abril, los más secos y limpios sobre el agua."),
            ("Conviene saber", "No hay carretera hasta la puerta y la señal va y viene. De eso se trata."),
        ],
    },
    {
        "slug": "tinamit",
        "house_title_en": "The city, from above its own noise.",
        "house_title_es": "La ciudad, por encima de su propio ruido.",
        "test": True,
        "name": "Aldaba Tinamit",
        "destination_slug": "ciudad",
        "place_en": "Guatemala City", "place_es": "Ciudad de Guatemala",
        "image": "img/houses/tinamit-01.jpg",
        "alt_en": "A modern house lit among tall pines at dusk",
        "alt_es": "Una casa moderna encendida entre pinos altos al anochecer",

        "lead_en": "Glass and concrete in a stand of old pines, fifteen minutes from the runway and nowhere near the noise.",
        "lead_es": "Vidrio y concreto en un bosque de pinos viejos, a quince minutos de la pista y lejísimos del ruido.",

        "body_en": [
            "The city is where the flights land and where the country actually eats, and most visitors give it neither a night nor a thought. This house is the argument against that. It sits in the trees above the ravine, and from the top floor you would not know a capital was down there at all.",
            "It is the right house for the first night and the last one. Bags land, the airport is fifteen minutes back down the hill, and somebody else is already driving.",
        ],
        "body_es": [
            "La ciudad es donde aterrizan los vuelos y donde de verdad se come en el país, y casi todos los visitantes no le dan ni una noche ni un pensamiento. Esta casa es el argumento en contra. Está entre los árboles sobre el barranco, y desde el piso de arriba uno no sabría que hay una capital abajo.",
            "Es la casa correcta para la primera noche y la última. Llegan las maletas, el aeropuerto queda quince minutos abajo, y ya hay alguien más manejando.",
        ],

        "stats_en": [("Guests", "6"), ("Bedrooms", "3"), ("Baths", "3"), ("Arrival", "By car")],
        "stats_es": [("Huéspedes", "6"), ("Habitaciones", "3"), ("Baños", "3"), ("Llegada", "En carro")],

        "rooms_en": [
            ("The top floor", "Glass on three sides and pines filling all of it. The city is under there somewhere."),
            ("The long room", "One table, one fireplace, and enough space to arrive at any hour without waking anyone."),
            ("The terrace", "Cold air, tall trees, and the best cup of coffee of the trip taken standing up."),
            ("The kitchen", "Stocked before you land, because the flight always lands later than it should."),
            ("Three rooms", "Quiet, dark, and built for the night before an early flight."),
            ("The house team", "A housekeeper and a driver who has done the airport run a thousand times."),
        ],
        "rooms_es": [
            ("El piso de arriba", "Vidrio por tres lados y pinos llenándolo todo. La ciudad está ahí abajo, en alguna parte."),
            ("El salón largo", "Una mesa, una chimenea, y espacio para llegar a cualquier hora sin despertar a nadie."),
            ("La terraza", "Aire frío, árboles altos, y el mejor café del viaje tomado de pie."),
            ("La cocina", "Surtida antes de que aterrice, porque el vuelo siempre llega más tarde de lo que debería."),
            ("Tres habitaciones", "Calladas, oscuras, y hechas para la noche anterior a un vuelo temprano."),
            ("La casa", "Una camarista y un chofer que ha hecho el viaje al aeropuerto mil veces."),
        ],

        "programmes": [
            {
                "key": "root",
                "name_en": "Root", "name_es": "Raíz",
                "title_en": "The best food in the country is here.",
                "title_es": "La mejor comida del país está aquí.",
                "text_en": "Not the prettiest city on the itinerary. Easily the one that eats best.",
                "text_es": "No es la ciudad más bonita del itinerario. Es, de lejos, la que mejor come.",
                "beats_en": [
                    ("The morning", "Two small museums, textiles and ceramics, both better than they have any right to be."),
                    ("The day", "The market at the hour it is actually working, with somebody who buys there."),
                    ("After dark", "Zona 4 late, at a table held for you, eating what the country cooks for itself."),
                ],
                "beats_es": [
                    ("La mañana", "Dos museos pequeños, textiles y cerámica, los dos mejores de lo que deberían ser."),
                    ("El día", "El mercado a la hora en que de verdad trabaja, con alguien que compra ahí."),
                    ("De noche", "Zona 4 tarde, en una mesa apartada para usted, comiendo lo que el país cocina para sí mismo."),
                ],
            },
            {
                "key": "stillness",
                "name_en": "Stillness", "name_es": "Reposo",
                "title_en": "A soft landing, or a soft exit.",
                "title_es": "Un aterrizaje suave, o una salida suave.",
                "text_en": "For the night the flight got in at eleven, and the morning after the volcano.",
                "text_es": "Para la noche en que el vuelo llegó a las once, y la mañana después del volcán.",
                "beats_en": [
                    ("On arrival", "A driver, a lit house, a made bed, and nothing asked of you until you have slept."),
                    ("The day", "The trees, the terrace, a massage, and a kitchen you did not have to shop for."),
                    ("The way out", "A car at the hour the flight leaves, however unreasonable that hour is."),
                ],
                "beats_es": [
                    ("Al llegar", "Un chofer, una casa encendida, una cama hecha, y nada que se le pida hasta que haya dormido."),
                    ("El día", "Los árboles, la terraza, un masaje, y una cocina que usted no tuvo que surtir."),
                    ("La salida", "Un carro a la hora del vuelo, por poco razonable que sea esa hora."),
                ],
            },
        ],

        "facts_en": [
            ("Getting here", "Fifteen minutes from La Aurora, which sits inside the city."),
            ("Onward", "Fifty minutes to Antigua, three hours to the lake."),
            ("How long", "A night at each end of the trip is enough, and more than most people give it."),
        ],
        "facts_es": [
            ("Cómo se llega", "Quince minutos de La Aurora, que está dentro de la ciudad."),
            ("Hacia dónde sigue", "Cincuenta minutos a Antigua, tres horas al lago."),
            ("Cuánto tiempo", "Una noche a cada extremo del viaje basta, y es más de lo que casi nadie le da."),
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
        title=t(h["house_title_en"], h["house_title_es"]),
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
    return common.footer_html("../") + """
  <script src="../script.js"></script>
</body>
</html>
"""


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

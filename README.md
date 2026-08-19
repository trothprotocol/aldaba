# Aldaba

Guest-facing site for Aldaba, a collection of houses in Guatemala. Plain static
HTML, CSS and one script, no build step for the site itself. Deployed on Vercel.

## Running it locally

    python3 -m http.server 4321 --directory .

## Destination pages

`destinations/*.html` are generated. All of their copy, in both languages,
lives in `build-destinations.py`. Edit that file and run:

    python3 build-destinations.py

Never edit the built pages directly; the next run overwrites them.

## House pages

`houses/*.html` work the same way, from `build-houses.py`:

    python3 build-houses.py

`houses/choq.html` is a test listing. Aldaba does not manage that house, the
photograph is stock, the name carries "(test)" and the page is noindexed.
Delete the entry from `build-houses.py` when it has served its purpose.

No nightly rate appears on a house page. Budget is a field the guest fills in,
never a number we publish, and services are named but never bundled into the
house.

## Languages

English is primary. Both languages live in one document: every translatable
node carries `data-en` and `data-es` (set as innerHTML, so inline markup
travels), plus `data-en-label` / `data-es-label` for aria-labels. The choice
persists in localStorage. The tagline "Well received." stays in English in
both.

## What is deliberately not here

`_private/` is gitignored. It holds the full owner pitch page and the
full-resolution stock originals, and it must not ship. The public site keeps
the owner conversation to one quiet footer link and a noindex page: no rates,
no commissions, no owner economics on any public URL.

## Media

The hero video was transcoded from a 4K original with macOS `avconvert`
(1080p and 720p, with a poster pulled from its own first frame). The 1080p file
is heavier than it should be and is worth re-encoding with ffmpeg before
launch.

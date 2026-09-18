# Ladanta

Guest-facing site for Ladanta, a small collection of private houses in
Guatemala. Plain static HTML, one stylesheet and one script. No build step.
Deployed on Vercel with `cleanUrls`, so links are written without `.html`.

## Pages

    index.html            Home: video hero and search, the rail, promises, experiences, mailing list
    houses/index.html     The collection, filtered by place (?place=antigua|atitlan|rio-dulce|ciudad)
    houses/<slug>.html    One house: sticky frame, image stack, the house, inside, around, practical, enquire
    about.html            The idea, the name, the people behind it, where we are, contact
    experiences/index.html   The three days we arrange, as cards
    experiences/<slug>.html  One day: split opening, the day, what we arrange, houses nearby, elsewhere, ask
    propietarios.html     The private door for owners. noindex, and disallowed in robots.txt

Every page carries the same header, footer and two dialogs. When one of
those changes, change it in every file; there is no template.

## Running it locally

Any static server from the repo root will do, as long as it resolves clean
URLs the way Vercel does (`/about` to `about.html`, `/houses` to
`houses/index.html`). `dev-server.js` is a gitignored local copy that does.

## Houses

The four houses (Ja', Choq', Ki', Tinamit) are working names on placeholder
photography, and their pages are `noindex` until the houses are real. The
fifth card on the rail and in the grid is a "listing soon" plate, not a link.

No nightly rate appears anywhere. Budget is something a guest tells us, never
a number we publish, and services are named but never bundled into the house.

## Forms

There is no backend. The enquiry forms (house pages, about, owners) compose
an email to `hola@ladanta.com` and open the guest's mail client; nothing is
stored. The mailing list form does nothing yet.

## The hero

`index.html` opens on the hiker video (`img/hero-fuego-720.mp4`; the script
swaps in the 1080 file on screens 1280px and wider, and leaves the poster
alone under `prefers-reduced-motion` or Save-Data). The hero slides under the
sticky header by `--header-h`, which the script measures, and the header goes
transparent with light type while it is over the video, then translucent with
a blur once the page has moved.

## Motion

One easing curve (`--ease`) and long durations: image scale on hover 1.6s,
borders 0.4s, header states 0.5s. Sections carry `.reveal` (set by script,
so nothing hides without it) and fade up on an IntersectionObserver. All of
it is switched off under `prefers-reduced-motion`.

## Images

`img/houses/` is the house photography (stock, low resolution, to be
replaced). `img/places/` is cut from the full-resolution originals in
`stock/`, which is gitignored: a 2000px file and a `-1000` file for `srcset`,
JPEG at quality 78, made with `sips`. Cut a new one the same way rather than
committing an original.

## Colour and type

Tokens live at the top of `styles.css`: paper `#F3EFE8` (a warm off-white,
in the Aman register), ink `#272826`, and
two greys for prose and labels that clear WCAG AA on paper. Jade `#35564A`
is a signature, not a palette: the focus ring and the chosen filter's
underline, and nothing else. Adding a third use needs a reason.

Headlines set in a system serif stack (Iowan Old Style, Palatino, Georgia);
everything else is the system sans. Both are one line to change in `:root`.

## What is deliberately not here

`_private/` is gitignored. It holds the business plan, the full owner pitch
and the schema diagrams, and it must not ship. Nothing about commissions,
owner economics or how the business is run appears on any public URL.

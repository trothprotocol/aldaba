/* Prototype only. Dialogs, the collection rail and grid, and the enquiry forms. */

/* Dialogs. Focus moves in on open and back to the trigger on close. */

(function () {
  var lastTrigger = null;

  function open(id, trigger) {
    var overlay = document.getElementById(id);
    if (!overlay) return;
    lastTrigger = trigger || null;
    overlay.hidden = false;
    var first = overlay.querySelector('.dialog__close');
    if (first) first.focus();
  }

  function closeAll() {
    var wasOpen = false;
    document.querySelectorAll('.overlay').forEach(function (overlay) {
      if (!overlay.hidden) wasOpen = true;
      overlay.hidden = true;
    });
    if (wasOpen && lastTrigger) lastTrigger.focus();
    lastTrigger = null;
  }

  document.querySelectorAll('[data-open]').forEach(function (trigger) {
    trigger.addEventListener('click', function () {
      open(trigger.dataset.open, trigger);
    });
  });

  document.querySelectorAll('.overlay').forEach(function (overlay) {
    overlay.addEventListener('click', function (event) {
      if (event.target === overlay || event.target.closest('[data-close]')) {
        closeAll();
      }
    });
  });

  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') closeAll();
  });

  document.querySelectorAll('.choices').forEach(function (group) {
    group.addEventListener('click', function (event) {
      var choice = event.target.closest('.choice');
      if (!choice) return;
      group.querySelectorAll('.choice').forEach(function (other) {
        other.classList.remove('is-selected');
      });
      choice.classList.add('is-selected');
    });
  });
})();

/* Collection rail. Arrows scroll the whole track, intro panel included. */

(function () {
  var rail = document.getElementById('rail');
  if (!rail) return;

  var arrows = document.querySelectorAll('[data-scroll]');
  var animation = null;

  function step() {
    var card = rail.querySelector('.card');
    var gap = parseFloat(getComputedStyle(rail).columnGap) || 0;
    return card ? card.getBoundingClientRect().width + gap : rail.clientWidth * 0.8;
  }

  function sync() {
    var max = rail.scrollWidth - rail.clientWidth;
    var atStart = rail.scrollLeft <= 8;
    var atEnd = rail.scrollLeft >= max - 8;
    arrows.forEach(function (arrow) {
      arrow.disabled = arrow.dataset.scroll === '1' ? atEnd : atStart;
    });
  }

  // Animate by hand. behavior:"smooth" is unreliable next to scroll snapping.
  function glide(to) {
    var from = rail.scrollLeft;
    var max = rail.scrollWidth - rail.clientWidth;
    var target = Math.max(0, Math.min(to, max));
    var startedAt = null;
    var duration = 640;

    if (animation) cancelAnimationFrame(animation);

    function frame(now) {
      if (startedAt === null) startedAt = now;
      var t = Math.min((now - startedAt) / duration, 1);
      var eased = t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
      rail.scrollLeft = from + (target - from) * eased;
      if (t < 1) {
        animation = requestAnimationFrame(frame);
      } else {
        animation = null;
        sync();
      }
    }

    animation = requestAnimationFrame(frame);
  }

  arrows.forEach(function (arrow) {
    arrow.addEventListener('click', function () {
      glide(rail.scrollLeft + step() * Number(arrow.dataset.scroll));
    });
  });

  rail.addEventListener('scroll', sync);
  window.addEventListener('resize', sync);

  // Defeat the browser restoring a scroll position on reload.
  rail.scrollLeft = 0;
  sync();
  window.addEventListener('load', function () {
    rail.scrollLeft = 0;
    sync();
  });
})();

/* Header. Translucent once the page moves, transparent over the video hero,
   and it takes the search from the hero on the way past. */

(function () {
  var header = document.getElementById('header');
  if (!header) return;

  var hero = document.querySelector('.hero');
  var overVideo = !!document.querySelector('.hero--video, .hero--image');

  // The hero slides under the header by this much.
  function measure() {
    if (header.classList.contains('is-compact')) return;
    document.documentElement.style.setProperty('--header-h', header.offsetHeight + 'px');
  }

  function sync() {
    var h = header.offsetHeight;
    var heroBottom = hero ? hero.getBoundingClientRect().bottom : 0;
    header.classList.toggle('is-scrolled', window.scrollY > 8);
    header.classList.toggle('is-over', overVideo && heroBottom > h);
    if (hero) header.classList.toggle('is-compact', heroBottom < h);
  }

  window.addEventListener('scroll', sync, { passive: true });
  window.addEventListener('resize', function () { measure(); sync(); });
  measure();
  sync();
})();

/* Hero. Two video layers take turns through the clips, crossfading a
   second before each one ends. Wide screens get the 1080 files. */

(function () {
  var hero = document.querySelector('.hero--video');
  if (!hero) return;

  var layers = hero.querySelectorAll('.hero__video');
  var clips = [];
  try { clips = JSON.parse(hero.dataset.clips || '[]'); } catch (e) {}

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var saveData = navigator.connection && navigator.connection.saveData;
  var hd = window.innerWidth >= 1280 && !saveData;

  if (reduced || saveData) {
    layers.forEach(function (layer) {
      layer.removeAttribute('autoplay');
      layer.pause();
    });
    return;
  }

  if (clips.length < 2 || layers.length < 2) {
    if (hd && clips[0]) layers[0].src = clips[0].hd;
    var single = layers[0].play();
    if (single && single.catch) single.catch(function () {});
    return;
  }

  var current = 0;
  var index = 0;
  var prepared = false;
  var switching = false;

  function load(layer, clip) {
    layer.poster = clip.poster;
    layer.preload = 'auto';
    layer.src = hd ? clip.hd : clip.sd;
    layer.load();
  }

  function prepare() {
    if (prepared) return;
    prepared = true;
    load(layers[1 - current], clips[(index + 1) % clips.length]);
  }

  function advance() {
    if (switching) return;
    switching = true;
    var from = layers[current];
    var to = layers[1 - current];
    var played = to.play();
    if (!played || !played.then) played = Promise.resolve();
    played.then(function () {
      to.classList.add('is-on');
      from.classList.remove('is-on');
      index = (index + 1) % clips.length;
      current = 1 - current;
      prepared = false;
      switching = false;
      setTimeout(function () { from.pause(); }, 1800);
    }).catch(function () {
      // The next clip would not start; run this one again.
      from.currentTime = 0;
      from.play();
      switching = false;
    });
  }

  layers.forEach(function (layer) {
    layer.removeAttribute('loop');
    layer.addEventListener('timeupdate', function () {
      if (layer !== layers[current] || !layer.duration) return;
      var left = layer.duration - layer.currentTime;
      if (left < 4) prepare();
      if (left < 1.2 && prepared) advance();
    });
    layer.addEventListener('ended', function () {
      if (layer !== layers[current]) return;
      prepare();
      advance();
    });
  });

  load(layers[0], clips[0]);
  layers[0].classList.add('is-on');
  var first = layers[0].play();
  if (first && first.catch) first.catch(function () {});
})();

/* Ambient video elsewhere. Loads when it is in view, pauses when it is not. */

(function () {
  var videos = document.querySelectorAll('video[data-src]');
  if (!videos.length) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (navigator.connection && navigator.connection.saveData) return;

  function start(video) {
    if (!video.src) video.src = video.dataset.src;
    var playing = video.play();
    if (playing && playing.catch) playing.catch(function () {});
  }

  if (!('IntersectionObserver' in window)) {
    videos.forEach(start);
    return;
  }

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) start(entry.target);
      else if (entry.target.src) entry.target.pause();
    });
  }, { rootMargin: '200px 0px' });

  videos.forEach(function (video) { observer.observe(video); });
})();

/* Preferences and the guest profile. Both live in this browser only. */

(function () {
  var store = {
    get: function (key) {
      try { return JSON.parse(localStorage.getItem(key)); } catch (e) { return null; }
    },
    set: function (key, value) {
      try {
        if (value === null) localStorage.removeItem(key);
        else localStorage.setItem(key, JSON.stringify(value));
      } catch (e) {}
    }
  };

  var prefs = store.get('ladanta.prefs') || { language: 'en', currency: 'usd' };
  var labels = { language: { en: 'EN', es: 'ES' }, currency: { usd: '$', gtq: 'Q' } };
  var names = { language: { en: 'English', es: 'Español' }, currency: { usd: 'US dollars', gtq: 'quetzales' } };

  function paintPrefs() {
    document.querySelectorAll('[data-pref-label]').forEach(function (button) {
      var key = button.dataset.prefLabel;
      var value = prefs[key] in labels[key] ? prefs[key] : Object.keys(labels[key])[0];
      button.textContent = button.classList.contains('menu__util')
        ? (key === 'language' ? 'Language' : 'Currency') + ' \u00b7 ' + names[key][value]
        : labels[key][value];
      button.setAttribute('aria-label', (key === 'language' ? 'Language: ' : 'Currency: ') + names[key][value]);
    });
    document.querySelectorAll('.choices[data-group]').forEach(function (group) {
      group.querySelectorAll('.choice').forEach(function (choice) {
        choice.classList.toggle('is-selected', choice.dataset.value === prefs[group.dataset.group]);
      });
    });
  }

  document.querySelectorAll('[data-save-prefs]').forEach(function (button) {
    button.addEventListener('click', function () {
      document.querySelectorAll('.choices[data-group]').forEach(function (group) {
        var chosen = group.querySelector('.choice.is-selected');
        if (chosen) prefs[group.dataset.group] = chosen.dataset.value;
      });
      store.set('ladanta.prefs', prefs);
      paintPrefs();
    });
  });

  paintPrefs();

  var form = document.querySelector('[data-profile]');
  var signed = document.querySelector('[data-signed]');

  function paintProfile() {
    var guest = store.get('ladanta.guest');
    document.querySelectorAll('.util--boxed[data-open="signin"], [data-signin-label]').forEach(function (button) {
      button.textContent = guest ? guest.name.split(' ')[0] : 'Sign in';
    });
    if (form && signed) {
      form.hidden = !!guest;
      signed.hidden = !guest;
      if (guest) {
        signed.querySelector('[data-signed-name]').textContent = guest.name;
        signed.querySelector('[data-signed-email]').textContent = guest.email;
      }
    }
    if (!guest) return;
    document.querySelectorAll('[data-enquire]').forEach(function (enquiry) {
      var name = enquiry.querySelector('input[name="name"]');
      var email = enquiry.querySelector('input[name="email"]');
      if (name && !name.value) name.value = guest.name;
      if (email && !email.value) email.value = guest.email;
    });
  }

  if (form) {
    form.addEventListener('submit', function (event) {
      event.preventDefault();
      store.set('ladanta.guest', { name: form.name.value.trim(), email: form.email.value.trim() });
      paintProfile();
      var close = form.closest('.overlay') && form.closest('.overlay').querySelector('.dialog__close');
      if (close) close.click();
    });
  }

  document.querySelectorAll('[data-forget]').forEach(function (button) {
    button.addEventListener('click', function () {
      store.set('ladanta.guest', null);
      if (form) form.reset();
      paintProfile();
    });
  });

  paintProfile();
})();

/* A search carries its dates and guests through to the enquiry form. */

(function () {
  var params = new URLSearchParams(window.location.search);
  ['from', 'to', 'guests'].forEach(function (key) {
    var value = params.get(key);
    if (!value) return;
    document.querySelectorAll('[data-enquire] [name="' + key + '"]').forEach(function (field) {
      if (!field.value) field.value = value;
    });
  });
})();

/* Reveal. Sections fade up as they arrive. Without the observer nothing is hidden. */

(function () {
  if (!('IntersectionObserver' in window)) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var targets = document.querySelectorAll(
    '.section:not(.section--collection):not(.section--experiences), .section--experiences .section__line, ' +
    '.experience, .collection, .promise, .filters, .grid .card, .house-section, ' +
    '.essay__lede, .essay__intro, .essay__block, .pull, .split, ' +
    '.spread, .duo, .feature, .pair__item, .band__title, .mosaic, .book, .letterpress, .partners-line, .word' + ', ' +
    '.homes__head, .home, .homes__foot, .pillar, .season__text, .season__media, .tiers > .title, .tiers__intro, .tier, .tiers > .cta, ' +
    '.plan__media, .plan__text, .days__head, .day, .twin__col, .word__text, .word__side, .step, .others__grid .card'
  );

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-in');
      observer.unobserve(entry.target);
    });
  }, { rootMargin: '0px 0px -6% 0px', threshold: 0.06 });

  // Cards in a row arrive one after another, 90ms apart.
  var groups = '.home, .pillar, .tier, .day, .twin__col, .step, .others__grid .card';
  targets.forEach(function (el) {
    el.classList.add('reveal');
    if (el.matches(groups)) {
      var index = Array.prototype.indexOf.call(el.parentNode.children, el);
      el.style.transitionDelay = Math.min(index, 4) * 90 + 'ms';
    }
    observer.observe(el);
  });
})();

/* Collection grid. One filter, by place, mirrored into the address bar. */

(function () {
  var grid = document.querySelector('[data-grid]');
  if (!grid) return;

  var filters = document.querySelectorAll('[data-filters] .filter');
  var count = document.querySelector('[data-count]');
  var clear = document.querySelector('[data-clear]');
  var empty = document.querySelector('[data-empty]');
  var cards = grid.querySelectorAll('.card');
  var words = ['No', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'];

  // Everything the search sent along, besides the place, rides through to the house.
  var params = new URLSearchParams(window.location.search);
  var guests = parseInt(params.get('guests'), 10) || 0;
  var carried = new URLSearchParams();
  ['from', 'to', 'guests'].forEach(function (key) {
    if (params.get(key)) carried.set(key, params.get(key));
  });
  var carry = carried.toString();
  if (carry) {
    cards.forEach(function (card) {
      if (card.href) card.href += (card.href.indexOf('?') < 0 ? '?' : '&') + carry;
    });
  }

  function apply(place, pushState) {
    var shown = 0;
    var label = '';

    filters.forEach(function (button) {
      var active = button.dataset.place === place;
      button.setAttribute('aria-pressed', active ? 'true' : 'false');
      if (active && place) label = button.textContent;
    });

    cards.forEach(function (card) {
      var fits = !guests || Number(card.dataset.guests || 0) >= guests;
      var match = (!place || card.dataset.place === place) && fits;
      card.hidden = !match;
      if (match) shown += 1;
    });

    if (count) {
      count.textContent = (words[shown] || shown) + (shown === 1 ? ' home' : ' homes') +
        (label ? ' in ' + label : '') +
        (guests ? ' for ' + (words[guests] ? words[guests].toLowerCase() : guests) : '');
    }
    if (clear) clear.hidden = !carry;
    if (empty) empty.hidden = shown > 0;

    if (pushState && window.history.replaceState) {
      if (place) params.set('place', place); else params.delete('place');
      var query = params.toString();
      window.history.replaceState(null, '', query ? '?' + query : window.location.pathname);
    }
  }

  filters.forEach(function (button) {
    button.addEventListener('click', function () {
      apply(button.dataset.place, true);
    });
  });

  var initial = params.get('place') || '';
  var known = Array.prototype.some.call(filters, function (button) {
    return button.dataset.place === initial;
  });
  apply(known ? initial : '', false);
})();

/* Enquiries. No backend yet: the form writes the email and hands it over. */

(function () {
  var address = 'hello@ladantajourneys.com';

  document.querySelectorAll('[data-enquire]').forEach(function (form) {
    form.addEventListener('submit', function (event) {
      event.preventDefault();

      var lines = [];
      form.querySelectorAll('input, textarea').forEach(function (field) {
        var label = form.querySelector('label[for="' + field.id + '"]');
        var value = field.value.trim();
        if (!value) return;
        lines.push((label ? label.textContent : field.name) + ': ' + value);
      });

      var subject = form.dataset.subject || 'Enquiry';
      var body = lines.join('\n') + '\n\nSent from ladantajourneys.com';
      window.location.href = 'mailto:' + address +
        '?subject=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(body);
    });
  });
})();

/* Once the page moves, the header's utilities fold into a menu on the right. */

(function () {
  var menu = document.getElementById('menu');
  var toggle = document.querySelector('.menu-toggle');
  if (!menu || !toggle) return;
  var panel = menu.querySelector('.menu__panel');

  function open() {
    menu.hidden = false;
    void menu.offsetWidth;
    menu.classList.add('is-open');
    toggle.setAttribute('aria-expanded', 'true');
    document.documentElement.classList.add('is-locked');
    menu.querySelector('.menu__close').focus();
  }

  function close(returnFocus) {
    if (menu.hidden) return;
    menu.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
    document.documentElement.classList.remove('is-locked');
    panel.addEventListener('transitionend', function done() {
      panel.removeEventListener('transitionend', done);
      if (!menu.classList.contains('is-open')) menu.hidden = true;
    });
    if (returnFocus) toggle.focus();
  }

  toggle.addEventListener('click', open);
  menu.addEventListener('click', function (event) {
    if (event.target.closest('[data-menu-close]')) close(true);
    else if (event.target.closest('[data-open], a')) close(false);
  });
  document.addEventListener('keydown', function (event) {
    if (menu.hidden) return;
    if (event.key === 'Escape') close(true);
    if (event.key !== 'Tab') return;
    // Keep focus inside the open panel.
    var stops = panel.querySelectorAll('a[href], button');
    var first = stops[0];
    var last = stops[stops.length - 1];
    if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
    else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
  });
})();

/* Our houses. Four filters over the same four cards; the ones that stay
   visible fade in so the change reads as a change. */

(function () {
  var filters = document.querySelectorAll('.homes__filter');
  var homes = document.querySelectorAll('.home');
  if (!filters.length || !homes.length) return;

  filters.forEach(function (filter) {
    filter.addEventListener('click', function () {
      var key = filter.dataset.filter;
      filters.forEach(function (other) {
        other.setAttribute('aria-pressed', other === filter ? 'true' : 'false');
      });
      homes.forEach(function (home) {
        var show = key === 'all' || (' ' + home.dataset.tags + ' ').indexOf(' ' + key + ' ') > -1;
        home.hidden = !show;
        home.classList.remove('is-entering');
        if (show) {
          void home.offsetWidth;
          home.classList.add('is-entering');
        }
      });
    });
  });
})();

/* Hero dates. The fields read Arriving and Leaving until a date is set,
   open the calendar on a click anywhere in them, and leaving can never
   come before arriving. */

(function () {
  var dates = document.querySelectorAll('.search__date');
  if (!dates.length) return;

  var from = document.getElementById('search-from');
  var to = document.getElementById('search-to');

  function mark(label) {
    var input = label.querySelector('input');
    label.classList.toggle('has-value', !!input.value);
  }

  dates.forEach(function (label) {
    var input = label.querySelector('input');
    input.addEventListener('input', function () { mark(label); });
    input.addEventListener('change', function () { mark(label); });
    label.addEventListener('click', function () {
      if (typeof input.showPicker === 'function') {
        try { input.showPicker(); } catch (e) {}
      }
    });
    mark(label);
  });

  if (from && to) {
    from.addEventListener('change', function () {
      to.min = from.value;
      if (to.value && from.value && to.value < from.value) {
        to.value = '';
        mark(to.closest('.search__date'));
      }
    });
  }
})();

/* Homes map. Pins sit near each home's town, never on the address, and
   follow the filters. Hovering a card lifts its pin and the other way round. */

(function () {
  var el = document.querySelector('[data-map]');
  if (!el || !window.L) return;

  var cards = Array.prototype.filter.call(document.querySelectorAll('[data-grid] .card'), function (card) {
    return card.dataset.lat;
  });

  var map = L.map(el, { scrollWheelZoom: false, zoomControl: true, attributionControl: true });
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 16,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(map);

  var pins = cards.map(function (card) {
    var name = card.querySelector('.card__name').textContent;
    var soon = card.classList.contains('card--soon');
    var icon = L.divIcon({
      className: 'pin' + (soon ? ' pin--soon' : ''),
      html: '<span>' + (soon ? 'Soon' : name) + '</span>',
      iconSize: null
    });
    var marker = L.marker([Number(card.dataset.lat), Number(card.dataset.lng)], { icon: icon, keyboard: false, title: name });
    marker.on('mouseover', function () { card.classList.add('is-hot'); });
    marker.on('mouseout', function () { card.classList.remove('is-hot'); });
    marker.on('click', function () {
      if (card.href) window.location.href = card.href;
      else card.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
    card.addEventListener('mouseenter', function () {
      var node = marker.getElement();
      if (node) node.classList.add('is-hot');
      marker.setZIndexOffset(1000);
    });
    card.addEventListener('mouseleave', function () {
      var node = marker.getElement();
      if (node) node.classList.remove('is-hot');
      marker.setZIndexOffset(0);
    });
    return { card: card, marker: marker };
  });

  function sync() {
    var shown = [];
    pins.forEach(function (pin) {
      if (pin.card.hidden) {
        map.removeLayer(pin.marker);
      } else {
        pin.marker.addTo(map);
        shown.push(pin.marker.getLatLng());
      }
    });
    if (!shown.length) return;
    if (shown.length === 1) map.setView(shown[0], 11);
    else map.fitBounds(L.latLngBounds(shown), { padding: [48, 48], maxZoom: 11 });
  }

  var observer = new MutationObserver(sync);
  cards.forEach(function (card) { observer.observe(card, { attributes: true, attributeFilter: ['hidden'] }); });
  sync();
  window.addEventListener('resize', function () { map.invalidateSize(); });
})();

/* Home pages. The booking box takes dates from the search, hands them to
   the enquiry form, and a slim bar keeps the way to it in reach. */

(function () {
  var book = document.querySelector('[data-book]');
  if (!book) return;

  var params = new URLSearchParams(window.location.search);
  ['from', 'to', 'guests'].forEach(function (key) {
    var field = book.querySelector('[name="' + key + '"]');
    if (field && params.get(key)) field.value = params.get(key);
  });

  var from = book.querySelector('[name="from"]');
  var to = book.querySelector('[name="to"]');
  from.addEventListener('change', function () {
    to.min = from.value;
    if (to.value && to.value < from.value) to.value = '';
  });

  book.addEventListener('submit', function (event) {
    event.preventDefault();
    ['from', 'to', 'guests'].forEach(function (key) {
      var source = book.querySelector('[name="' + key + '"]');
      var target = document.getElementById('enq-' + key);
      if (source && target && source.value) target.value = source.value;
    });
    var enquire = document.getElementById('enquire');
    if (enquire) {
      enquire.scrollIntoView({ behavior: 'smooth', block: 'start' });
      var name = document.getElementById('enq-name');
      if (name) setTimeout(function () { name.focus({ preventScroll: true }); }, 500);
    }
  });

  var bar = document.querySelector('[data-bookbar]');
  var enquire = document.getElementById('enquire');
  if (!bar) return;

  function update() {
    var gone = book.getBoundingClientRect().bottom < 0;
    var reached = enquire ? enquire.getBoundingClientRect().top < window.innerHeight * 0.85 : false;
    var show = gone && !reached;
    bar.hidden = !show;
    document.documentElement.classList.toggle('has-bookbar', show);
  }

  window.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', update);
  update();
})();

/* One pin on a small map, near the home but never on it. */

(function () {
  var el = document.querySelector('[data-map-point]');
  if (!el || !window.L) return;
  var point = [Number(el.dataset.lat), Number(el.dataset.lng)];
  var map = L.map(el, { scrollWheelZoom: false, dragging: !L.Browser.mobile, attributionControl: true }).setView(point, 12);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 14,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(map);
  L.circle(point, { radius: 900, color: '#944636', weight: 1, fillColor: '#944636', fillOpacity: 0.12 }).addTo(map);
  L.marker(point, {
    icon: L.divIcon({ className: 'pin', html: '<span>' + el.dataset.label + '</span>', iconSize: null }),
    keyboard: false,
    interactive: false
  }).addTo(map);
})();

/* The privacy note shows once. Either button closes it for good. */

(function () {
  var box = document.querySelector('[data-consent]');
  if (!box) return;
  var key = 'ladanta.consent';
  var seen = null;
  try { seen = localStorage.getItem(key); } catch (e) {}
  if (seen) return;
  box.hidden = false;
  box.querySelectorAll('[data-consent-close]').forEach(function (button) {
    button.addEventListener('click', function () {
      try { localStorage.setItem(key, button.textContent.trim().toLowerCase()); } catch (e) {}
      box.classList.add('is-leaving');
      setTimeout(function () { box.hidden = true; }, 200);
    });
  });
})();

/* Prototype only. Dialogs, the header, the films, and the enquiry forms. */

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

/* Header. Translucent once the page moves, transparent over the video hero,
   and it takes the search from the hero on the way past. */

(function () {
  var header = document.getElementById('header');
  if (!header) return;

  var hero = document.querySelector('.hero, .about-hero, .homes--film');
  var overVideo = !!document.querySelector('.hero--video, .hero--image, .about-hero, .homes--film');

  // The hero slides under the header by this much.
  function measure() {
    if (header.classList.contains('is-compact')) return;
    document.documentElement.style.setProperty('--header-h', header.offsetHeight + 'px');
  }

  function sync() {
    var h = header.offsetHeight;
    var heroBottom = hero ? hero.getBoundingClientRect().bottom : 0;
    document.documentElement.style.setProperty('--header-now', h + 'px');
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

  // The poster is already on screen. A very slow or metered connection
  // keeps it, and so does anyone who has asked for less motion. A middling
  // one gets the small files, still all three in turn.
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var connection = navigator.connection || {};
  var type = connection.effectiveType || '';
  var slow = connection.saveData || /2g$/.test(type);
  var modest = type === '3g';
  // Every screen gets the 1080 files; quality is not traded for size.
  var hd = true;

  if (reduced || slow || !clips.length) {
    layers.forEach(function (layer) { layer.removeAttribute('autoplay'); });
    return;
  }

  if (clips.length < 2 || layers.length < 2) {
    layers[0].src = hd ? clips[0].hd : clips[0].sd;
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
      // Fetch the next clip early so it is ready when this one ends.
      if (layer.currentTime > 1) prepare();
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

/* Pictures arrive softly. A lazy picture that is not ready yet waits on its
   frame's colour and fades in when it lands; cached ones show at once. */

(function () {
  document.querySelectorAll('img[loading="lazy"]').forEach(function (img) {
    if (img.complete || img.matches('.split__inset, .split__main')) return;
    img.classList.add('is-loading');
    function arrive() {
      img.classList.remove('is-loading');
      img.classList.add('is-arriving');
    }
    img.addEventListener('load', arrive, { once: true });
    img.addEventListener('error', arrive, { once: true });
  });
})();

/* Ambient video elsewhere. Loads when it is in view, pauses when it is not. */

(function () {
  var videos = document.querySelectorAll('video[data-src]');
  if (!videos.length) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var connection = navigator.connection || {};
  if (connection.saveData || /2g$/.test(connection.effectiveType || '')) return;
  var small = window.matchMedia('(max-width: 800px)').matches || connection.effectiveType === '3g';

  function start(video) {
    if (!video.src) video.src = (small && video.dataset.srcSd) || video.dataset.src;
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
    '.plan__media, .plan__text, .days__head, .day, .twin__col, .word__text, .word__side, .step, .others__grid .card' + ', ' +
    '.journey-feature, .soon-card, .soon-plate, .trip-intro, .trip-notes__grid > div'
  );

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-in');
      observer.unobserve(entry.target);
    });
  }, { rootMargin: '0px 0px -6% 0px', threshold: 0.06 });

  // Cards in a row arrive one after another, 90ms apart.
  var groups = '.home, .pillar, .tier, .day, .twin__col, .step, .others__grid .card, .soon-card, .trip-notes__grid > div';
  targets.forEach(function (el) {
    el.classList.add('reveal');
    if (el.matches(groups)) {
      var index = Array.prototype.indexOf.call(el.parentNode.children, el);
      el.style.transitionDelay = Math.min(index, 4) * 90 + 'ms';
    }
    observer.observe(el);
  });
})();

/* A search that lands before any home is listed becomes a note to us,
   with the place, the dates and the party already written in. */

(function () {
  var plate = document.querySelector('[data-soon]');
  if (!plate) return;

  var params = new URLSearchParams(window.location.search);
  var places = { antigua: 'Antigua', atitlan: 'Lake Atitlán', 'rio-dulce': 'Río Dulce', ciudad: 'Guatemala City' };
  var place = places[params.get('place')] || '';
  var from = params.get('from');
  var to = params.get('to');
  var guests = parseInt(params.get('guests'), 10) || 0;
  if (!place && !from && !to && !guests) return;

  function day(value) {
    var date = new Date(value + 'T12:00:00');
    return isNaN(date) ? '' : date.toLocaleDateString('en-GB', { day: 'numeric', month: 'long' });
  }

  var parts = [];
  if (place) parts.push(place);
  if (day(from) && day(to)) parts.push(day(from) + ' to ' + day(to));
  else if (day(from)) parts.push('from ' + day(from));
  if (guests) parts.push(guests + (guests === 1 ? ' guest' : ' guests'));
  if (!parts.length) return;
  var summary = parts.join(', ');

  var note = document.createElement('p');
  note.className = 'soon-plate__search';
  note.textContent = 'You searched for ' + summary + '. Nothing is listed yet, but we can still arrange the stay.';
  plate.querySelector('.soon-plate__text').insertAdjacentElement('afterend', note);

  var send = document.createElement('a');
  send.className = 'cta';
  send.href = 'mailto:hello@ladantajourneys.com?subject=' + encodeURIComponent('A stay: ' + summary) +
    '&body=' + encodeURIComponent('Hello,\n\nWe are looking at ' + summary + '. What could you arrange?\n');
  send.textContent = 'Send us these dates';

  var actions = plate.querySelector('.soon-plate__actions');
  var hear = actions.querySelector('.cta');
  hear.className = 'more';
  hear.textContent = 'Or hear first';
  actions.querySelectorAll('.more').forEach(function (link) { if (link !== hear) link.remove(); });
  actions.insertBefore(send, actions.firstChild);
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
    // Hide it once the panel has slid away. The timer covers the case where
    // no transition runs, so a closed menu can never sit over the page.
    function done() {
      panel.removeEventListener('transitionend', done);
      clearTimeout(fallback);
      if (!menu.classList.contains('is-open')) menu.hidden = true;
    }
    var fallback = setTimeout(done, 500);
    panel.addEventListener('transitionend', done);
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

/* Journey route. As each day reaches the middle of the screen, the map
   flies to it and draws that day's part of the line. Earlier days stay
   drawn; later ones wait. A faint dotted line shows the whole way. */

(function () {
  var el = document.querySelector('[data-route-map]');
  var source = document.getElementById('route-data');
  if (!el || !source || !window.L) return;

  var data;
  try { data = JSON.parse(source.textContent); } catch (e) { return; }
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var steps = document.querySelectorAll('.route-day');

  var map = L.map(el, {
    scrollWheelZoom: false,
    zoomSnap: 0.25,
    zoomControl: true,
    attributionControl: true
  });
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 15,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(map);

  var everything = [];
  data.days.forEach(function (day) {
    day.legs.forEach(function (leg) {
      everything = everything.concat(leg.points);
      L.polyline(leg.points, { className: 'leg leg--ghost', interactive: false }).addTo(map);
    });
  });
  map.fitBounds(L.latLngBounds(everything), { padding: [40, 40] });

  data.stops.forEach(function (stop) {
    L.marker([stop.lat, stop.lng], {
      icon: L.divIcon({
        className: 'pin' + (stop.kind ? ' pin--' + stop.kind : ''),
        html: '<span>' + stop.name + '</span>',
        iconSize: null
      }),
      keyboard: false,
      interactive: false
    }).addTo(map);
  });

  var lines = data.days.map(function (day) {
    return day.legs.map(function (leg) {
      return L.polyline(leg.points, { className: 'leg leg--' + leg.mode, interactive: false });
    });
  });

  function draw(line, animate) {
    if (map.hasLayer(line)) return;
    line.addTo(map);
    var path = line.getElement && line.getElement();
    if (!path || !animate || reduced) return;
    var dashed = /leg--(boat|home)/.test(path.getAttribute('class'));
    if (dashed) {
      path.style.opacity = '0';
      path.getBoundingClientRect();
      path.style.transition = 'opacity 0.8s ease-out';
      path.style.opacity = '';
      return;
    }
    var length = path.getTotalLength();
    path.style.transition = 'none';
    path.style.strokeDasharray = length + ' ' + length;
    path.style.strokeDashoffset = String(length);
    path.getBoundingClientRect();
    path.style.transition = 'stroke-dashoffset 1.6s cubic-bezier(0.23, 1, 0.32, 1)';
    path.style.strokeDashoffset = '0';
    // Once drawn, let the line behave normally when the map zooms.
    setTimeout(function () {
      path.style.transition = '';
      path.style.strokeDasharray = '';
      path.style.strokeDashoffset = '';
    }, 1700);
  }

  var current = -1;
  function go(index) {
    if (index === current) return;
    current = index;

    steps.forEach(function (step) {
      step.classList.toggle('is-active', Number(step.dataset.day) === index);
    });

    lines.forEach(function (legs, i) {
      legs.forEach(function (line) {
        if (i < index) draw(line, false);
        if (i > index && map.hasLayer(line)) map.removeLayer(line);
      });
    });

    var day = data.days[index];
    var bounds = L.latLngBounds(day.view);
    var options = { padding: [56, 56], maxZoom: day.zoom || 12 };
    var done = false;
    function reveal() {
      if (done || current !== index) return;
      done = true;
      lines[index].forEach(function (line, n) {
        setTimeout(function () { if (current === index) draw(line, true); }, n * 500);
      });
    }

    if (reduced) {
      map.fitBounds(bounds, options);
      reveal();
      return;
    }
    map.once('moveend', reveal);
    setTimeout(reveal, 1500);
    options.duration = 1.1;
    map.flyToBounds(bounds, options);
  }

  // The day whose box crosses the middle of the screen is the day on the map.
  function pick() {
    var middle = window.innerHeight / 2;
    var chosen = -1;
    steps.forEach(function (step) {
      var box = step.getBoundingClientRect();
      if (box.top <= middle && box.bottom >= middle) chosen = Number(step.dataset.day);
    });
    if (chosen < 0) {
      var first = steps[0] && steps[0].getBoundingClientRect();
      if (first && first.top > middle) return;
      chosen = steps.length - 1;
    }
    go(chosen);
  }

  window.addEventListener('scroll', pick, { passive: true });
  window.addEventListener('resize', pick);
  pick();

  window.addEventListener('resize', function () { map.invalidateSize(); });
})();

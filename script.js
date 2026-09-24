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
    return card ? card.getBoundingClientRect().width + 24 : rail.clientWidth * 0.8;
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
  var overVideo = !!document.querySelector('.hero--video');

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
      button.textContent = labels[key][value];
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
    document.querySelectorAll('.util--boxed[data-open="signin"]').forEach(function (button) {
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
    '.spread, .duo, .feature, .pair__item, .band__title, .mosaic, .book, .letterpress, .partners-line, .word'
  );

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-in');
      observer.unobserve(entry.target);
    });
  }, { rootMargin: '0px 0px -6% 0px', threshold: 0.06 });

  targets.forEach(function (el) {
    el.classList.add('reveal');
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
      count.textContent = (words[shown] || shown) + (shown === 1 ? ' house' : ' houses') +
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
  var address = 'hola@ladantajourneys.com';

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

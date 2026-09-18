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
    var duration = 420;

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

/* Header. The hero search hands its job to the header on the way past. */

(function () {
  var header = document.getElementById('header');
  var heroSearch = document.querySelector('.hero .search');
  if (!header || !heroSearch) return;

  function sync() {
    var passed = heroSearch.getBoundingClientRect().bottom < header.offsetHeight;
    header.classList.toggle('is-compact', passed);
  }

  window.addEventListener('scroll', sync, { passive: true });
  window.addEventListener('resize', sync);
  sync();
})();

/* Collection grid. One filter, by place, mirrored into the address bar. */

(function () {
  var grid = document.querySelector('[data-grid]');
  if (!grid) return;

  var filters = document.querySelectorAll('[data-filters] .filter');
  var count = document.querySelector('[data-count]');
  var empty = document.querySelector('[data-empty]');
  var cards = grid.querySelectorAll('.card');
  var words = ['No', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'];

  function apply(place, pushState) {
    var shown = 0;
    var label = '';

    filters.forEach(function (button) {
      var active = button.dataset.place === place;
      button.setAttribute('aria-pressed', active ? 'true' : 'false');
      if (active && place) label = button.textContent;
    });

    cards.forEach(function (card) {
      var match = !place || card.dataset.place === place;
      card.hidden = !match;
      if (match) shown += 1;
    });

    if (count) {
      count.textContent = (words[shown] || shown) + (shown === 1 ? ' house' : ' houses') + (label ? ' in ' + label : '');
    }
    if (empty) empty.hidden = shown > 0;

    if (pushState && window.history.replaceState) {
      var url = place ? '?place=' + place : window.location.pathname;
      window.history.replaceState(null, '', url);
    }
  }

  filters.forEach(function (button) {
    button.addEventListener('click', function () {
      apply(button.dataset.place, true);
    });
  });

  var initial = new URLSearchParams(window.location.search).get('place') || '';
  var known = Array.prototype.some.call(filters, function (button) {
    return button.dataset.place === initial;
  });
  apply(known ? initial : '', false);
})();

/* Enquiries. No backend yet: the form writes the email and hands it over. */

(function () {
  var address = 'hola@ladanta.com';

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
      var body = lines.join('\n') + '\n\nSent from ladanta.com';
      window.location.href = 'mailto:' + address +
        '?subject=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(body);
    });
  });
})();

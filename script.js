/* Prototype only. Opens and closes the dialogs, tracks the selected choice. */

document.querySelectorAll('[data-open]').forEach(function (trigger) {
  trigger.addEventListener('click', function () {
    var dialog = document.getElementById(trigger.dataset.open);
    if (dialog) dialog.hidden = false;
  });
});

document.querySelectorAll('.overlay').forEach(function (overlay) {
  overlay.addEventListener('click', function (event) {
    if (event.target === overlay || event.target.closest('[data-close]')) {
      overlay.hidden = true;
    }
  });
});

document.addEventListener('keydown', function (event) {
  if (event.key !== 'Escape') return;
  document.querySelectorAll('.overlay').forEach(function (overlay) {
    overlay.hidden = true;
  });
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

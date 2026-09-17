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

  function step() {
    var card = rail.querySelector('.card');
    return card ? card.getBoundingClientRect().width + 24 : rail.clientWidth * 0.8;
  }

  function sync() {
    var atStart = rail.scrollLeft <= 1;
    var atEnd = rail.scrollLeft + rail.clientWidth >= rail.scrollWidth - 1;
    arrows.forEach(function (arrow) {
      var forward = arrow.dataset.scroll === '1';
      arrow.disabled = forward ? atEnd : atStart;
    });
  }

  arrows.forEach(function (arrow) {
    arrow.addEventListener('click', function () {
      rail.scrollBy({ left: step() * Number(arrow.dataset.scroll), behavior: 'smooth' });
    });
  });

  rail.addEventListener('scroll', sync);
  window.addEventListener('resize', sync);
  sync();
})();

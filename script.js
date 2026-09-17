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

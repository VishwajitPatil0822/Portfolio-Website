document.addEventListener('DOMContentLoaded', () => {
  const popup = document.getElementById('popupBox');
  const popupOverlay = document.getElementById('popupOverlay');

  const shouldShowPopup = popup?.dataset.show;

  if (shouldShowPopup === "true") {
    popup.style.display = 'flex';
    popupOverlay.style.display = 'block'; // Show backdrop
  }

  window.closePopup = function () {
    popup.style.display = 'none';
    popupOverlay.style.display = 'none'; // Hide backdrop
  };
});

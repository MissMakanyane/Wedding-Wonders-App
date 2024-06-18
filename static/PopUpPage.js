document.addEventListener("DOMContentLoaded", function() {
    var popupOverlay = document.getElementById("popup-overlay");
    var closePopupButton = document.getElementById("close-popup");
  
    // Show the popup
    popupOverlay.style.opacity = "1";
    popupOverlay.style.visibility = "visible";
  
    // Close the popup when the button is clicked
    closePopupButton.addEventListener("click", function() {
      popupOverlay.style.opacity = "0";
      popupOverlay.style.visibility = "hidden";
    });
  });
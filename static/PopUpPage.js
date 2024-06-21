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


 
      document.addEventListener("DOMContentLoaded", function() {
        const stars = document.querySelectorAll('.star');
        let rating = 0;
  
        stars.forEach((star, index) => {
          star.addEventListener('click', () => {
            rating = index + 1;
            stars.forEach((s, i) => {
              if (i < rating) {
                s.classList.add('active');
              } else {
                s.classList.remove('active');
              }
            });
            document.getElementById('rating-value').value = rating;
            console.log("Rating:", document.getElementById('rating-value').value);
          });
        });
  
        document.getElementById('submit-review').addEventListener('click', async (event) => {
          event.preventDefault();
          const form = document.getElementById('inquiry-form');
          const formData = new FormData(form);
  
          try {
            const response = await fetch(form.action, {
              method: form.method,
              body: formData
            });
  
            if (response.ok) {
              document.getElementById('popup').style.display = 'block';
            } else {
              alert('Failed to submit review');
            }
          } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while submitting the review');
          }
        });
  
        document.getElementById('close-popup').addEventListener('click', function() {
          document.getElementById('popup').style.display = 'none';
          window.location.href = "/review_display";
        });
      });
  

   


function goToHaircutReview(action) {
    // Implement navigation logic if needed
    // Example: window.location.href = '/haircut_review';
}

function delete_display() {
    // Implement delete confirmation logic if needed
    return confirm('Are you sure you want to delete this review?');
}

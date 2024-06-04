// Get all the service divs
const serviceDivs = document.querySelectorAll('.service');

// Add click event listener to each service div
serviceDivs.forEach(serviceDiv => {
  serviceDiv.addEventListener('click', () => {
    // Get the form within the clicked service div
    const form = serviceDiv.querySelector('form');

    // Submit the form
    form.submit();
  });
});
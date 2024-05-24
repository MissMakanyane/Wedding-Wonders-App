document.getElementById('registration-form').addEventListener('submit', function(event) {
    event.preventDefault();
  
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirm-password').value;
    var termsChecked = document.getElementById('terms').checked;
  
    var errorMessage = '';
  
    if (name.trim() === '') {
      errorMessage += 'Please enter your name.<br>';
    }
  
    if (!isValidEmail(email)) {
      errorMessage += 'Please enter a valid email address.<br>';
    }
  
    if (password.length < 8) {
      errorMessage += 'Password must be at least 8 characters long.<br>';
    }
  
    if (password !== confirmPassword) {
      errorMessage += 'Passwords do not match.<br>';
    }
  
    if (!termsChecked) {
      errorMessage += 'You must agree to the terms and conditions.<br>';
    }
  
    if (errorMessage !== '') {
      document.getElementById('error-message').innerHTML = errorMessage;
    } else {
      // Handle successful registration, e.g., redirect to a success page
      alert('Registration successful!');
    }
  });
  
  function isValidEmail(email) {
    // Basic email validation
    return /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email);
  }
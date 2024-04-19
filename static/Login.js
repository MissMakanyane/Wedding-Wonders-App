

function validateForm() {
    var username = document.getElementById('username').value;
    // var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    // var confirmPassword = document.getElementById('confirm-password').value;
  
    // Basic validation
    if (username.trim()  === '' || password.trim() === '' ) {
      alert('All fields are required');
      return false;
    }

    // Validate password format (at least one letter, one number, and one special character)
    var passwordPattern = /^(?=.[a-zA-Z])(?=.\d)(?=.[@$!%?&])[A-Za-z\d@$!%*?&]{10,}$/;
    if (!passwordPattern.test(password)) {
      alert('Password must contain at least 10 characters, including at least one letter, one number, and one special character.');
      return false;
    }
  
    if (password !== confirmPassword) {
      alert('Passwords do not match');
      return false;
    }
  
    // Additional validation logic can be added here (e.g., password strength, email format)
  
    // Form is valid
    return true;
  }
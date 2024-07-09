function isValidPassword(password) {
  // Password must be at least 8 characters long
  if (password.length < 8) {
      return false;
  }
  // Password must contain at least one number, one letter, and one symbol
  var hasNumber = /\d/.test(password);
  var hasLetter = /[a-zA-Z]/.test(password);
  var hasSymbol = /[!@#$%^&*()_+-=[]{};':"\|,.<>/?]/.test(password);
  return hasNumber && hasLetter && hasSymbol;
}
document.addEventListener("DOMContentLoaded", function() {
  document.getElementById("signup-form").addEventListener("submit", function(event) {
      event.preventDefault(); // Prevent form submission

      // Validate password
      var password = document.getElementById("password").value;
      if (!isValidPassword(password)) {
          alert("Password must be at least 8 characters long and contain at least one number, one letter, and one symbol.");
          return;
      }

      // If password is valid, proceed with sign up logic
      // Your sign up logic here
      alert("Sign up successful!");
  });
});

function isValidPassword(password) {
  // Password must be at least 8 characters long
  if (password.length < 8) {
      return false;
  }
  // Password must contain at least one number, one letter, and one symbol
  var hasNumber = /\d/.test(password);
  var hasLetter = /[a-zA-Z]/.test(password);
  var hasSymbol = /[!@#$%^&*()_+-=[]{};':"\|,.<>/?]/.test(password);
  return hasNumber && hasLetter && hasSymbol;
}





// function validateForm() {
//     var username = document.getElementById('username').value;
//     var email = document.getElementById('email').value;
//     var password = document.getElementById('password').value;
//     var confirmPassword = document.getElementById('confirm-password').value;
  
//     // Basic validation
//     if (username.trim() === '' || email.trim() === '' || password.trim() === '' || confirmPassword.trim() === '') {
//       alert('All fields are required');
//       return false;
//     }

//     // Validate password format (at least one letter, one number, and one special character)
//     var passwordPattern = /^(?=.[a-zA-Z])(?=.\d)(?=.[@$!%?&])[A-Za-z\d@$!%*?&]{10,}$/;
//     if (!passwordPattern.test(password)) {
//       alert('Password must contain at least 10 characters, including at least one letter, one number, and one special character.');
//       return false;
//     }
  
//     if (password !== confirmPassword) {
//       alert('Passwords do not match');
//       return false;
//     }
  
//     // Additional validation logic can be added here (e.g., password strength, email format)
  
//     // Form is valid
//     return true;
//   }
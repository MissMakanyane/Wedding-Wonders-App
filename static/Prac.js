var languageForm = document.getElementById("language-form");
var languageInput = document.getElementById("language-input");
var languageList = document.getElementById("language-list");

languageForm.addEventListener("submit", function(event) {
    event.preventDefault();

    var languageName = languageInput.value.trim();

    if (languageName) {
        var listItem = document.createElement("li");
        var languageSpan = document.createElement("span");
        languageSpan.textContent = languageName;
        listItem.appendChild(languageSpan);

        var updateButton = document.createElement("button");
        updateButton.textContent = "Update";
        updateButton.addEventListener("click", function() {
            var newLanguageName = prompt("Enter new language name:", languageName);

            if (newLanguageName) {
                languageSpan.textContent = newLanguageName;
            }
        });
        listItem.appendChild(updateButton);

        var deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.addEventListener("click", function() {
            listItem.parentNode.removeChild(listItem);
        });
        listItem.appendChild(deleteButton);

        languageList.appendChild(listItem);

        languageInput.value = "";
    }
})
function gotoLandingPage1() {
    
    window.location.href = "http://127.0.0.1:5000/Rings";
  }


  function gotoLandingPage2() {
    
    window.location.href = "http://127.0.0.1:5000/Suits";
  }


  function gotoLandingPage3() {
    s
    window.location.href = "http://127.0.0.1:5000/TraditionalAttires";
  }


  function gotoLandingPage4() {
    
    window.location.href = "http://127.0.0.1:5000/Gown";
  }


  function gotoLandingPage6() {
    
    window.location.href = "http://127.0.0.1:5000/Display_Services";
  }


  function updateCartCount(count) {
    const cartCount = document.querySelector('#cartCount');
    cartCount.textContent = count;
}

let cartCount = 0;

function addToCart() {
    cartCount++;
    updateCartCount(cartCount);
}

function updateCartCount(count) {
    document.getElementById('cartCount').innerText = count;
}


function incrementValue(e) {
  e.preventDefault();
  var fieldName = $(e.target).data('field');
  var parent = $(e.target).closest('div');
  var currentVal = parseInt(parent.find('input[name=' + fieldName + ']').val(), 10);

  if (!isNaN(currentVal)) {
      parent.find('input[name=' + fieldName + ']').val(currentVal + 1);
  } else {
      parent.find('input[name=' + fieldName + ']').val(0);
  }
}

function decrementValue(e) {
  e.preventDefault();
  var fieldName = $(e.target).data('field');
  var parent = $(e.target).closest('div');
  var currentVal = parseInt(parent.find('input[name=' + fieldName + ']').val(), 10);

  if (!isNaN(currentVal) && currentVal > 0) {
      parent.find('input[name=' + fieldName + ']').val(currentVal - 1);
  } else {
      parent.find('input[name=' + fieldName + ']').val(0);
  }
}

$('.input-group').on('click', '.button-plus', function(e) {
  incrementValue(e);
});

$('.input-group').on('click', '.button-minus', function(e) {
  decrementValue(e);
});




  function decreaseQuantity(itemId) {
  var quantityElement = document.getElementById(`quantity-${itemId}`);
    var currentQuantity = parseInt(quantityElement.textContent);

    if (currentQuantity > 1) {
      quantityElement.textContent = currentQuantity - 1;
      updateCart(itemId, currentQuantity - 1);
    }
  }

  function increaseQuantity(itemId) {
    var quantityElement = document.getElementById(`quantity-${itemId}`);
    var currentQuantity = parseInt(quantityElement.textContent);
    quantityElement.textContent = currentQuantity + 1;
    updateCart(itemId, currentQuantity + 1);
  }

  function updateCart(itemId, newQuantity) {
    // Code to update the cart with the new quantity goes here
    // This could involve making an AJAX request to the server or updating the cart state in the client-side application
    console.log(`Item ${itemId} quantity updated to ${newQuantity}`);
  }



  // Assume session is an object that holds the cart items
// and `session.get('cart')` returns an array of items in the cart

let items = session.get('cart') || []; // Initialize items with cart items or an empty array

// Example new item to add to cart
let newItem = { id: 'your_item_id', quantity: 1 }; // Replace 'your_item_id' with actual item id

let itemFound = false;

// Loop through each item in the cart
for (let i = 0; i < items.length; i++) {
    let item = items[i];
    
    // Check if the item id matches the new item id
    if (item.id === newItem.id) {
        // If item already exists in cart, increase the quantity
        item.quantity++;
        itemFound = true;
        break;
    }
}

// If item was not found in cart, add it to the cart
if (!itemFound) {
    items.push(newItem);
}

// Update session variable with modified cart
session['cart'] = items;





// Assuming you have a function to retrieve the cart from the session
function getCart() {
  return JSON.parse(sessionStorage.getItem('cart')) || [];
}

// Assuming you have a function to update the cart in the session
function updateCart(cart) {
  sessionStorage.setItem('cart', JSON.stringify(cart));
}

// Function to add or update an item in the cart
function addToCart(item) {
  const cart = getCart();
  let found = false;

  for (let i = 0; i < cart.length; i++) {
    if (cart[i].id === item.id) {
      cart[i].quantity++;
      found = true;
      break;
    }
  }

  if (!found) {
    cart.push(item);
  }

  updateCart(cart);
}


// Assume session is an object that holds the cart items
// and `session.get('cart')` returns an array of items in the cart

letitems = session.get('cart') || []; // Initialize items with cart items or an empty array

// Function to update item quantity in the cart
function updateCartItemQuantity(itemId, newQuantity) {
    // Find the item in the cart by its id
    let itemIndex = items.findIndex(item => item.id === itemId);

    if (itemIndex !== -1) {
        // If item exists in cart, update its quantity
        if (newQuantity > 0) {
            // Increase quantity
            items[itemIndex].quantity = newQuantity;
        } else {
            // Remove item if quantity is zero or less (optional)
            items.splice(itemIndex, 1);
        }
    } else {
        // If item does not exist in cart (optional scenario handling)
        if (newQuantity > 0) {
            items.push({ id: itemId, quantity: newQuantity });
        }
    }

    // Update session variable with modified cart
    session['cart'] = items;
}

// Example usage to increase or decrease quantity of an item
let itemIdToUpdate = 'your_item_id'; // Replace with actual item id
let newQuantity = 5; // Replace with desired new quantity (can be increased or decreased)

// Call the function to update cart item quantity
updateCartItemQuantity(itemIdToUpdate, newQuantity);


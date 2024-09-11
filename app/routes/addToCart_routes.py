from flask import Blueprint
from ..controllers import addToCart_controllers

app = Blueprint ('cart',__name__)


app.route("/About")(addToCart_controllers.About)

app.route('/AddToCart', methods=['POST'])(addToCart_controllers.add_to_cart)

app.route('/ViewCart')(addToCart_controllers.cart)

app.route('/cart/remove', methods=['POST'])(addToCart_controllers.remove_from_cart)

app.route('/cart/checkout-success', methods=['POST'])(addToCart_controllers.checkout_success)

app.route('/checkout')(addToCart_controllers.checkout)

app.route('/cart/update_quantity', methods=['POST'])(addToCart_controllers.update_cart)

app.route('/client-checkout')(addToCart_controllers.usercheckout)

app.route('/payment-successful')(addToCart_controllers.success)

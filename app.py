from flask import Flask, url_for, redirect, Response, request, render_template,session, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os
from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path='/static')
app.config["MONGO_URI"] = "mongodb://localhost:27017/WeddingWonders"
app.config['SECRET_KEY'] = 'your_secret_key' 
mongo = PyMongo(app)
db = mongo.db

UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# LANDING
@app.route("/")
def landing():
    return render_template("Access.html")

# AAA
@app.route("/aaa")
def aaa():
    return render_template("aaa.html")


# SIGN UP
@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        user = {"name": name, "email": email, "password": password}
        if db.user.insert_one(user):
            return redirect(url_for("login"))
    return render_template("SignUp.html")

# LOGIN
@app.route("/Login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]

        user = {"name": name, "password": password}
        if db.user.find_one(user):
            return render_template("Add_Services.html")

    return render_template("Login.html")

# ABOUT
@app.route("/About")
def About():
    return render_template("About.html")

# RINGS
@app.route("/Rings")
def Rings():
    return render_template("Rings.html")

# Traditional Attires
@app.route("/TraditionalAttires")
def Traditional_Attires():
    return render_template("TraditionalAttires.html")

# SUITS
@app.route("/Suits")
def Suits():
    return render_template("Suits.html")

# Add_service
@app.route('/Add_Services', methods=["POST", "GET"])
def Add_Services():
    if request.method == 'POST':
        categories = request.form.get("categories")
        price = request.form.get("price")
        colour = request.form.get("colour")
        description = request.form.get("description")
        image_file = request.files.get("image_url")
        
        # Save the file and store the filename in the database
        if image_file:
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(image_path)
        else:
            filename = None
        
        services = {
            "categories": categories,
            "price": price,
            "colour": colour,
            "description": description,
            "image_url": filename
        }
        db.services.insert_one(services)
        
        services = list(db.services.find())
        return render_template("Display_Services.html", services=services)
    return render_template("Display_Services.html")




# Display Services
@app.route("/Display_Servicess", methods=["POST", "GET"])
def Display_Services():
    services = list(db.services.find())
    return render_template("Display_Services.html", services=services)

@app.route("/Edit_Services", methods=["POST"])
def update_service():
    # Get form data
    if request.method == "POST":
        id = request.form["id"]

    # Update service in MongoDB

    # Redirect to the home page after updating service
        return render_template("Update.html", id=id)

@app.route("/Update_Services", methods=["POST"])
def update_service2():
    # Get form data
    if request.method == "POST":
        id = request.form["id"]
        categories = request.form["categories"]
        price = request.form["price"]
        colour = request.form["colour"]
        description = request.form["description"]
    # Update service in MongoDB
        mongo.db.services.update_one({"_id": ObjectId(id)}, {"$set": {"categories": categories, "price": price, "colour": colour, "description": description}})
    # Redirect to the home page after updating service
        return render_template("Update.html", id=id)
    
    
    
# Delete Services Page
@app.route("/delete", methods=["GET", "POST"])
def delete_Display_Services():
    if request.method == "POST":
        # Get form data
        id = request.form["delete_id"]

        mongo.db.services.delete_one({"_id": ObjectId(id)})
        services = list(mongo.db.services.find())
        # Redirect to the services page after deleting service
        return render_template("Display_Services.html", services=services)

    return render_template("Add_Services.html")


# Register

@app.route("/Register", methods=["POST", "GET"])
def Register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        user = {"name": name, "email": email, "password": password}
        if db.user2.insert_one(user):
         return render_template ("ClientsLogin.html")
    return render_template("Register.html")

# LOGIN
 
@app.route("/Clientslogin", methods=["GET", "POST"])
def Clientslogin():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]

        user = {"name": name, "password": password}
        if db.user2.find_one(user):
            return redirect(url_for("ViewProduct"))

    return render_template("ClientsLogin.html")

                                                                                                                                                
# View Product
@app.route("/ViewProduct", methods=["GET"])
def ViewProduct():
    services = list(db.services.find())
    return render_template("ViewProduct.html", services=services)

@app.route("/viewProduct/<product_id>")
def ViewSingleProduct(product_id):
    product = db.services.find_one({"_id": ObjectId(product_id)})
    return render_template("ViewSingleProduct.html", product=product)

@app.route('/AddToCart', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')
    product = db.services.find_one({"_id": ObjectId(product_id)})

    if product:
        cart_item = {
            'id': str(product['_id']),
            'categories': product['categories'],
            'price': product['price'],
            'colour': product['colour'],
            'description': product['description'],
            'image_url': product['image_url'],
            'quantity': 1
        }

        cart_items = session.get('cart', [])
        for item in cart_items:
            if item['id'] == cart_item['id']:
                item['quantity'] += 1
                break
        else:
            cart_items.append(cart_item)

        session['cart'] = cart_items

    return redirect(url_for('cart'))

@app.route('/ViewCart')
def cart():
    cart_items = session.get('cart', [])
    total_price = sum(float(item['price']) * item['quantity'] for item in cart_items)
    cart_count = len(cart_items)
    return render_template('ViewCart.html', cart_items=cart_items, total_price=total_price, cart_count=cart_count)

@app.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    item_id = request.form.get('selected_items')
    cart_items = session.get('cart', [])
    cart_items = [item for item in cart_items if item['id'] != item_id]
    session['cart'] = cart_items
    return redirect(url_for('cart'))

@app.route('/cart/checkout-success', methods=['POST'])
def checkout_success():
    session.pop('cart', None)
    return redirect('/checkout_success')



# ADDTOCART

# @app.route("/AddToCart")
# def AddToCart():
#     return render_template("AddToCart.html")


# @app.route('/Cart', methods=['POST'])
# def add_to_cart():
#     id = request.form.get('id')
#     category = request.form.get('category')
#     price = request.form.get('price')
#     colour = request.form.get('colour')
#     description = request.form.get('description')
#     image = request.form['image']
#     item = {'id': id, 'category': category, 'price': price, 'colour': colour, 'description': description, 'image': image}
#     cart_items = session.get('cart', [])
#     cart_items.append(item)
#     session['cart'] = cart_items
#     print("cart items", id)
#     print("cart items1", price)
#     print("cart items2", colour)
#     print("cart items3", image)
#     print("cart items4", description)
#     print("cart items5", category)
#     return redirect(url_for('cart'))


# VEIWCART

# @app.route('/ViewCart')
# def cart():
#     cart_items = session.get('cart', [])
#     total_price = sum(float(item['Amount']) for item in cart_items)
#     cart_count = len(session.get('cart', []))
#     print("cart items1", total_price)
#     return render_template('Cart.html', cart_items=cart_items, total_price=total_price, cart_count=cart_count)

# # fix delete 
# @app.route('/cart/remove', methods=['POST'])
# def remove_from_cart():
#     selected_items = request.form.getlist('selected_items')
#     cart_items = session.get('cart', [])
#     cart_items = [item for item in cart_items if item['id'] not in selected_items]
#     session['cart'] = cart_items
#     return redirect(url_for('cart'))

# @app.route('/cart/checkout', methods=['POST'])
# def checkout():
#     session.pop('cart', None)
#     return redirect('/checkout_success')

# ACCESS
@app.route("/Access")
def Access():
    return render_template("Landing.html")


# @app.route("/")
# def Landing():
#     return render_template("Access.html")


cart_items = [
    {'id': 1, 'image': 'item1.jpg', 'category': 'Electronics', 'price': 100, 'colour': 'Red', 'description': 'A cool gadget', 'quantity': 1},
    {'id': 2, 'image': 'item2.jpg', 'category': 'Clothing', 'price': 50, 'colour': 'Blue', 'description': 'A nice shirt', 'quantity': 2},
]

def calculate_total_price(cart_items):
    return sum(item['price'] * item['quantity'] for item in cart_items)

@app.route('/')
def index():
    return 'Welcome to the Online Store!'

# @app.route("/Cart")
# def Cart():
#     return render_template("Cart.html")

# @app.route('/cart')
# def view_cart():
#     total_price = calculate_total_price(cart_items)
#     return render_template('view_cart.html', cart_items=cart_items, total_price=total_price)

# @app.route('/cart/remove', methods=['POST'])
# def remove_from_cart():
#     item_id = int(request.form['selected_items'])
#     global cart_items
#     cart_items = [item for item in cart_items if item['id'] != item_id]
#     return redirect(url_for('view_cart'))
@app.route('/cart/update_quantity', methods=['POST'])
def update_cart():
    data = request.get_json()
    product_id = data.get('id')
    quantity = int(data.get('value'))

    cart = session.get('cart', [])
    for item in cart:
        if item['id'] == product_id:
            item['quantity'] = quantity
            break

    session['cart'] = cart
    total = round(sum(float(item['price']) * item['quantity'] for item in cart), 2)
    item_price = round(next((float(item['price']) * item['quantity'] for item in cart if item['id'] == product_id), 0), 2)
    return jsonify({'success': True, 'total': total, 'item_price': item_price})



# @app.route('/checkout', methods=['POST'])
# def checkout():
#     # Implement checkout logic here
#     return 'Checkout process initiated.'


# CHECKOUT

@app.route('/checkout')
def checkout():
    cart_items = session.get('cart', [])
    total_price = sum(float(item['price']) * item['quantity'] for item in cart_items)
    cart_count = len(cart_items)
    return render_template('Checkout.html', cart_items=cart_items, total_price=total_price, cart_count=cart_count)


@app.route('/client-checkout')
def usercheckout():
    cart_items = session.get('cart', [])
    total_price = sum(float(item['price']) * item['quantity'] for item in cart_items)
    # cart_count = len(cart_items)
    return render_template('Checkout.html', total_price=total_price)

@app.route('/payment-successful')
def success():
    session.pop('cart', None)
    return render_template('success.html')



# @app.route('/Checkout', methods=['POST'])
# def Checkout():
#     data = request.get_json()
#     data = request.json
#     name = data.get('name')
#     email = data.get('email')
#     cell_number = data.get('cell_number')
#     address = data.get('address')
#     city = data.get('city')
#     zip_code = data.get('zip')
    
   
    # Process the order data and save it to the database
    # ...
    # return jsonify({'message': 'Order placed successfully'})

    # data = {"name": name, "email": email,"cell_number": cell_number, "address": address, "city": city, "zip_code": zip_code,}
    # if db.data.insert_one(data):
    #        return redirect(url_for(""))
    # return render_template("")


# def update_cart_item_quantity(item_id, new_quantity):
#     items = session.get('cart', [])

#     for item in items:
#         if item['id'] == item_id:
#             if new_quantity > 0:
#                 item['quantity'] = new_quantity
#             else:
#                 items.remove(item)
#             break
#     else:
#         if new_quantity > 0:
#             items.append({'id': item_id, 'quantity': new_quantity})
#     session['cart'] = items
    
# item_id_to_update = 'your_item_id' 
# new_quantity = 5  

# update_cart_item_quantity(item_id_to_update, new_quantity)


# PopUpPage

@app.route('/PopUpPage')
def PopUpPage():
    return render_template('PopUpPage.html')

# @app.route('/PopUpPage')
# def PopUpPage():
#     return redirect(url_for('PopUpPage'))


if __name__ == '__main__':
    app.run(debug=True)
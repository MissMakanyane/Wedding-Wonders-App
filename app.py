from flask import Flask, url_for, redirect, Response, request, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__, static_url_path='/static')
app.config["MONGO_URI"] = "mongodb://localhost:27017/SignUp"
mongo = PyMongo(app)
db = mongo.db

# LANDING
@app.route("/")
def landing():
    return render_template("Landing.html")

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
        image_url = request.form.get("image_url")  # Ensure you get image_url from form or set a default value
        print("frnjif")
        services = {
            "categories": categories,
            "price": price,
            "colour": colour,
            "description": description,
            "image_url": image_url
        }
        db.services.insert_one(services)
        services = []
        
        for i in db.services.find():
            services.append(i)
        return render_template("Display_Services.html", services=services)
    return render_template("Display_Services.html")

# Display Services
@app.route("/Display_Servicess", methods=["POST", "GET"])
def Display_Services():
    services = list(db.services.find())
    return render_template("Display_Services.html", services=services)

# UPDATE    mongo.db.services.update_one({"_id": ObjectId(id)}, {"$set": {"service_name": service_name, "image_url": image_url}})

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
        prices = request.form["prices"]
        colours = request.form["colours"]
        description = request.form["description"]
    # Update service in MongoDB
        mongo.db.services.update_one({"_id": ObjectId(id)}, {"$set": {"categories": categories, "price": prices, "colour": colours, "description": description}})
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
        cornfirmpassword = request.form["cornfirm password"]

        user = {"name": name, "email": email, "password": password, "cornfirm password": cornfirmpassword}
        if db.user.insert_one(user):
            # return redirect(url_for("ClientsLogin"))
            return render_template("ClientsLogin.html")
    return render_template("Register.html")

# ClientsLogin
@app.route("/ClientsLogin", methods=["GET", "POST"])
def ClientsLogin():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]

        user = {"name": name, "password": password}
        if db.user.find_one(user):
            return render_template("ViewProduct.html")

    return render_template("ClientsLogin.html")

# ViewProduct

@app.route("/ViewProduct")
def ViewProduct():
    return render_template("ViewProduct.html")


if __name__ == '__main__':
    app.run(debug=True)
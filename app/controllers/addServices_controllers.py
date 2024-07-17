from flask import Flask, url_for, redirect, Response, request, render_template,session, jsonify
from ..models.addServices_models import Services
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os
from werkzeug.utils import secure_filename



app = Flask(__name__)

UPLOAD_FOLDER = 'app/static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Add_service

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
    
    # add product to database  
        Services.Add_Services(services)
    # display or get products from database
        services = list(Services.display_items())
        
        return render_template("Display_Services.html", services=services)
    return render_template("Display_Services.html")

# Display Services
def Display_Services():
    services = list(Services.display_items())
    return render_template("Display_Services.html", services=services)

def ViewProduct():
    services = list(Services.View())
    
    return render_template("ViewProduct.html", services=services)

def ViewSingleProduct(product_id):
    product_id = list(Services.View(product_id))
    return render_template("ViewSingleProduct.html", product_id=product_id)


   
def upload_file(file):
    return "https://example.com/uploads/" + file.filename

def update_service():
    
    if request.method == "POST":
        id = request.form["id"]
        
        return render_template("Update.html", id=id)


def update_service2():
    # Get form data
    if request.method == "POST":
        id = request.form["id"]
        categories = request.form["categories"]
        price = request.form["price"]
        colour = request.form["colour"]
        description = request.form["description"]
    # Update service in MongoDB
        services.update_one({"_id": ObjectId(id)}, {"$set": {"categories": categories, "price": price, "colour": colour, "description": description}})
        
        services = services.update_one()
        
    # Redirect to the home page after updating service
        return render_template("Update.html", id=id)
    
    
    
# Delete Services Page
def delete_Display_Services():
    if request.method == "POST":
        # Get form data
        id = request.form["delete_id"]

        services.delete_one({"_id": ObjectId(id)})
        services = list(services.find())
        # Redirect to the services page after deleting service
        return render_template("Display_Services.html", services=services)

    return render_template("Add_Services.html")
    

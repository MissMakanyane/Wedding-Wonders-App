from flask import Flask, url_for, redirect, Response, request, render_template,session, jsonify
from ..models.users_model import User
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

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
      
        services = list()
        return render_template("Display_Services.html", services=services)
        return render_template("Display_Services.html")

    

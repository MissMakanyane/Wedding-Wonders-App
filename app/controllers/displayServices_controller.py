from flask import Flask, url_for, redirect, Response, request, render_template,session, jsonify
from ..models.users_model import User
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os
from werkzeug.utils import secure_filename



def Display_Services():
    services = list()
    return render_template("Display_Services.html", services=services)


def update_service():
    # Get form data
    if request.method == "POST":
        id = request.form["id"]

    # Update service in MongoDB

    # Redirect to the home page after updating service
        return render_template("Update.html", id=id)


# def update_service2():
#     # Get form data
#     if request.method == "POST":
#         id = request.form["id"]
#         categories = request.form["categories"]
#         price = request.form["price"]
#         colour = request.form["colour"]
#         description = request.form["description"]
#     # Update service in MongoDB
#         mongo.db.services.update_one({"_id": ObjectId(id)}, {"$set": {"categories": categories, "price": price, "colour": colour, "description": description}})
#     # Redirect to the home page after updating service
#         return render_template("Update.html", id=id)
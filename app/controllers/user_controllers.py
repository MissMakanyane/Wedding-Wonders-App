from flask import Flask, url_for, redirect, Response, request, render_template,session, jsonify
from ..models.users_model import User 
from flask_pymongo import PyMongo
from bson.objectid import ObjectId




def landing():
    return render_template("Access.html")
# Register

def Register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        details = {"name": name, "email": email, "password": password}
        if (User.create_user(details)):
         return render_template ("ClientsLogin.html")
     
    return render_template("Register.html")

# Clientslogin

def Clientslogin():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]

        LoginDetails = {"name": name, "password": password}
       
        if (User.login_user(LoginDetails)):
            return render_template("ViewProduct.html")
    return render_template("ClientsLogin.html")

# SIGNUP

def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
 
        SignupDetails = {"name": name, "email": email, "password": password}
        
        # check if user exist using email / username
        
        
        
        
        if (User.admin_signup(SignupDetails)):
            return render_template ("Login.html")
    return render_template("SignUp.html")

# LOGIN

def login():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]

        AdminDetails = {"name": name, "password": password}
        if (User.admin_login(AdminDetails)):
            return render_template("Add_Services.html")

    return render_template("Login.html")


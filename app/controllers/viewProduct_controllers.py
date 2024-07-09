from flask import Flask, url_for, redirect, Response, request, render_template,session, jsonify
from flask import Flask, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId




# View Product

def ViewProduct():
    services = list()
    return render_template("ViewProduct.html", services=services)

def ViewSingleProduct(product_id):
    product = ()
    return render_template("ViewSingleProduct.html", product=product)



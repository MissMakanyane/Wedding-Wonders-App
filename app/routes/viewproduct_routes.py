from flask import Blueprint, render_template,request
from ..controllers import user_controllers
from ..import mongo
from flask import request, redirect, url_for, render_template
from flask import Flask

app = Flask(__name__)

app.route("/ViewProduct", methods=["GET"])(user_controllers. ViewProduct)

app.route("/viewProduct/<product_id>")(user_controllers. ViewProduct)
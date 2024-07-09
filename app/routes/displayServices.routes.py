from flask import Blueprint, render_template,request
from ..controllers import user_controllers
from ..import mongo
from flask import request, redirect, url_for, render_template

app = Blueprint ('user',__name__)

app.route("/Display_Servicess", methods=["POST", "GET"])

app.route("/Edit_Services", methods=["POST"])

app.route("/Update_Services", methods=["POST"])
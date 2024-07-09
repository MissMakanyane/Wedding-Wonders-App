from flask import Blueprint, render_template,request
from ..controllers import user_controllers
from ..import mongo
from flask import request, redirect, url_for, render_template

app = Blueprint ('user',__name__)

app.route('/Add_Services', methods=["POST", "GET"])(user_controllers.Add_Services)

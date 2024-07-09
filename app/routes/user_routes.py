from flask import Blueprint, render_template,request
from ..controllers import user_controllers
from ..import mongo
from flask import request, redirect, url_for, render_template


app = Blueprint ('user',__name__)

auth_bp = Blueprint('auth', __name__)

app.route("/")(user_controllers.landing)

app.route("/Register", methods=['GET', 'POST'])(user_controllers.Register)

app.route("/Clientslogin", methods=["GET", "POST"])(user_controllers. Clientslogin)

app.route("/signup", methods=["POST", "GET"])(user_controllers.signup)

app.route("/Login", methods=["GET", "POST"])(user_controllers. login)

auth_bp.route('/check_email', methods=['POST'])

auth_bp.route('/check_email', methods=['POST'])
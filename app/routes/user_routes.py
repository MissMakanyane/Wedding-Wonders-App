from flask import Blueprint
from ..controllers import user_controllers

app = Blueprint ('user',__name__)

app.route("/")(user_controllers.landing)

app.route("/Register", methods=['GET', 'POST'])(user_controllers.Register)

app.route("/Clientslogin", methods=["GET", "POST"])(user_controllers. Clientslogin)

app.route("/signup", methods=["POST", "GET"])(user_controllers.signup)

app.route("/Login", methods=["GET", "POST"])(user_controllers. login)

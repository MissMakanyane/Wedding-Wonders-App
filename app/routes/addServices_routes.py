from flask import Blueprint
from ..controllers import addServices_controllers


app = Blueprint ('Services',__name__)

app.route('/Add_Services', methods=["POST", "GET"])(addServices_controllers.Add_Services)

app.route('/Display_Services', methods=["POST", "GET"])(addServices_controllers.Display_Services)

app.route("/ViewProduct", methods=["GET"])(addServices_controllers.ViewProduct)

app.route("/viewProduct", methods=["POST", "GET"])(addServices_controllers.ViewSingleProduct)

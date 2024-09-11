from flask import Blueprint
from ..controllers import addServices_controllers


app = Blueprint ('Services',__name__)

app.route('/Add_Services', methods=["POST", "GET"])(addServices_controllers.Add_Services)

app.route('/Display_Services', methods=["POST", "GET"])(addServices_controllers.Display_Services)

app.route("/ViewProduct", methods=["GET"])(addServices_controllers.ViewProduct)

app.route("/viewProduct", methods=["POST", "GET"])(addServices_controllers.ViewSingleProduct)

app.route("/Edit_Services", methods=["POST"])(addServices_controllers.update_service)

app.route("/Update_Services", methods=["POST"])(addServices_controllers.update_service2)

app.route("/delete_Display_Services", methods=["GET", "POST"])(addServices_controllers.delete_Display_Services)
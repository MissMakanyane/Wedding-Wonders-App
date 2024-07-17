from flask import Blueprint, render_template,request
from ..controllers import addServices_controllers



app = Blueprint ('Add_Services',__name__)

app.route('/Add_Services', methods=["POST", "GET"])(addServices_controllers.Add_Services)

app.route('/Display_Services', methods=["POST", "GET"])(addServices_controllers.Display_Services)

app.route("/ViewProduct", methods=["GET"])(addServices_controllers.ViewProduct)

app.route("/viewProduct/<product_id>")(addServices_controllers.ViewProduct)

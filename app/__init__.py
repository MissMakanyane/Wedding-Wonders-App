from flask import Flask
from flask_pymongo import PyMongo
from .config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
   
    
    mongo.init_app(app)
    with app.app_context():
       from .routes import user_routes
       from .routes import addServices_routes
       from .routes import addToCart_routes
       
       
       app.register_blueprint(user_routes.app)
       app.register_blueprint(addServices_routes.app)
       app.register_blueprint(addToCart_routes.app)
      
    return app


mongo = PyMongo()
  
from ..import mongo
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename

class Carts_Services:
    
    def Add(product_id):
        mongo.db.services.find_one({"_id": ObjectId(product_id)})
    
    
from ..import mongo
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename


def view_product(product_id):
    mongo.db.services.find_one({"_id": ObjectId(product_id)})
    return str(product_id)

def view_one(products):
    services = list(mongo.db.services.find(products))
    return str(services)
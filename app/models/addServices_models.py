from ..import mongo
from bson.objectid import ObjectId
db = mongo.db

class Services:
    
    def Add_Services(services):
        return mongo.db.services.insert_one(services)

    def display_items():
        return mongo.db.services.find()

    
    def View(product_id):
        return mongo.db.services.find_one({"_id": ObjectId(product_id)})
    

    def update_one(new_service):  
        mongo.db.services.update_one({"_id": ObjectId(id)})
        
    def delete_one(service):
          return mongo.db.services.find(service)

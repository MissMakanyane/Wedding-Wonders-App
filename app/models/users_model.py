from ..import mongo


class User:
   
    def create_user(details):
    #  mongo.db.user2.insert_one(details)
     return mongo.db.user2.insert_one(details)

    def login_user(loginDetails):
        # mongo.db.user2.find_one(loginDetails)
        return mongo.db.user2.find_one(loginDetails)
                               
    def admin_signup(SignupDetails):
        return mongo.db.user.insert_one(SignupDetails)

    def admin_login(AdminDetails):
        mongo.db.user.find_one(AdminDetails)
        return str(AdminDetails)
    
    def check_client_email(email):
        return mongo.db.user2.find_one({"email": email})
    
    def check_admin_email(email):
        return mongo.db.user.find_one({"email": email})
   
   
    def check_client_username(username):
        return mongo.db.user2.find_one({"username": username})
    

    def check_admin_username(username):
        return mongo.db.user.find_one({"usernamel": username})
    

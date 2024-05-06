from ast import Call
from flask import Flask, url_for, redirect, Response, request, render_template
from flask_pymongo import PyMongo

app = Flask(__name__,static_url_path=('/static'))
app.config["MONGO_URI"] = "mongodb://localhost:27017/SignUp"
Mongo = PyMongo(app)
db  = Mongo.db

# LANDING
@app.route("/")
def landing():
        return render_template("Landing.html")

# SIGN UP

@app.route("/signup",methods=["POST", "GET"])
def signup():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]

        user = {"name":name, "email": email, "password": password }
        if  db.user.insert_one(user):
            return redirect(url_for("login"))
    return render_template("SignUp.html"  )

# LOGIN

@app.route("/Login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]

        user = {"name": name, "password": password}
        
        
        if db.user.find_one(user):
            return render_template("Calllog.html")


    return render_template("Login.html")




# ABOUT

@app.route("/About")
def About():
        return render_template("About.html")

# RINGS

@app.route("/Rings")
def Rings():
        return render_template("Rings.html")

# Traditional Attires

@app.route("/TraditionalAttires")
def Traditional_Attires():
        return render_template("TraditionalAttires.html")
   
#    SUITS

@app.route("/Suits")
def Suits():
        return render_template("Suits.html")
   
#    GOWNS
   
@app.route("/Gown")
def Gown():
        return render_template("Gown.html")
   
    # ADD CALL LOG
    
@app.route('/add_call', methods=["POST", "GET"])
def add_call():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        date = request.form['date']
        cellphone_number= request.form['cellphone_number']
        description = request.form['description']
        
        call_log = { 'name': name, 'surname': surname, 'date': date, 'cellphone_number': cellphone_number, 'description': description,}

        db.calllog.insert_one(call_log)
        if ('form submission success'):
                     return redirect (url_for('calllog'))
        else:
                  if ('form submission failed'):
                   return 'form unsuccessful'
        
    return render_template("AddCallLog.html")

@app.route("/calllog", methods=["POST", "GET"] )
def calllog():
     if request.method == 'GET':
         calllog = []
# get finances to view in html
         for i in db.calllog.find():
               calllog.append(i)
               
               
    
     return render_template("Calllog.html", calllog=calllog)

if __name__ == '__main__':
    app.run(debug = True)
    
    

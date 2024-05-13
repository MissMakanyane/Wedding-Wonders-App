from ast import Call
from flask import Flask, url_for, redirect, Response, request, render_template
from flask_pymongo import PyMongo

app = Flask(__name__,static_url_path=('/static'))
app.config["MONGO_URI"] = "mongodb://localhost:27017/SignUp"
Mongo = PyMongo(app)
db  = Mongo.db


app = Flask(__name__, static_url_path='/static')
app.config["MONGO_URI"] = "mongodb://localhost:27017/SignUp"
mongo = PyMongo(app)
db = mongo.db
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
  
#   DELETE CALLLOG

# calllog_data = [
#     {"id": 1,},
#     {"id": 2}
# ]

@app.route('/calllog', methods=['GET', 'POST'])
def calllog():
    if request.method == 'POST':
        if 'delete' in request.form:
            print(request.form['delete'])
            id_to_delete = request.form['delete']
            global calllog_data

            db.calllog.delete_many( {"surname": id_to_delete})
            calllogs = []

            for log in db.calllog.find():
                        calllogs.append(log)
                

            # calllog_data = [row for row in calllog_data if row['id'] != id_to_delete]
            return render_template('Calllog.html', calllog=calllogs)

    return render_template('Calllog.html')

@app.route('/AddItem')
def add_item():   
    return render_template("AddCalllog.html")


# ADD CALL LOG

@app.route('/AddCalllog', methods=["POST", "GET"])
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
            calllogs = []

            for log in db.calllog.find():
                        calllogs.append(log)
                        print(log)
            return render_template("Calllog.html", calllog=calllogs)
        else:
                  if ('form submission failed'):
                   return 'form unsuccessful'
        
    return render_template("Calllog.html")


     




if __name__ == '__main__':
    app.run(debug = True)
    
    


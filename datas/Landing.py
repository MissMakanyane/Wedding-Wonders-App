from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["your-database-name"]
collection = db["your-collection-name"]

@app.route("/")
def Landing():
    return render_template("Landing.html")

@app.route("/add", methods=["POST"])
def add_data():
    data = request.form.get("data")

    # Insert the data into the MongoDB collection
    collection.insert_one({"data": data})

    return "Data added successfully"

@app.route("/delete", methods=["POST"])
def delete_data():
    data = request.form.get("data")

    # Delete the data from the MongoDB collection
    collection.delete_one({"data": data})

    return "Data deleted successfully"

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    
    
    
    @app.route("/")
    def index(): return render_template("Landing.html")

if __name__ == "__main__":
    app.run(debug=True)
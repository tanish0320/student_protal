from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://toyijaks0320_db_user:<db_password>@studentporal.ske5qgz.mongodb.net/?appName=Studentporal")
db = client["student_portal"]

@app.route("/")
def home():
    return "Backend & Database connected"

if __name__ == "__main__":
    app.run(debug=True)



from flask import Flask
from dotenv import load_dotenv
import os

from extensions import mongo, bcrypt, jwt

load_dotenv()

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

mongo.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

from auth import auth_bp
app.register_blueprint(auth_bp, url_prefix="/auth")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

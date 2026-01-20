from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from extensions import mongo, bcrypt
from auth import auth_bp
from dotenv import load_dotenv
import certifi
import os

from extensions import mongo, bcrypt, jwt
from auth import auth_bp

load_dotenv()

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
print("JWT_SECRET_KEY =", app.config["JWT_SECRET_KEY"])

app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["MONGO_TLS_CA_FILE"] = certifi.where()

mongo.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

from auth import auth_bp
app.register_blueprint(auth_bp, url_prefix="/auth")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

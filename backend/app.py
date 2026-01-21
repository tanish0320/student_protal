from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
import certifi

from extensions import mongo, bcrypt, jwt
from auth import auth_bp

load_dotenv()

app = Flask(__name__)

# ✅ FIXED CORS CONFIG (THIS IS THE IMPORTANT PART)
CORS(
    app,
    resources={r"/*": {"origins": "http://localhost:5173"}},
    supports_credentials=True
)

# Config
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["MONGO_TLS_CA_FILE"] = certifi.where()

# Init extensions
mongo.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

# Blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

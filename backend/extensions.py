from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import certifi

mongo = PyMongo()
bcrypt = Bcrypt()
jwt = JWTManager()

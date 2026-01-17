from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from extensions import mongo, bcrypt

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Missing fields"}), 400

    if mongo.db.users.find_one({"email": email}):
        return jsonify({"error": "User already exists"}), 409

    hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")

    mongo.db.users.insert_one({
        "email": email,
        "password": hashed_pw,
        "role": "student"   # default role
    })

    return jsonify({"message": "User registered"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    email = data.get("email")
    password = data.get("password")

    user = mongo.db.users.find_one({"email": email})

    if not user or not bcrypt.check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=email)

    return jsonify({"access_token": token}), 200


@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def me():
    email = get_jwt_identity()

    user = mongo.db.users.find_one(
        {"email": email},
        {"_id": 0, "password": 0}
    )

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user), 200

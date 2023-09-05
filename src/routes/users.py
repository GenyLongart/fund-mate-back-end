from flask import Blueprint, request, jsonify
from schemas.user_schema import UserSchema
from schemas.login_schema import LoginSchema
from services.user_service import UserService
from marshmallow import ValidationError

bp = Blueprint('users', __name__)
user_schema = UserSchema()
login_schema = LoginSchema()
user_service = UserService()

@bp.route('/login', methods=['POST'])
def login():
    
    try:
        # Deserialize the incoming JSON data using the LoginSchema
        login_data = login_schema.load(request.json)

    # Check if deserialization was successful and validate the data
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    username = login_data['username']
    password = login_data['password']

    #try and login the user
    result = user_service.login_user(username, password)
    
    #if failed, invalid
    if not result:
        return jsonify({"error": "Invalid credentials"}), 401
    
    # Serialize the structured result using UserSchema
    user_data = UserSchema(exclude=("password",)).dump(result['user'])

    return jsonify({"user": user_data, "access_token": result['access_token']}), 200

@bp.route('/register', methods=['POST'])
def register_user():
    try:
        # Deserialize the incoming JSON data using the UserSchema
        user_data = user_schema.load(request.json)

    # Check if deserialization was successful and validate the data
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Check if the username already exists
    if user_service.username_exists(user_data['username']):
        return jsonify({"error": "Username already exists"}), 400

    # Create a new user using the UserService
    new_user = user_service.create_user(user_data)

    if new_user:
        # Serialize the new user using the UserSchema and return a success response
        serialized_user = user_schema.dump(new_user)
        return jsonify(serialized_user), 201
    else:
        return jsonify({"error": "Registration failed, please try again"}),

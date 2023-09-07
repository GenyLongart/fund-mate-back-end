from flask import Blueprint, request, jsonify
from schemas.user_schema import UserSchema
from schemas.login_schema import LoginSchema
from services.user_service import UserService
from marshmallow import ValidationError
import json

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
        # Check if the 'templateRequest' field is in the form data
        if 'loginRequest' not in request.form:
            return jsonify({"msg": "JSON data 'loginRequest' is required!"}), 400

        elif 'identityFile' not in request.files:
            return jsonify({"msg": "File 'identityFile' is required!"}), 400
        
        elif 'dicomFile' not in request.files:
            return jsonify({"msg": "File 'dicomFile' is required!"}), 400 
        
        user_data = json.loads(request.form['loginRequest'])
        user_data['identity']['identityFile'] = request.files['identityFile']
        user_data['dicom']['dicomFile'] = request.files['dicomFile']
        
        # Deserialize the incoming JSON data using the UserSchema
        user_data = user_schema.load(user_data)

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
        serialized_user = UserSchema(exclude=("password",)).dump(new_user)
        return jsonify(serialized_user), 201
    else:
        return jsonify({"error": "Registration failed, please try again"}), 404
    
@bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        # Get a user using the UserService
        user = user_service.get_user(user_id)
        print(user)
    
        if user:
            # Serialize the new user using the UserSchema and return a success response
            serialized_user = UserSchema(exclude=("password",)).dump(user)
            return jsonify(serialized_user), 200
        else:
            return jsonify({"error": "Failed to get user, please try again"}), 404
    except Exception as e:
        return jsonify({"message": "User get failed: " + str(e)}), 500
    

@bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        noUser = user_service.deleteUser(user_id)
        if noUser:
            return jsonify({"message": "User deleted successfully"}), 200
        else:
            return jsonify({"message": "User does not exist to delete"}), 404
    except Exception as e:
        return jsonify({"message": "User deletion failed: " + str(e)}), 500


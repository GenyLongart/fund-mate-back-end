from flask import Blueprint, request, jsonify
from schemas.user.user_schema import UserSchema
from schemas.user.login_schema import LoginSchema
from schemas.user.user_schema import BankDetailsSchema
from schemas.user.phone_schema import PhoneSchema
from schemas.user.profile_picture_schema import ProfilePictureSchema
from services.user.user_service import UserService
from services.user.bank_service import BankService
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity
import json

bp = Blueprint('user', __name__)
user_schema = UserSchema()
login_schema = LoginSchema()
bank_schema = BankDetailsSchema()
phone_schema = PhoneSchema()
profile_picture_schema = ProfilePictureSchema()
user_service = UserService()
bank_service = BankService()

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
@jwt_required()
def get_user(user_id):
    try:
        # Extract the user's ID from the JWT payload
        current_user_id = get_jwt_identity()

         # Check if the current user's ID matches the user_id in the URL
        if current_user_id != user_id:
            return jsonify({"message": "You are not authorized to get another user's full details"}), 403
        
        # Get a user using the UserService
        user = user_service.get_user(user_id)
        if user:
            # Serialize the new user using the UserSchema and return a success response
            serialized_user = UserSchema(exclude=("password",)).dump(user)
            return jsonify(serialized_user), 200
        else:
            return jsonify({"error": "Failed to get user, please try again"}), 404
    except Exception as e:
        return jsonify({"message": "User get failed: " + str(e)}), 500
    

@bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    try:
        # Extract the user's ID from the JWT payload
        current_user_id = get_jwt_identity()

         # Check if the current user's ID matches the user_id in the URL
        if current_user_id != user_id:
            return jsonify({"message": "You are not authorized to delete another user's account"}), 403
        
        noUser = user_service.deleteUser(user_id)
        if noUser:
            return jsonify({"message": "User deleted successfully"}), 200
        else:
            return jsonify({"message": "User does not exist to delete"}), 404
    except Exception as e:
        return jsonify({"message": "User deletion failed: " + str(e)}), 500


@bp.route('/<int:user_id>/bank', methods=['PUT'])
@jwt_required()
def edit_user_banco(user_id):
    try:
        # Extract the user's ID from the JWT payload
        current_user_id = get_jwt_identity()

         # Check if the current user's ID matches the user_id in the URL
        if current_user_id != user_id:
            return jsonify({"message": "You are not authorized to edit another user's bank details"}), 403

        # Get a user using the UserService
        user = user_service.get_user(user_id)

        if user:
            # Deserialize the incoming JSON data containing bank details
            bank_data = bank_schema.load(request.json)
            # edit the bank information using the bankService
            user = bank_service.edit_user_details(user, bank_data)

            return jsonify({"message": "User bank details updated successfully"}), 200

        else:
            return jsonify({"message": "User does not exist to edit"}), 404
        
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"message": "User edit failed: " + str(e)}), 500

@bp.route('/<int:user_id>/phone', methods=['PUT'])
@jwt_required()
def edit_user_phone(user_id):
    try:
        # Extract the user's ID from the JWT payload
        current_user_id = get_jwt_identity()

         # Check if the current user's ID matches the user_id in the URL
        if current_user_id != user_id:
            return jsonify({"message": "You are not authorized to edit another user's phone number"}), 403

        # Get a user using the UserService
        user = user_service.get_user(user_id)

        if user:
            # Deserialize the incoming JSON data containing bank details
            phone_data = phone_schema.load(request.json)
            # edit the bank information using the bankService
            user = user_service.update_phone_number(user, phone_data['phoneNumber'])

            return jsonify({"message": "User phone number updated successfully"}), 200

        else:
            return jsonify({"message": "User does not exist to edit"}), 404
        
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"message": "User edit failed: " + str(e)}), 500
    

@bp.route('/<int:user_id>/profile-picture', methods=['PUT'])
@jwt_required()
def edit_user_profilePicture(user_id):
    try:
        # Extract the user's ID from the JWT payload
        current_user_id = get_jwt_identity()

         # Check if the current user's ID matches the user_id in the URL
        if current_user_id != user_id:
            return jsonify({"message": "You are not authorized to edit another user's profile picture"}), 403

        # Get a user using the UserService
        user = user_service.get_user(user_id)

        if user:

            if 'profilePicture' not in request.files:
                return jsonify({"msg": "File 'profilePicture' is required!"}), 400
            
            # get profile picture
            profile_picture_data = request.files['profilePicture']
            # transform to JSON
            profile_picture_data = {
                "profilePictureFile": profile_picture_data
            }
            
             # Deserialize the incoming JSON data using the profile_picture_schema
            profile_picture_data = profile_picture_schema.load(profile_picture_data)
        
            # edit the profile picture using the userService
            user_service.update_profile_picture(user, profile_picture_data['profilePictureFile'])

            return jsonify({"message": "User profile picture updated successfully"}), 200

        else:
            return jsonify({"message": "User does not exist to edit"}), 404
        
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"message": "User edit failed: " + str(e)}), 500


import datetime
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from models import User

authApi = Blueprint('authApi', __name__)

@authApi.route('/login', methods=['POST'])
def login():
    
    username = request.json.get('username')
    password = request.json.get('password')
    
    if not username:
        return jsonify({"msg": "Username is required!"}), 400
    
    if not password:
        return jsonify({"msg": "Password is required!"}), 400
    
    userFound = User.query.filter_by(Username=username).first()
    
    if not userFound:
        return jsonify({"error": "Credentials are incorrect"}), 401
    
    if not check_password_hash(userFound.Password, password):
        return jsonify({"error": "Credentials are incorrect"}), 401
    
    expire = datetime.timedelta(days=1)
    access_token = create_access_token(identity=userFound.UserID, expires_delta=expire)
    
    data = {
        "access_token": access_token,
        "user": userFound.serialize()
    }
    
    return jsonify(data), 200

# @authApi.route('/register', methods=['POST'])
# def register():

#     # define the expected attributes from the body request
#     expectedAttributes = {
#         "username": None,
#         "password": None,
#         "firstName": None,
#         "lastName": None,
#         "email" : None,
#         "phoneNumber": None,
#         "mobileNumber" : None,
#         "nationality" : None,
#     }

#     # check if each attribute is in the body
#     for key in expectedAttributes:
#         value = request.json.get(key)

#         # if not, send message back stating required
#         if not value:
#             return jsonify({"msg": key + " is required! Not added to database"}), 400
#         else:
#             expectedAttributes[key] = value
    
#     # check if user already is in database
#     userFound = User.query.filter_by(Username=expectedAttributes["username"]).first()
    
#     # send back error response if already found
#     if userFound:
#         return jsonify({"error": "Username already exists"}), 400

#     # if not, create a new user
#     newUser = User()
#     newUser.Username = expectedAttributes["username"]
#     newUser.Password = generate_password_hash(expectedAttributes["password"])
#     newUser.FirstName = expectedAttributes["firstName"]
#     newUser.LastName = expectedAttributes["lastName"]
#     newUser.Email = expectedAttributes["email"]
#     newUser.PhoneNumber = expectedAttributes["phoneNumber"]
#     newUser.MobileNumber = expectedAttributes["mobileNumber"]
#     newUser.Nationality = expectedAttributes["nationality"]
#     newUser.save()

#     #check if new user has been initialised properly
#     if newUser:    
#         return jsonify({"success": "User has been created!"}), 200
    
#     else:
#         return jsonify({"error": "Register fail, please try again!"}), 400
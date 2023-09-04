import datetime
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from models import User

api = Blueprint('api1', __name__)

@api.route('/login', methods=['POST'])
def login():
    
    username = request.json.get('username')
    password = request.json.get('password')
    
    if not username:
        return jsonify({"msg": "Username is required!"}), 400
    
    if not password:
        return jsonify({"msg": "Password is required!"}), 400
    
    userFound = User.query.filter_by(username=username, active=True).first()
    
    if not userFound:
        return jsonify({"error": "Credentials are incorrects"}), 401
    
    if not check_password_hash(userFound.password, password):
        return jsonify({"error": "Credentials are incorrects"}), 401
    
    expire = datetime.timedelta(days=3)
    access_token = create_access_token(identity=userFound.id, expires_delta=expire)
    
    data = {
        "access_token": access_token,
        "user": userFound.serialize()
    }
    
    return jsonify(data), 200

@api.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    
    if not username:
        return jsonify({"msg": "Username is required!"}), 400
    
    if not password:
        return jsonify({"msg": "Password is required!"}), 400
    
    userFound = User.query.filter_by(username=username).first()
    
    if userFound:
        return jsonify({"error": "Username already exists"}), 400
    
    newUser = User()
    newUser.username = username
    newUser.password = generate_password_hash(password)
    newUser.save()

    if newUser:    

        expire = datetime.timedelta(days=3)
        access_token = create_access_token(identity=userFound.id, expires_delta=expire)
        
        data = {
            "access_token": access_token,
            "user": newUser.serialize()
        }
        
        return jsonify(data), 200
    
    else:
        return jsonify({"error": "Register fail, please try again!"}), 400
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.user.user_service import UserService
from schemas.user.get_single_user_schema import GetSingleUserSchema

bp = Blueprint('users', __name__)
user_service = UserService()
getSingleUserSchema = GetSingleUserSchema()

@bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    try:        
        # Get a user using the UserService
        user = user_service.get_user(user_id)
        if user:
            # Serialize the new user using the UserSchema and return a success response
            serialized_user = GetSingleUserSchema().dump(user)
            return jsonify(serialized_user), 200
        else:
            return jsonify({"error": "Failed to get user, please try again"}), 404
    except Exception as e:
        return jsonify({"message": "User get failed: " + str(e)}), 500



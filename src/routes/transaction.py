from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.user.user_service import UserService

bp = Blueprint('transaction', __name__)
user_service = UserService()

@bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_transactions_by_user_id(user_id):
    try:
        # Extract the user's ID from the JWT payload
        current_user_id = get_jwt_identity()

         # Check if the current user's ID matches the user_id in the URL
        if current_user_id != user_id:
            return jsonify({"message": "You are not authorized to view this user's transactions"}), 403
                
        # Get a user using the UserService
        user = user_service.get_user(user_id)

        if user:
            print()
        else:
            return jsonify({"error": "Failed to get user, please try again"}), 404
    except Exception as e:
        return jsonify({"message": "User get failed: " + str(e)}), 500
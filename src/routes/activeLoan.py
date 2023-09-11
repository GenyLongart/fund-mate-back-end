from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.activeLoanTransaction.activeLoanSchema import ActiveLoanSchema
from services.user.user_service import UserService

bp = Blueprint('activeLoan', __name__)
active_loan_schema = ActiveLoanSchema()
user_service = UserService()

@bp.route('/user/<int:user_id>', methods=['GET'])
@jwt_required()
def get_active_loans_by_user_id(user_id):
    try:
        # Extract the user's ID from the JWT payload
        current_user_id = get_jwt_identity()

         # Check if the current user's ID matches the user_id in the URL
        if current_user_id != user_id:
            return jsonify({"message": "You are not authorized to view this user's activeLoan"}), 403
                
        # Get a user using the UserService
        user = user_service.get_user(user_id)

        if user:
            # Serialize the new user using the UserSchema and return a success response
            active_loan_data = ActiveLoanSchema().dump(user)
            return jsonify(active_loan_data), 200
            
        else:
            return jsonify({"error": "Failed to get user, please try again"}), 404
    except Exception as e:
        return jsonify({"message": "User get failed: " + str(e)}), 500
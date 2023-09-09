from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.loans.loans_schema import LoansSchema
from services.user.user_service import UserService
from services.loans.loans_serivce import LoansService

bp = Blueprint('loans', __name__)
#loans_schema = LoansSchema()
user_service = UserService()
loan_service = LoansService()

@bp.route('/', methods=['GET'])
@jwt_required()
def get_all_loans():
    try:
        all_loans = loan_service.get_all_loans()
        # Serialize the new user using the UserSchema and return a success response
        serialized_loans = LoansSchema().dump(all_loans)
        return jsonify(serialized_loans), 200
        
    except Exception as e:
        return jsonify({"message": "Loan Advertisments get failed: " + str(e)}), 500
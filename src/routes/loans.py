from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.loans.loan_advertisement_schema import LoanAdvertisementSchema, LoanAdvertismentListSchema
from services.user.user_service import UserService
from services.loans.loans_serivce import LoansService
import models.db_utils as db_utils

bp = Blueprint('loans', __name__)
#loans_schema = LoansSchema()
user_service = UserService()
loan_advertisement_schema = LoanAdvertisementSchema()
loans_service = LoansService()

@bp.route('/', methods=['GET'])
@jwt_required()
def get_all_loans_advertisments():
    try:
        with db_utils.session_scope() as session:
            all_loans = loans_service.get_all_loans(session)
            # Serialize the new user using the UserSchema and return a success response
            serialized_loans = LoanAdvertismentListSchema(many=True).dump(all_loans)
            return jsonify(serialized_loans), 200
        
    except Exception as e:
        return jsonify({"message": "Loan Advertisments get failed: " + str(e)}), 500
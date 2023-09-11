from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.loans.loan_advertisement_schema import LoanAdvertisementSchema, LoanAdvertismentListSchema
from services.user.user_service import UserService
from services.loans.loans_serivce import LoansService
import models.db_utils as db_utils

bp = Blueprint('lender', __name__)
#loans_schema = LoansSchema()
user_service = UserService()
loan_advertisement_schema = LoanAdvertisementSchema()
loans_service = LoansService()

@bp.route('/<int:lender_id>/loan-advertisment', methods=['POST'])
@jwt_required()
def add_new_loan_advertisment(lender_id):
    try:
        # Extract the user's ID from the JWT payload
        current_user_id = get_jwt_identity()
        # we need to get user id from the lender id. They should be the same but this is an extra check 
        user_id = user_service.get_user_from_lender_id(lender_id)
        user_id = user_id.userID

        # Check if the current user's ID matches the user_id in the URL
        if current_user_id != user_id:
            return jsonify({"message": "You are not authorized to add a loan advertisment for another user"}), 403
        
        loan_advertisment_request = request.json
        loan_advertisment_request['lenderID'] = lender_id

        loan_advertisment = loan_advertisement_schema.load(loan_advertisment_request)
        loans_service.add_new_loan_advertisment(loan_advertisment)
        return jsonify({"message": "Loan Advertisment Added Successfully"}), 200
        
    except Exception as e:
        return jsonify({"message": "Loan Advertisment Creation Failed: " + str(e)}), 500


@bp.route('/<int:lender_id>/loan-advertisements', methods=['GET'])
@jwt_required()
def get_all_loan_advertisements(lender_id):
    try:
        with db_utils.session_scope() as session:
            # Extract the user's ID from the JWT payload
            current_user_id = get_jwt_identity()
            # we need to get user id from the debtor id. They should be the same but this is an extra check 
            user = user_service.get_user_from_lender_id(lender_id)
            user_id = user.userID

            # Check if the current user's ID matches the user_id in the URL
            if current_user_id != user_id:
                return jsonify({"message": "You are not authorized to view loan advertisements for another user"}), 403
            
            loan_advertisements = loans_service.get_loan_advertisements_by_lender(session, lender_id)
            serialized_loan_advertisements = LoanAdvertismentListSchema(many=True).dump(loan_advertisements)
            return jsonify(serialized_loan_advertisements), 200
        
    except Exception as e:
        return jsonify({"message": "Loan Advertisements By Lender get failed: " + str(e)}), 500
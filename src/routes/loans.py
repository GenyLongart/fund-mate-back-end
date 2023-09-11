from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.loans.loan_advertisement_schema import LoanAdvertisementSchema, LoanAdvertismentListSchema, LoanAdvertisementSingleSchema
from schemas.loans.loan_offer_schema import LoanOfferSingleSchema
from services.user.user_service import UserService
from services.loans.loans_serivce import LoansService
import models.db_utils as db_utils

bp = Blueprint('loans', __name__)
#loans_schema = LoansSchema()
user_service = UserService()
loan_advertisement_schema = LoanAdvertisementSchema()
loans_service = LoansService()

@bp.route('/loan-advertisements', methods=['GET'])
@jwt_required()
def get_all_loans_advertisments():
    try:
        with db_utils.session_scope() as session:
            amount = request.args.get('amount')
            filtered_loans = loans_service.get_filtered_loan_advertisements(session, amount)

            #all_loans = loans_service.get_all_loans(session)

            serialized_loans = LoanAdvertismentListSchema(many=True).dump(filtered_loans)
            return jsonify(serialized_loans), 200
        
    except Exception as e:
        return jsonify({"message": "Loan Advertisments get failed: " + str(e)}), 500
    
@bp.route('/loan-advertisements/<int:loan_advertisement_id>', methods=['GET'])
@jwt_required()
def get_loan_advertisement(loan_advertisement_id):
    try:

        # Get a loan using the LoanService
        loan_advertisement = loans_service.get_loan_advertisement(loan_advertisement_id)
        if loan_advertisement:
            # Serialize the new loan advertisement using the LoanAdvertisementSchema and return a success response
            serialized_loan_advertisement = LoanAdvertisementSingleSchema().dump(loan_advertisement)
            return jsonify(serialized_loan_advertisement), 200
        else:
            return jsonify({"error": "Failed to get loan advertisement, please try again"}), 404
    except Exception as e:
        return jsonify({"message": "Loan advertisement get failed: " + str(e)}), 500
    
@bp.route('/loan-offers/<int:loan_offer_id>', methods=['GET'])
@jwt_required()
def get_loan_offer(loan_offer_id):
    try:
        # Get a loan offer using the LoanService
        loan_offer = loans_service.get_loan_offer(loan_offer_id)
        if loan_offer:
            # Serialize the new loan offer using the LoanOfferSchema and return a success response
            serialized_loan_offer = LoanOfferSingleSchema().dump(loan_offer)
            return jsonify(serialized_loan_offer), 200
        else:
            return jsonify({"error": "Failed to get loan offer, please try again"}), 404
    except Exception as e:
        return jsonify({"message": "Loan offer get failed: " + str(e)}), 500
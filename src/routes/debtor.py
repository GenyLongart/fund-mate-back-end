from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.loans.loan_offer_schema import LoanOfferSchema, LoanOfferSingleSchema
from services.user.user_service import UserService
from services.loans.loans_serivce import LoansService
import models.db_utils as db_utils

bp = Blueprint('debtor', __name__)
#loans_schema = LoansSchema()
user_service = UserService()
loan_offer_schema = LoanOfferSchema()
loans_service = LoansService()

@bp.route('/<int:debtor_id>/loan-offer', methods=['POST'])
@jwt_required()
def add_new_loan_offer(debtor_id):
    try:
        # Extract the user's ID from the JWT payload
        current_user_id = get_jwt_identity()
        # we need to get user id from the debtor id. They should be the same but this is an extra check 
        user = user_service.get_user_from_debtor_id(debtor_id)
        user_id = user.userID

        # Check if the current user's ID matches the user_id in the URL
        if current_user_id != user_id:
            return jsonify({"message": "You are not authorized to add a loan offer for another user"}), 403
        
        loan_offer_request = request.json
        loan_offer_request['debtorID'] = debtor_id
        loan_offer_request['lenderID'] = user.lender.lenderID

        loan_offer = loan_offer_schema.load(loan_offer_request)
        loans_service.add_new_loan_offer(loan_offer)
        return jsonify({"message": "Loan Offer Added Successfully"}), 200
        
    except Exception as e:
        return jsonify({"message": "Loan Offer Creation Failed: " + str(e)}), 500
    
@bp.route('/<int:debtor_id>/loan-offers', methods=['GET'])
@jwt_required()
def get_all_loans_offers(debtor_id):
    try:
        with db_utils.session_scope() as session:
            # Extract the user's ID from the JWT payload
            current_user_id = get_jwt_identity()
            # we need to get user id from the debtor id. They should be the same but this is an extra check 
            user = user_service.get_user_from_debtor_id(debtor_id)
            user_id = user.userID

            # Check if the current user's ID matches the user_id in the URL
            if current_user_id != user_id:
                return jsonify({"message": "You are not authorized to view loan offers for another user"}), 403
            
            loan_offers = loans_service.get_loan_offers_by_debtor(session, debtor_id)
            serialized_loan_offers = LoanOfferSingleSchema(many=True).dump(loan_offers)
            return jsonify(serialized_loan_offers), 200
        
    except Exception as e:
        return jsonify({"message": "Loan Offers By Debtor get failed: " + str(e)}), 500


@bp.route('/<int:debtor_id>/loan-offers/<int:loan_offer_id>', methods=['PUT'])
@jwt_required()
def update_loan_offer(debtor_id, loan_offer_id):
    try:
        # Extract the user's ID from the JWT payload
        current_user_id = get_jwt_identity()

        # we need to get user id from the debtor id. They should be the same but this is an extra check 
        user = user_service.get_user_from_debtor_id(debtor_id)
        user_id = user.userID

        # Check if the current user's ID matches the user_id in the URL
        if current_user_id != user_id:
            return jsonify({"message": "You are not authorized to edit a loan offer for another user"}), 403

        # Get a loan offer using the loans service
        loan_offer = loans_service.get_loan_offer(loan_offer_id)

        if loan_offer:

            loan_offer_request = request.json
            loan_offer_request['debtorID'] = debtor_id
            loan_offer_request['lenderID'] = user.lender.lenderID
            loan_offer_request['loanAdvertisementID'] = loan_offer.loanAdvertisement.loanAdvertisementID

            # Deserialize the incoming JSON data containing bank details
            loan_offer_data = loan_offer_schema.load(loan_offer_request)
            # edit the bank information using the bankService
            loan_offer = loans_service.update_loan_offer(loan_offer, loan_offer_data)

            return jsonify({"message": "Loan offer updated successfully"}), 200

        else:
            return jsonify({"message": "Loan offer does not exist to edit"}), 404
        
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"message": "Loan offer edit failed: " + str(e)}), 500

@bp.route('/<int:debtor_id>/loan-offers/<int:loan_offer_id>', methods=['DELETE'])
@jwt_required()
def delete_loan_offer(debtor_id, loan_offer_id):
    try:
        with db_utils.session_scope() as session:
            # Extract the user's ID from the JWT payload
            current_user_id = get_jwt_identity()
            # we need to get user id from the debtor id. They should be the same but this is an extra check 
            user = user_service.get_user_from_debtor_id(debtor_id)
            user_id = user.userID

            # Check if the current user's ID matches the user_id in the URL
            if current_user_id != user_id:
                return jsonify({"message": "You are not authorized to delete a loan offer for another user"}), 403
            
            no_loan_offer = loans_service.delete_loan_offer(loan_offer_id)
            if no_loan_offer:
                return jsonify({"message": "loan offer deleted successfully"}), 200
            else:
                return jsonify({"message": "loan offer does not exist to delete"}), 404
        
    except Exception as e:
        return jsonify({"message": "Loan Offers By Debtor delete failed: " + str(e)}), 500
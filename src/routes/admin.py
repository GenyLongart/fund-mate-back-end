from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.admin.payment_frequency_schema import PaymentFrequencySchema
from schemas.admin.offer_status_schema import OfferStatusSchema
from schemas.admin.bank_schema import BankSchema
from schemas.admin.account_type_schema import AccountTypeSchema
from services.admin.payment_frequency_type_service import PaymentFrequencyTypeService
from services.admin.offer_status_type_service import OfferStatusTypeService
from services.admin.bank_service import BankService
from services.admin.account_type_service import AccountTypeService

bp = Blueprint('admin', __name__)
payment_frequency_type_schema = PaymentFrequencySchema()
payment_frequency_type_service = PaymentFrequencyTypeService()
offer_status_type_schema = OfferStatusSchema()
offer_status_type_service = OfferStatusTypeService()
bank_schema = BankSchema()
bank_service = BankService()
account_type_schema = AccountTypeSchema()
account_type_service = AccountTypeService()

@bp.route('/payment-frequency', methods=['POST'])
@jwt_required()
def add_payment_type():
    try:
        payment_frequency_type = payment_frequency_type_schema.load(request.json)
        payment_frequency_type = payment_frequency_type_schema.load(payment_frequency_type)
        payment_frequency_type_service.add_payment_frequency_type(payment_frequency_type)
        return jsonify({"message": "Payment Frequency Type Added Successfully"}), 200

    except Exception as e:
        return jsonify({"message": "Payment Frequency Type Add Failed: " + str(e)}), 500
    
@bp.route('/payment-frequencies', methods=['GET'])
def get_payment_frequency_types():
    try:
        payment_types = payment_frequency_type_service.get_all_payment_frequency_types()
        if payment_types:
            serialized_payment_frequency_types = PaymentFrequencySchema(many=True).dump(payment_types)
            return jsonify(serialized_payment_frequency_types), 200
        else:
            return jsonify({"error": "Failed to get payment frequency types, please try again"}), 404

    except Exception as e:
        return jsonify({"message": "Payment Frequency Type Get Failed: " + str(e)}), 500

@bp.route('/payment-frequencies/<int:payment_frequency_id>', methods=['DELETE'])
def delete_payment_frequency(payment_frequency_id):
    try:
        no_payment_frequency = payment_frequency_type_service.delete_payment_frequency_type(payment_frequency_id)
        if no_payment_frequency:
            return jsonify({"message": "Payment Frequency Deleted Successfully"}), 200
        else:
            return jsonify({"message": "Payment Frequency does not exist to delete"}), 404

    except Exception as e:
        return jsonify({"message": "Payment Frequency Type Delete Failed: " + str(e)}), 500

@bp.route('/offer-status', methods=['POST'])
@jwt_required()
def add_offer_status_type():
    try:
        offer_status_type = offer_status_type_schema.load(request.json)
        offer_status_type = offer_status_type_schema.load(offer_status_type)
        offer_status_type_service.add_offer_status_type(offer_status_type)
        return jsonify({"message": "Offer Status Type Added Successfully"}), 200

    except Exception as e:
        return jsonify({"message": "Offer Status Type Add Failed: " + str(e)}), 500
    
@bp.route('/offer-status', methods=['GET'])
@jwt_required()
def get_offer_status_types():
    try:
        offer_status = offer_status_type_service.get_all_offer_status_types()
        if offer_status:
            serialized_offer_status_types = OfferStatusSchema(many=True).dump(offer_status)
            return jsonify(serialized_offer_status_types), 200
        else:
            return jsonify({"error": "Failed to get offer status types, please try again"}), 404

    except Exception as e:
        return jsonify({"message": "Offer Status Type Get Failed: " + str(e)}), 500

@bp.route('/offer-status/<int:offer_status_id>', methods=['DELETE'])
def delete_offer_status(offer_status_id):
    try:
        no_offer_status = offer_status_type_service.delete_offer_status_type(offer_status_id)
        if no_offer_status:
            return jsonify({"message": "Offer Status Deleted Successfully"}), 200
        else:
            return jsonify({"message": "Offer Status does not exist to delete"}), 404

    except Exception as e:
        return jsonify({"message": "Offer Status Type Delete Failed: " + str(e)}), 500
    
@bp.route('/bank', methods=['POST'])
@jwt_required()
def add_bank():
    try:
        bank = bank_schema.load(request.json)
        bank = bank_schema.load(bank)
        bank_service.add_bank(bank)
        return jsonify({"message": "Bank Added Successfully"}), 200

    except Exception as e:
        return jsonify({"message": "Bank Add Failed: " + str(e)}), 500
    
@bp.route('/bank', methods=['GET'])
def get_banks():
    try:
        banks = bank_service.get_all_banks()
        if banks:
            serialized_banks = BankSchema(many=True).dump(banks)
            return jsonify(serialized_banks), 200
        else:
            return jsonify({"error": "Failed to get banks, please try again"}), 404

    except Exception as e:
        return jsonify({"message": "Bank Get Failed: " + str(e)}), 500
    
@bp.route('/bank/<int:bank_id>', methods=['DELETE'])
def delete_bank(bank_id):
    try:
        no_bank = bank_service.delete_bank(bank_id)
        if no_bank:
            return jsonify({"message": "Bank Deleted Successfully"}), 200
        else:
            return jsonify({"message": "Bank does not exist to delete"}), 404

    except Exception as e:
        return jsonify({"message": "Bank Delete Failed: " + str(e)}), 500
    
@bp.route('/account-type', methods=['POST'])
@jwt_required()
def add_account_type():
    try:
        account_type = account_type_schema.load(request.json)
        account_type = account_type_schema.load(account_type)
        account_type_service.add_account_type(account_type)
        return jsonify({"message": "Account Type Added Successfully"}), 200

    except Exception as e:
        return jsonify({"message": "Account Type Add Failed: " + str(e)}), 500
    
@bp.route('/account-type', methods=['GET'])
def get_account_types():
    try:
        account_types = account_type_service.get_all_account_types()
        if account_types:
            serialized_account_types = AccountTypeSchema(many=True).dump(account_types)
            return jsonify(serialized_account_types), 200
        else:
            return jsonify({"error": "Failed to get account types, please try again"}), 404

    except Exception as e:
        return jsonify({"message": "Account Type Get Failed: " + str(e)}), 500
    
@bp.route('/account-type/<int:account_type_id>', methods=['DELETE'])
def delete_account_type(account_type_id):
    try:
        no_account_type = account_type_service.delete_account_type(account_type_id)
        if no_account_type:
            return jsonify({"message": "Account Type Deleted Successfully"}), 200
        else:
            return jsonify({"message": "Account Type does not exist to delete"}), 404

    except Exception as e:
        return jsonify({"message": "Account Type Delete Failed: " + str(e)}), 500
    
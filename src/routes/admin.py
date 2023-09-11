from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.admin.payment_frequency_schema import PaymentFrequencySchema
from schemas.admin.offer_status_schema import OfferStatusSchema
from services.admin.payment_frequency_type_service import PaymentFrequencyTypeService
from services.admin.offer_status_type_service import OfferStatusTypeService

bp = Blueprint('admin', __name__)
payment_frequency_type_schema = PaymentFrequencySchema()
payment_frequency_type_service = PaymentFrequencyTypeService()
offer_status_type_schema = OfferStatusSchema()
offer_status_type_service = OfferStatusTypeService()

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
@jwt_required()
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
    
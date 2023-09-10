from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.admin.payment_frequency_schema import PaymentFrequencySchema
from services.admin.payment_frequency_type_service import PaymentFrequencyTypeService

bp = Blueprint('admin', __name__)
payment_frequency_type_schema = PaymentFrequencySchema()
payment_frequency_type_service = PaymentFrequencyTypeService()

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
    
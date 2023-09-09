from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas.admin.payment_type_schema import PaymentTypeSchema
from services.admin.payment_type_service import PaymentTypeService

bp = Blueprint('admin', __name__)
payment_type_schema = PaymentTypeSchema()
payment_type_service = PaymentTypeService()

@bp.route('/payment-type', methods=['POST'])
@jwt_required()
def add_payment_type():
    try:
        payment_type = payment_type_schema.load(request.json)
        payment_type = payment_type_schema.load(payment_type)
        payment_type_service.add_payment_type(payment_type)
        return jsonify({"message": "PaymentType Added Successfully"}), 200

    except Exception as e:
        return jsonify({"message": "PaymentType Add Failed: " + str(e)}), 500
    
@bp.route('/payment-types', methods=['GET'])
@jwt_required()
def get_payment_types():
    try:
        payment_types = payment_type_service.get_all_payment_types()
        if payment_types:
            print(payment_types)
            # Serialize the new user using the UserSchema and return a success response
            serialized_payment_types = PaymentTypeSchema(many=True).dump(payment_types)
            print(serialized_payment_types)
            return jsonify(serialized_payment_types), 200
        else:
            return jsonify({"error": "Failed to get payment types, please try again"}), 404

    except Exception as e:
        return jsonify({"message": "PaymentType Add Failed: " + str(e)}), 500
    
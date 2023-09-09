from marshmallow import Schema, fields, validate

class PaymentTypeSchema(Schema):
    paymentTypeID = fields.Int(dump_only=True)
    paymentType = fields.Str(required=True, validate=validate.Length(max=30))
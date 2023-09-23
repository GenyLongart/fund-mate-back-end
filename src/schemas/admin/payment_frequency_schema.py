from marshmallow import Schema, fields, validate

class PaymentFrequencySchema(Schema):
    paymentFrequencyID = fields.Int(dump_only=True)
    frequency = fields.Str(required=True, validate=validate.Length(max=30))
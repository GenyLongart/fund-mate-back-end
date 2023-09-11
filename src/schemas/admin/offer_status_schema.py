from marshmallow import Schema, fields, validate

class OfferStatusSchema(Schema):
    offerStatusID = fields.Int(dump_only=True)
    status = fields.Str(required=True, validate=validate.Length(max=30))
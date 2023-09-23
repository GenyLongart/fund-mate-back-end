from marshmallow import Schema, fields, validate

class BankSchema(Schema):
    bankID = fields.Int(dump_only=True)
    bankName = fields.Str(required=True, validate=validate.Length(max=30))
from marshmallow import Schema, fields, validate

class BankSchema(Schema):
    bankAccountNumber = fields.Str(required=True, validate=validate.Length(min=8, max=8))
    bankNameID = fields.Int(required=True)
    accountTypeID = fields.Int(required=True)
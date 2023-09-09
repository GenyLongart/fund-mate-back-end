from marshmallow import Schema, fields, validate

class BankSchema(Schema):
    bankName = fields.Str(required=True, validate=validate.Length(max=100))
    bankCardNumber = fields.Str(required=True, validate=validate.Length(min=16, max=16))
    bankAccountNumber = fields.Str(required=True, validate=validate.Length(min=8, max=8))
    bankSortCode = fields.Str(required=True, validate=validate.Length(min=6, max=6))
    bankIssueDate = fields.Date(required=True)
    bankExpiryDate = fields.Date(required=True)
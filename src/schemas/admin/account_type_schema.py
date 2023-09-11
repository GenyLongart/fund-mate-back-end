from marshmallow import Schema, fields, validate

class AccountTypeSchema(Schema):
    accountTypeID = fields.Int(dump_only=True)
    accountName = fields.Str(required=True, validate=validate.Length(max=30))
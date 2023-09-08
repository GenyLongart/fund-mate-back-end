from marshmallow import Schema, fields, validate

class PhoneSchema(Schema):
    phoneNumber = fields.Str(required=True, validate=validate.Length(max=20))
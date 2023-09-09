from marshmallow import Schema, fields, validate

class GetSingleUserSchema(Schema):
    userID = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(max=100))
    firstName = fields.Str(required=True, validate=validate.Length(max=50))
    lastName = fields.Str(required=True, validate=validate.Length(max=50))
    email = fields.Email(required=True, validate=validate.Length(max=100))
    profilePictureLink = fields.Str()

    # Define nested fields for related objects
    lender = fields.Nested('LenderSchema', exclude=('user',))
    debtor = fields.Nested('DebtorSchema', exclude=('user',))  
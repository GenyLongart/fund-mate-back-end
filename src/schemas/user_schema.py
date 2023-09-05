from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    userID = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(max=100))
    password = fields.Str(required=True, validate=validate.Length(max=120))
    firstName = fields.Str(required=True, validate=validate.Length(max=50))
    lastName = fields.Str(required=True, validate=validate.Length(max=50))
    email = fields.Email(required=True, validate=validate.Length(max=100))
    phoneNumber = fields.Str(required=True, validate=validate.Length(max=20))

    # Define nested fields for related objects
    googleOAuth = fields.Nested('GoogleOAuthSchema', exclude=('user',), allow_none=True)
    identity = fields.Nested('IdentitySchema', exclude=('user',), allow_none=True)
    bankDetails = fields.Nested('BankDetailsSchema', exclude=('user',), allow_none=True)
    # ... Add other nested fields as needed

class GoogleOAuthSchema(Schema):
    googleID = fields.Int(dump_only=True)
    googleOAuthID = fields.Str(required=True)
    googleName = fields.Str(required=True)
    googleProfilePicture = fields.Str(allow_none=True)
    user = fields.Nested('UserSchema', exclude=('googleOAuth',), allow_none=True)

class IdentitySchema(Schema):
    identityID = fields.Int(dump_only=True)
    identityNumber = fields.Str(required=True)
    identityDocumentLink = fields.Str(required=True)
    identityFileName = fields.Str(required=True)
    identityType = fields.Str(required=True)
    user = fields.Nested('UserSchema', exclude=('identity',), allow_none=True)

class BankDetailsSchema(Schema):
    bankID = fields.Int(dump_only=True)
    bankName = fields.Str(required=True)
    bankCardNumber = fields.Str(required=True)
    bankAccountNumber = fields.Str(required=True)
    bankSortCode = fields.Str(required=True)
    bankIssueDate = fields.DateTime(required=True)
    bankExpiryDate = fields.DateTime(required=True)
    user = fields.Nested('UserSchema', exclude=('bankDetails',), allow_none=True)




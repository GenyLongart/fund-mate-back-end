from marshmallow import Schema, fields, validate, validates_schema
from ..master_schema import MasterSchema

class UserSchema(Schema):
    userID = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(max=100))
    password = fields.Str(required=True, validate=validate.Length(max=120))
    firstName = fields.Str(required=True, validate=validate.Length(max=50))
    lastName = fields.Str(required=True, validate=validate.Length(max=50))
    email = fields.Email(required=True, validate=validate.Length(max=100))
    phoneNumber = fields.Str(required=True, validate=validate.Length(max=20))
    profilePictureLink = fields.Str()

    # Define nested fields for related objects
    googleOAuth = fields.Nested('GoogleOAuthSchema', exclude=('user',), allow_none=True)
    identity = fields.Nested('IdentitySchema', exclude=('user',), required=True)
    dicom = fields.Nested('DicomSchema', exclude=('user',))
    bankDetails = fields.Nested('BankDetailsSchema', exclude=('user',), required=True)
    lender = fields.Nested('LenderSchema', exclude=('user',))
    debtor = fields.Nested('DebtorSchema', exclude=('user',))
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
    identityDocumentLink = fields.Str()
    identityFileName = fields.Str(required=True)
    identityFile = fields.Field(metadata={'type': 'string', 'format': 'byte'}, required=True)
    identityType = fields.Str(required=True)
    user = fields.Nested('UserSchema', exclude=('identity',), allow_none=True)

    @validates_schema
    def masterSchemaInvoke(self, in_data, **kwargs):
        masterSchema = MasterSchema()
        return masterSchema.validate_uploaded_file(in_data, "identityFile", ["application/pdf", "image/png", "image/jpeg"])

class DicomSchema(Schema):
    dicomID = fields.Int(dump_only=True)
    dicomDocumentLink = fields.Str()
    dicomFileName = fields.Str(required=True)
    dicomFile = fields.Field(metadata={'type': 'string', 'format': 'byte'}, required=True)
    user = fields.Nested('UserSchema', exclude=('dicom',), allow_none=True)

    @validates_schema
    def masterSchemaInvoke(self, in_data, **kwargs):
        masterSchema = MasterSchema()
        return masterSchema.validate_uploaded_file(in_data, "dicomFile", ["application/pdf", "image/png", "image/jpeg"])

class BankDetailsSchema(Schema):
    bankID = fields.Int(dump_only=True)
    bankName = fields.Str(required=True)
    bankCardNumber = fields.Str(required=True, validate=validate.Length(min=16, max=16))
    bankAccountNumber = fields.Str(required=True, validate=validate.Length(min=8, max=8))
    bankSortCode = fields.Str(required=True, validate=validate.Length(min=6, max=6))
    bankIssueDate = fields.Date(required=True)
    bankExpiryDate = fields.Date(required=True)
    user = fields.Nested('UserSchema', exclude=('bankDetails',), allow_none=True)

class LenderSchema(Schema):
    lenderID = fields.Int(dump_only=True)
    user = fields.Nested('UserSchema', exclude=('lender',), allow_none=True)

class DebtorSchema(Schema):
    debtorID = fields.Int(dump_only=True)
    user = fields.Nested('UserSchema', exclude=('debtor',), allow_none=True)
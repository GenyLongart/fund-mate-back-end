from marshmallow import Schema, Field, fields, validate, FileStorage, ValidationError

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
    identity = fields.Nested('IdentitySchema', exclude=('user',), required=True)
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
    identityFile = Field(metadata={'type': 'string', 'format': 'byte'}, required=True)
    identityType = fields.Str(required=True)
    user = fields.Nested('UserSchema', exclude=('identity',), allow_none=True)

    @validates_schema
    def validate_uploaded_file(self, in_data, **kwargs):
        errors = {}
        file: FileStorage = in_data.get("identityFile", None)

        if file is None:
            # if any file is not uploaded, skip validation
            pass

        elif type(file) != FileStorage:
            errors["identityFile"] = [
                f"Invalid content. Only PNG, JPG/JPEG files accepted"]
            raise ValidationError(errors)

        elif file.content_type not in {"image/jpeg", "image/png"}:
            errors["identityFile"] = [
                f"Invalid file_type: {file.content_type}. Only PNG, JPG/JPEG images accepted."]
            raise ValidationError(errors)

        return in_data

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



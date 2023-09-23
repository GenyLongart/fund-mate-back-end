from marshmallow import Schema, fields, validate
from ..master_schema import MasterSchema

class LoanAdvertisementSchema(Schema):
    loanAdvertisementID = fields.Int(dump_only=True)
    amount = fields.Number(required=True)
    createdAt = fields.Date(required=True)
    updatedAt = fields.Date(required=True)
    interest = fields.Int(required=True)
    negotiable = fields.Boolean(required=True)
    description = fields.Str(required=True, validate=validate.Length(max=200))
    dueDate = fields.Date(required=True)
    paymentFrequencyID = fields.Int(required=True)
    lenderID = fields.Int(required=True)

    # Define nested fields for related objects
    lender = fields.Nested('LenderSchema')
    paymentFrequency = fields.Nested('PaymentFrequencySchema')
    transactions = fields.Nested('TransactionSchema', exclude=('loanAdvertisment',))

class LoanAdvertismentListSchema(Schema):
    amount = fields.Number(required=True)
    dueDate = fields.Date(required=True)
    interest = fields.Int(required=True)
    lender = fields.Nested('SimplifiedLenderSchema')
    loanAdvertisementID = fields.Int(required=True)
    negotiable = fields.Boolean(required=True)
    paymentFrequency = fields.Nested('PaymentFrequencySchema')
    loanOffers = fields.Nested('LoanOfferSingleSchema', many=True, exclude=('loanAdvertisement', 'lender'))

class LoanAdvertisementSingleSchema(Schema):
    loanAdvertisementID = fields.Int(dump_only=True)
    amount = fields.Number(required=True)
    createdAt = fields.Date(required=True)
    updatedAt = fields.Date(required=True)
    interest = fields.Int(required=True)
    negotiable = fields.Boolean(required=True)
    description = fields.Str(required=True, validate=validate.Length(max=200))
    dueDate = fields.Date(required=True)
    paymentFrequency = fields.Nested('PaymentFrequencySchema')
    lender = fields.Nested('SimplifiedLenderSchema')
    loanOffers = fields.Nested('LoanOfferSingleSchema', many=True, exclude=('loanAdvertisement', 'lender'))

class SimplifiedLenderSchema(Schema):
    lenderID = fields.Int(required=True)
    user = fields.Nested('SimplifiedUserSchema')

class SimplifiedUserSchema(Schema):
    firstName = fields.Str(required=True)
    lastName = fields.Str(required=True)
    profilePictureLink = fields.Str()
    userID = fields.Int(required=True)
    username = fields.Str(required=True)
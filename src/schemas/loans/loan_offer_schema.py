from marshmallow import Schema, fields, validate
from ..master_schema import MasterSchema

class LoanOfferSchema(Schema):
    loanOfferID = fields.Int(dump_only=True)
    loanAdvertisementID = fields.Int(required=True)
    debtorID = fields.Int(required=True)
    createdAt = fields.Date(required=True)
    updatedAt = fields.Date(required=True)
    interest = fields.Int(required=True)
    comment = fields.Str()
    dueDate = fields.Date(required=True)
    paymentFrequencyID = fields.Int(required=True)
    offerStatusID = fields.Int(required=True)
    lenderID = fields.Int(required=True)

    # Define nested fields for related objects
    debtor = fields.Nested('DebtorSchema')
    paymentFrequency = fields.Nested('PaymentFrequencySchema')
    offerStatus = fields.Nested('OfferStatusSchema')

class LoanOfferSingleSchema(Schema):
    loanOfferID = fields.Int(dump_only=True)
    createdAt = fields.Date(required=True)
    updatedAt = fields.Date(required=True)
    interest = fields.Int(required=True)
    comment = fields.Str()
    dueDate = fields.Date(required=True)

    loanAdvertisement = fields.Nested('LoanAdvertisementSingleSchema', exclude=('loanOffers', 'lender'))
    paymentFrequency = fields.Nested('PaymentFrequencySchema')
    debtor = fields.Nested('SimplifiedDebtorSchema')
    lender = fields.Nested('SimplifiedLenderSchema')
    offerStatus = fields.Nested('OfferStatusSchema')

class SimplifiedDebtorSchema(Schema):
    debtorID = fields.Int(required=True)
    user = fields.Nested('SimplifiedUserSchema')
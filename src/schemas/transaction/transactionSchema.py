from marshmallow import Schema, fields, validate
from ..master_schema import MasterSchema

class TransactionSchema(Schema):
    transactionID = fields.Int(dump_only=True)
    createdAt = fields.Date(required=True)
    updatedAt = fields.Date(required=True)
    originalAmount = fields.Number(required=True)
    amountDue = fields.Number(required=True)
    interest = fields.Int(required=True)
    dueDate = fields.Date(required=True)

    # Define nested fields for related objects
    loanAdvertisment = fields.Nested('TransactionStatusSchema', exclude=('Transaction',), allow_none=True)
    lender = fields.Nested('LenderSchema', exclude=('user',))
    debtor = fields.Nested('DebtorSchema', exclude=('user',))
    paymentFrequency = fields.Nested('PaymentFrequencySchema')
    transactionStatus = fields.Nested('TransactionStatusSchema')
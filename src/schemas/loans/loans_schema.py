from marshmallow import Schema, fields, validate
from ..master_schema import MasterSchema

class LoansSchema(Schema):
    loanAdvertisementID = fields.Int(dump_only=True)
    amount = fields.Number(required=True)
    createdAt = fields.Date(required=True)
    updatedAt = fields.Date(required=True)
    interest = fields.Int(required=True)
    negotiable = fields.Boolean(required=True)
    description = fields.Str(required=True, validate=validate.Length(max=200))
    dueDate = fields.Date(required=True)

    # Define nested fields for related objects
    lender = fields.Nested('LenderSchema')
    transactions = fields.Nested('TransactionSchema', exclude=('loanAdvertisment',))
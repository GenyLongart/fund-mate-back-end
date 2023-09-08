from sqlalchemy import Column, Integer, DateTime, Numeric, ForeignKey
from ..base import Base

class Transaction(Base):
    __tablename__ = 'Transaction'

    transactionID = Column(Integer, primary_key=True, autoincrement=True)
    loanAdvertisementID = Column(Integer, ForeignKey('LoanAdvertisement.loanAdvertisementID'), nullable=False)
    lenderID = Column(Integer, ForeignKey('Lender.lenderID'), nullable=False)
    debtorID = Column(Integer, ForeignKey('Debtor.debtorID'), nullable=False)
    createdAt = Column(DateTime(), nullable=False)
    updatedAt = Column(DateTime(), nullable=False )
    originalAmount = Column(Numeric, nullable=False)
    amountDue = Column(Numeric, nullable=False)
    interest = Column(Integer, nullable=False)
    dueDate = Column(DateTime(), nullable=False)
    paymentFrequency = Column(Integer, ForeignKey('PaymentFrequency.paymentFrequencyID'), nullable=False)
    transactionStatus = Column(Integer, ForeignKey('TransactionStatus.transactionStatusID'), nullable=False)
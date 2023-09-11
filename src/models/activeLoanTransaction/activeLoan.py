from sqlalchemy import Column, Integer, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base

class ActiveLoan(Base):
    __tablename__ = 'ActiveLoan'

    activeLoanID = Column(Integer, primary_key=True, autoincrement=True)
    loanAdvertisementID = Column(Integer, ForeignKey('LoanAdvertisement.loanAdvertisementID'), nullable=False)
    lenderID = Column(Integer, ForeignKey('Lender.lenderID'), nullable=False)
    debtorID = Column(Integer, ForeignKey('Debtor.debtorID'), nullable=False)
    createdAt = Column(DateTime(), nullable=False)
    updatedAt = Column(DateTime(), nullable=False )
    originalAmount = Column(Numeric, nullable=False)
    amountDue = Column(Numeric, nullable=False)
    interest = Column(Integer, nullable=False)
    dueDate = Column(DateTime(), nullable=False)
    paymentFrequencyID = Column(Integer, ForeignKey('PaymentFrequency.paymentFrequencyID'), nullable=False)
    paymentFrequency = relationship("PaymentFrequency", back_populates="activeLoans")
    transactionStatus = Column(Integer, ForeignKey('TransactionStatus.transactionStatusID'), nullable=False)
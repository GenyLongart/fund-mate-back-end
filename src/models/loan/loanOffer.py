from sqlalchemy import Column, Integer, DateTime, ForeignKey
from ..base import Base

class LoanOffer(Base):
    __tablename__ = 'LoanOffer'

    loanOfferID = Column(Integer, primary_key=True, autoincrement=True)
    loanAdvertisementID = Column(Integer, ForeignKey('LoanAdvertisement.loanAdvertisementID'), nullable=False)
    lenderID = Column(Integer, ForeignKey('Lender.lenderID'), nullable=False)
    debtorID = Column(Integer, ForeignKey('Debtor.debtorID'), nullable=False)
    createdAt = Column(DateTime(), nullable=False)
    updatedAt = Column(DateTime(), nullable=False )
    interest = Column(Integer, nullable=False)
    dueDate = Column(DateTime(), nullable=False)
    paymentFrequency = Column(Integer, ForeignKey('PaymentFrequency.paymentFrequencyID'), nullable=False)
    offerStatus = Column(Integer, ForeignKey('OfferStatus.offerStatusID'), nullable=False)

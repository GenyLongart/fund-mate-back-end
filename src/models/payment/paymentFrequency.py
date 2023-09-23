from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..base import Base

class PaymentFrequency(Base):
    __tablename__ = 'PaymentFrequency'

    paymentFrequencyID = Column(Integer, primary_key=True, autoincrement=True)
    frequency = Column(String(30), nullable=False)

    # Define a relationship to LoanAdvertisement, LoanOffer, and ActiveLoan
    loanAdvertisements = relationship("LoanAdvertisement", back_populates="paymentFrequency")
    loanOffers = relationship("LoanOffer", back_populates="paymentFrequency")
    activeLoans = relationship("ActiveLoan", back_populates="paymentFrequency")
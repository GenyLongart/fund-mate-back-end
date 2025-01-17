from sqlalchemy import Column, Integer, String, Numeric, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base

class LoanAdvertisement(Base):
    __tablename__ = 'LoanAdvertisement'

    loanAdvertisementID = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Numeric(100), nullable=False)
    interest = Column(Integer, nullable=False)
    description = Column(String(200))
    dueDate = Column(DateTime(), nullable=False)
    negotiable = Column(Boolean, nullable=False)
    createdAt = Column(DateTime(), nullable=False)
    updatedAt = Column(DateTime(), nullable=False )
    paymentFrequencyID = Column(Integer, ForeignKey('PaymentFrequency.paymentFrequencyID'), nullable=False)
    paymentFrequency = relationship("PaymentFrequency", back_populates="loanAdvertisements")
    lenderID = Column(Integer, ForeignKey('Lender.lenderID'), nullable=False)
    lender = relationship("Lender", back_populates="loanAdvertisements")
    loanOffers = relationship("LoanOffer", back_populates="loanAdvertisement")

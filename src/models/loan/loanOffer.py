from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base

class LoanOffer(Base):
    __tablename__ = 'LoanOffer'

    loanOfferID = Column(Integer, primary_key=True, autoincrement=True)
    loanAdvertisementID = Column(Integer, ForeignKey('LoanAdvertisement.loanAdvertisementID'), nullable=False)
    debtorID = Column(Integer, ForeignKey('Debtor.debtorID'), nullable=False)
    debtor = relationship("Debtor", back_populates="loanOffers")
    lenderID = Column(Integer, ForeignKey('Lender.lenderID'), nullable=False)
    lender = relationship("Lender", back_populates="loanOffers")
    interest = Column(Integer, nullable=False)
    comment = Column(String)
    dueDate = Column(DateTime(), nullable=False)
    createdAt = Column(DateTime(), nullable=False)
    updatedAt = Column(DateTime(), nullable=False )
    paymentFrequencyID = Column(Integer, ForeignKey('PaymentFrequency.paymentFrequencyID'), nullable=False)
    paymentFrequency = relationship("PaymentFrequency", back_populates="loanOffers")
    offerStatusID = Column(Integer, ForeignKey('OfferStatus.offerStatusID'), nullable=False)
    offerStatus = relationship("OfferStatus", back_populates="loanOffers")
    loanAdvertisement = relationship("LoanAdvertisement", back_populates="loanOffers")
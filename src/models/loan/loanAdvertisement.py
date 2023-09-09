from sqlalchemy import Column, Integer, String, Numeric, DateTime, Boolean, ForeignKey
from ..base import Base

class LoanAdvertisement(Base):
    __tablename__ = 'LoanAdvertisement'

    loanAdvertisementID = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Numeric(100), nullable=False)
    interest = Column(Integer, nullable=False)
    description = Column(String(200))
    dueDate = Column(DateTime(), nullable=False)
    negotiable = Column(Boolean, nullable=False, unique=True)
    createdAt = Column(DateTime(), nullable=False)
    updatedAt = Column(DateTime(), nullable=False )
    paymentType = Column(Integer, ForeignKey('PaymentType.paymentTypeID'), nullable=False)
    lenderID = Column(Integer, ForeignKey('Lender.lenderID'), nullable=False)

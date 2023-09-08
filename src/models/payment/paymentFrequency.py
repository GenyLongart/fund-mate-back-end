from sqlalchemy import Column, Integer, String
from ..base import Base

class PaymentFrequency(Base):
    __tablename__ = 'PaymentFrequency'

    paymentFrequencyID = Column(Integer, primary_key=True, autoincrement=True)
    frequency = Column(String(30), nullable=False)
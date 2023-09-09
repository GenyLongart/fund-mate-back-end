from sqlalchemy import Column, Integer, String
from ..base import Base

class PaymentType(Base):
    __tablename__ = 'PaymentType'

    paymentTypeID = Column(Integer, primary_key=True, autoincrement=True)
    paymentType = Column(String(30), nullable=False)
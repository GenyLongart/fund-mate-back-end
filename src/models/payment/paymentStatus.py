from sqlalchemy import Column, Integer, String
from ..base import Base

class PaymentStatus(Base):
    __tablename__ = 'PaymentStatus'

    paymentStatusID = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String(30), nullable=False)
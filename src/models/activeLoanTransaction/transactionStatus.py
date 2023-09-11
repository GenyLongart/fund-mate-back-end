from sqlalchemy import Column, Integer, String
from ..base import Base

class TransactionStatus(Base):
    __tablename__ = 'TransactionStatus'

    transactionStatusID = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String(30), nullable=False)
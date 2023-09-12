from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..base import Base

class Bank(Base):
    __tablename__ = 'Bank'

    bankID = Column(Integer, primary_key=True, autoincrement=True)
    bankName = Column(String(30), nullable=False)
    bankDetails = relationship("BankDetails", back_populates="bank", lazy="joined")
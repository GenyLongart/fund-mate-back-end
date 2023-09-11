from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..base import Base

class AccountType(Base):
    __tablename__ = 'AccountType'

    accountTypeID = Column(Integer, primary_key=True, autoincrement=True)
    accountName = Column(String(30), nullable=False)
    bankDetails = relationship("BankDetails", back_populates="accountType")
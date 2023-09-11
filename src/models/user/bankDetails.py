from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base

class BankDetails(Base):
     __tablename__ = 'BankDetails'

     bankDetailsID = Column(Integer, primary_key=True, autoincrement=True)
     bankNameID = Column(Integer, ForeignKey('Bank.bankID'), nullable=True)
     bank = relationship("Bank", back_populates="bankDetails")
     accountTypeID = Column(Integer, ForeignKey('AccountType.accountTypeID'), nullable=True) 
     accountType = relationship("AccountType", back_populates="bankDetails")
     bankAccountNumber = Column(String(8), nullable=False)
     userID = Column(Integer, ForeignKey('User.userID'))
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base

class BankDetails(Base):
     __tablename__ = 'BankDetails'

     bankDetailsID = Column(Integer, primary_key=True, autoincrement=True)
     bankNameID = Column(Integer, ForeignKey('Bank.bankID'), nullable=False)
     bank = relationship("Bank", back_populates="bankDetails", lazy="joined")
     accountTypeID = Column(Integer, ForeignKey('AccountType.accountTypeID'), nullable=False) 
     accountType = relationship("AccountType", back_populates="bankDetails", lazy="joined")
     bankAccountNumber = Column(String(8), nullable=False)
     userID = Column(Integer, ForeignKey('User.userID'))
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from .base import Base

class BankDetails(Base):
     __tablename__ = 'BankDetails'

     bankID = Column(Integer, primary_key=True, autoincrement=True)
     bankName = Column(String, nullable=False)
     bankCardNumber = Column(String(16), nullable=False)
     bankAccountNumber = Column(String(8), nullable=False)
     bankSortCode = Column(String(6), nullable=False)
     bankIssueDate = Column(DateTime, nullable=False)
     bankExpiryDate = Column(DateTime, nullable=False)
     userID = Column(Integer, ForeignKey('User.userID'))
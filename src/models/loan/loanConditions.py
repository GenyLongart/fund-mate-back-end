from sqlalchemy import Column, Integer, String, ForeignKey
from ..base import Base

class LoanConditions(Base):
    __tablename__ = 'LoanConditions'

    loanConditionID = Column(Integer, primary_key=True, autoincrement=True)
    loanAdvertisementID = Column(Integer, ForeignKey('LoanAdvertisement.loanAdvertisementID'), nullable=False)
    loanConditionDescription = Column(String(200), nullable=False)
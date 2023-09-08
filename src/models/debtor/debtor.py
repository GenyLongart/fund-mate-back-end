from sqlalchemy import Column, Integer, ForeignKey
from ..base import Base

class Debtor(Base):
    __tablename__ = 'Debtor'

    debtorID = Column(Integer, primary_key=True, autoincrement=True)
    userID = Column(Integer, ForeignKey('User.userID'), nullable=False)
from sqlalchemy import Column, Integer, ForeignKey
from .base import Base

class Lender(Base):
    __tablename__ = 'Lender'

    lenderID = Column(Integer, primary_key=True, autoincrement=True)
    userID = Column(Integer, ForeignKey('User.userID'), nullable=False)
from sqlalchemy import Column, Integer, String
from ..base import Base

class OfferStatus(Base):
    __tablename__ = 'OfferStatus'

    offerStatusID = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String(30), nullable=False)
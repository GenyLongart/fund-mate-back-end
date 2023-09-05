from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class Identity(Base):
    __tablename__ = 'Identity'

    identityID = Column(Integer, primary_key=True, autoincrement=True)
    identityNumber = Column(String(20), nullable=False)
    identityDocumentLink = Column(String, nullable=False)
    identityFileName = Column(String(50), nullable=False)
    identityType = Column(String(15), nullable=False)
    userID = Column(Integer, ForeignKey('User.userID'))
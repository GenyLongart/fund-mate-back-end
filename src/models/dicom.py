from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class Dicom(Base):
    __tablename__ = 'Dicom'

    dicomID = Column(Integer, primary_key=True, autoincrement=True)
    dicomDocumentLink = Column(String, nullable=False)
    dicomFileName = Column(String(50), nullable=False)
    userID = Column(Integer, ForeignKey('User.userID'))
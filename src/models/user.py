from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = 'User'

    userID = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(120), nullable=False)
    firstName = Column(String(50), nullable=False )
    lastName = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phoneNumber = Column(String(20), nullable=False)

    googleOAuth = relationship('GoogleOAuth', backref='user', uselist=False, cascade="all, delete-orphan")
    identity = relationship('Identity', backref='user', uselist=False, cascade="all, delete-orphan")
    bankDetails = relationship('BankDetails', backref='user', uselist=False, cascade="all, delete-orphan")
    lender = relationship('Lender', backref='user', uselist=False, cascade="all, delete-orphan")
    debtor = relationship('Debtor', backref='user', uselist=False, cascade="all, delete-orphan")
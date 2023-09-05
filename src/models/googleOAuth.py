from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class GoogleOAuth(Base):
    __tablename__ = 'GoogleOAuth'

    googleID = Column(Integer, primary_key=True, autoincrement=True)
    googleOAuthID = Column(String, nullable=False, unique=True)
    googleName = Column(String, nullable=False)
    googleProfilePicture = Column(String)
    userID = Column(Integer, ForeignKey('User.userID'))
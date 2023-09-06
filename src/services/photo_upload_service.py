from models import User, BankDetails, Identity, Lender, Debtor
from models.base import db
from cloudinary.uploader import upload 

class PhotoUploadService:
    def uploadPhoto(self, image, folderName):
        try:
            reponse = upload(image, folder=folderName)
            return reponse
        except Exception as e:
            return e
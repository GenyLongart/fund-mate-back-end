from models import User, BankDetails, Identity, Lender, Debtor
from models.base import db
from cloudinary import exceptions as cloudinary_exceptions
from cloudinary.uploader import upload
import cloudinary.api

class PhotoUploadService:
    def uploadPhoto(self, image, folderName):
        try:
            reponse = upload(image, folder=folderName, use_filename=True, unique_filename=False)
            return reponse
        except cloudinary_exceptions.Error as e:
            return e
        
    def deleteEntireUserFolder(self, username):
        try:
            response = cloudinary.api.delete_resources_by_prefix(username)
            response = cloudinary.api.delete_folder(username)
            return response
        except cloudinary_exceptions.Error as e:
            return e
from models import User, BankDetails, Identity, Dicom, Lender, Debtor
from models.base import db
import datetime
from ..master.photo_upload_service import PhotoUploadService
from cloudinary import exceptions as cloudinary_exceptions
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    def get_user(self, _userID):
        return User.query.filter_by(userID=_userID).first()
    
    def get_user_from_lender_id(self, _lenderID):
        lender = Lender.query.filter_by(lenderID=_lenderID).first()
        if lender:
            return User.query.filter_by(userID=lender.userID).first()
        else:
            raise Exception("error: No such Lender ID")

    def username_exists(self, _username):
        # Check if a user with the given username exists
        return User.query.filter_by(username=_username).first() is not None

    def update_phone_number(self, user, phone_data):
        user.phoneNumber = phone_data
        db.session.commit()
        return user
    
    def update_profile_picture(self, user, profile_picture):
        #upload photos here
        uploadImage = PhotoUploadService()
        uploadResponseProfilePicture = uploadImage.uploadPhoto(profile_picture, user.username + "/profile")

        # handle error upload here
        if not uploadResponseProfilePicture['secure_url']:
            raise Exception(f"Cloudinary API error: {str(uploadResponseProfilePicture)}")
        
        user.profilePictureLink = uploadResponseProfilePicture['secure_url']
        db.session.commit()
        return user

    def create_user(self, user_data):

        # Extract nested data
        bank_details_data = user_data.pop('bankDetails')
        identity_data = user_data.pop('identity')
        dicom_data = user_data.pop('dicom')

        #upload photos here
        uploadImage = PhotoUploadService()
        uploadPhotoResponseIdentity = uploadImage.uploadPhoto(identity_data['identityFile'], user_data["username"] + "/identification")
        uploadPhotoResponseDicom = uploadImage.uploadPhoto(dicom_data['dicomFile'], user_data["username"] + "/dicom")
        # handle error upload here
        if not uploadPhotoResponseIdentity['secure_url'] or not uploadPhotoResponseDicom['secure_url']:
            return
        
        # we don't need the images anymore, they are in cloud storage
        del identity_data['identityFile']
        del dicom_data['dicomFile'] 
        # modify the file paths to point towards the secure urls in cloudinary
        identity_data['identityDocumentLink'] = uploadPhotoResponseIdentity['secure_url']
        dicom_data['dicomDocumentLink'] = uploadPhotoResponseDicom['secure_url']

        # generate the password hash
        user_data["password"] = generate_password_hash(user_data["password"])

        # Create a new user and save it to the database
        new_user = User(**user_data)
        # include the default profile picture
        new_user.profilePictureLink = uploadImage.getDefaultProfilePicture()

        # Create BankDetails, Identity, Lender and Debtor instances and associate them with the new user
        bank_details = BankDetails(**bank_details_data)
        identity = Identity(**identity_data)
        dicom = Dicom(**dicom_data)
        lender = Lender()
        debtor = Debtor()

        # Associate bank_details, identity, lender and debtor with the new_user
        new_user.bankDetails = bank_details
        new_user.identity = identity
        new_user.dicom = dicom
        new_user.lender = lender
        new_user.debtor = debtor

        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    def login_user(self, _username, _password):
        #Login a user
        user_found = User.query.filter_by(username=_username).first()

        if not user_found or not check_password_hash(user_found.password, _password):
            return None

        # Generate an access token for the user
        expire = datetime.timedelta(days=1)
        access_token = create_access_token(identity=user_found.userID, expires_delta=expire)

        result = {
            "access_token": access_token,
            "user": user_found
        }

        return result

    def deleteUser(self, _userID):
        user_found = User.query.filter_by(userID=_userID).first()

        if not user_found:
            return False
        
        #delete photos here
        deletePhotoService = PhotoUploadService()
        deletePhotoResponse = deletePhotoService.deleteEntireUserFolder(user_found.username)

        # handle error upload here
        if isinstance(deletePhotoResponse, cloudinary_exceptions.Error):
            raise Exception(f"Cloudinary API error: {str(deletePhotoResponse)}")
        
        db.session.delete(user_found)
        db.session.commit()

        return True

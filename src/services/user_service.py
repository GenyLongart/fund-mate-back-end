from models import User, BankDetails, Identity, Lender, Debtor
from models.base import db
import datetime
from photo_upload_service import PhotoUploadService
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    def username_exists(self, _username):
        # Check if a user with the given username exists
        return User.query.filter_by(username=_username).first() is not None

    def create_user(self, user_data):

        # Extract nested data
        bank_details_data = user_data.pop('bankDetails')
        identity_data = user_data.pop('identity')

        uploadImage = PhotoUploadService()
        uploadPhotoResponse = uploadImage.uploadPhoto(identity_data.identityFile, user_data["username"] + "/" + identity_data["identityFileName"])

        # handle error upload here
        if not uploadPhotoResponse.status_code == 200 or not uploadPhotoResponse['secure_url']:
            return
        
        # modify the file path to point towards the secure url in cloudinary
        identity_data['identityDocumentLink'] = uploadPhotoResponse['secure_url']

        # generate the password hash
        user_data["password"] = generate_password_hash(user_data["password"])

        # Create a new user and save it to the database
        new_user = User(**user_data)

        # Create BankDetails, Identity, Lender and Debtor instances and associate them with the new user
        bank_details = BankDetails(**bank_details_data)
        identity = Identity(**identity_data)
        lender = Lender()
        debtor = Debtor()

        # Associate bank_details, identity, lender and debtor with the new_user
        new_user.bankDetails = bank_details
        new_user.identity = identity
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

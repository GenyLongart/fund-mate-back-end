from models.user import User
from models.base import db
from flask_jwt_extended import create_access_token, JWTManager
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

class UserService:
    def username_exists(self, _username):
        # Check if a user with the given username exists
        return User.query.filter_by(username=_username).first() is not None

    def create_user(self, user_data):
        #generate the password hash
        user_data["password"] = generate_password_hash(user_data["password"])

        # Create a new user and save it to the database
        new_user = User(**user_data)

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

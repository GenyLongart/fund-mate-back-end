import os
import cloudinary
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv
from models.base import db  # Import the SQLAlchemy instance from the new structure
from routes.user import bp as user_bp  # Import the blueprint for user-related routes
from routes.users import bp as users_bp
from routes.activeLoan import bp as activeLoan_bp
from routes.loans import bp as loans_bp
from routes.admin import bp as admin_bp
from routes.lender import bp as lender_bp
from routes.debtor import bp as debtor_bp

load_dotenv()

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')

# Initialize SQLAlchemy and Migrate
db.init_app(app)
Migrate(app, db)

# Initialize JWT Manager and CORS
jwt = JWTManager(app)
CORS(app)

# initialize cloudinary
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET'),
    secure=True
)

# Add the user-related blueprint
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(activeLoan_bp, url_prefix='/active-loan')
app.register_blueprint(loans_bp, url_prefix='/loans')
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(lender_bp, url_prefix='/lender')
app.register_blueprint(debtor_bp, url_prefix='/debtor')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081)


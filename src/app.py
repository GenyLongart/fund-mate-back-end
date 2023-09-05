import os
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv
from models.base import db  # Import the SQLAlchemy instance from the new structure
from routes.users import bp as users_bp  # Import the blueprint for user-related routes

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

# Add the user-related blueprint
app.register_blueprint(users_bp, url_prefix='/users')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081)


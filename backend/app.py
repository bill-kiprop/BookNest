import os
from datetime import timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from models import db

# Initialize Flask application
app = Flask(__name__)

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_ECHO'] = True

# JWT configurations
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your_jwt_secret_key')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)


migrate = Migrate(app, db)

# CORS configuration
CORS(app)

# Initialize Bcrypt
bcrypt = Bcrypt(app)

# Initialize JWTManager
jwt = JWTManager(app)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Home page</h1>'

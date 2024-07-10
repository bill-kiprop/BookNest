# this is a simple configurable file for my flask application
import os 
base_dir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SQLALCHEMY_DATABASE_URI = os.path.join(base_dir, 'app.db')
    # SQLALCHEMY_DATABASE_URI is the connection string to your database
    # Replace 'your_username', 'your_password', and 'your_database' with your actual credentials
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'postgresql://your_username:your_password@localhost/your_database'

    # JWT_SECRET_KEY is used to sign the JWT tokens
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'your_jwt_secret_key'

    # SQLALCHEMY_TRACK_MODIFICATIONS controls whether SQLAlchemy should track modifications
    # Set it to False if you want to disable this feature
    SQLALCHEMY_TRACK_MODIFICATIONS = False
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity
from .models import db, User

# Function to hash a password using SHA-256
def hash_password(password):
    """
    Hashes a plain text password using SHA-256.
    
    Args:
    - password (str): The plain text password to be hashed.

    Returns:
    - str: The hashed password.
    """
    return generate_password_hash(password, method='sha256')

# Function to check a password against its hash
def check_password(hashed_password, password):
    """
    Verifies a password against a given hashed password.
    
    Args:
    - hashed_password (str): The hashed password.
    - password (str): The plain text password to check.

    Returns:
    - bool: True if the password matches the hash, False otherwise.
    """
    return check_password_hash(hashed_password, password)

# Function to create a JWT access token
def create_token(identity):
    """
    Creates a JWT access token for a given identity.
    
    Args:
    - identity (dict): The identity information to include in the token (e.g., {'username': 'user1', 'role': 'host'}).

    Returns:
    - str: The JWT access token.
    """
    return create_access_token(identity=identity)

# Function to get the current authenticated user
def get_current_user():
    """
    Retrieves the current authenticated user based on the JWT token.
    
    Returns:
    - User: The user object of the current authenticated user.
    """
    # Get the identity from the JWT token
    identity = get_jwt_identity()
    
    # Query the user from the database using the username from the token's identity
    return User.query.filter_by(username=identity['username']).first()

import re
import logging
from flask_restful import Resource, reqparse
from flask_bcrypt import generate_password_hash
from flask_jwt_extended import create_access_token
from models import db, User

logging.basicConfig(level=logging.INFO)

class SignupResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=True, help="Name is required")
        self.parser.add_argument('email', required=True, help="Email address is required")
        self.parser.add_argument('password', required=True, help="Password is required")
    
    def post(self):
        data = self.parser.parse_args()

        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", data['email']):
            return {"message": "Invalid email format", "status": "fail"}, 400

        # Check password complexity
        if len(data['password']) < 8 or not re.search(r"\d", data['password']) or not re.search(r"[A-Z]", data['password']):
            return {"message": "Password must be at least 8 characters long and include a number and a capital letter", "status": "fail"}, 400

        # Hash the password
        hashed_password = generate_password_hash(data['password']).decode('utf-8')
        
        # Create new user data
        user_data = {
            'name': data['name'],
            'email': data['email'],
            'password': hashed_password,
            'role': 'member'
        }

        # Check if email is already taken
        if User.query.filter_by(email=user_data['email']).first():
            return {"message": "Email address already taken", "status": "fail"}, 422

        # Create new user instance
        new_user = User(**user_data)

        # Add and commit the new user to the database
        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error adding new user: {e}")
            return {"message": str(e), "status": "fail"}, 500

        logging.info(f"User registered successfully: {new_user.email}")

        # Placeholder for sending email verification
        # send_verification_email(new_user.email)

        return {"message": "User registered successfully", "status": "success", "user": new_user.to_dict()}, 201

class LoginResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', required=True, help="Email address is required")
        self.parser.add_argument('password', required=True, help="Password is required")
    
    def post(self):
        data = self.parser.parse_args()

        # Retrieve the user by email
        user = User.query.filter_by(email=data['email']).first()

        if not user or not user.check_password(data['password']):
            logging.warning(f"Failed login attempt for email: {data['email']}")
            return {"message": "Invalid email/password", "status": "fail"}, 403

        user_dict = user.to_dict()
        additional_claims = {"role": user_dict['role']}
        
        try:
            access_token = create_access_token(identity=user_dict['id'], additional_claims=additional_claims)
        except Exception as e:
            logging.error(f"Error creating access token: {e}")
            return {"message": "Failed to create access token", "status": "fail"}, 500

        logging.info(f"User logged in successfully: {user.email}")

        return {"message": "Login successful", "status": "success", "user": user_dict, "access_token": access_token}, 200

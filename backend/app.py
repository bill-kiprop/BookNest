import os
from datetime import timedelta
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from models import db, User, Property, Review

# Initialize Flask application
app = Flask(__name__)
app.config.from_object('config.Config')

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_ECHO'] = True

# Initialize database
db.init_app(app)
migrate = Migrate(app, db)

# Initialize Bcrypt
bcrypt = Bcrypt(app)

# Initialize JWTManager
jwt = JWTManager(app)

# CORS configuration
CORS(app)

# Routes

# Home page route
@app.route('/')
def home():
    return '<h1>Home page</h1>'

# User Registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], role=data['role'], images=0)
    new_user.set_password(data['password'])  # Hash the password
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

# User Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity={'username': user.username, 'role': user.role})
        return jsonify(access_token=access_token), 200
    return jsonify({"message": "Invalid credentials"}), 401

# Add Property
@app.route('/properties', methods=['POST'])
@jwt_required()
def add_property():
    data = request.get_json()
    current_user = get_jwt_identity()
    new_property = Property(host_id=current_user['id'], name=data['name'], description=data['description'], address=data['address'], images=0)
    db.session.add(new_property)
    db.session.commit()
    return jsonify({"message": "Property added successfully"}), 201

# Add Review
@app.route('/reviews', methods=['POST'])
@jwt_required()
def add_review():
    data = request.get_json()
    current_user = get_jwt_identity()
    new_review = Review(user_id=current_user['id'], property_id=data['property_id'], rating=data['rating'], comment=data['comment'])
    db.session.add(new_review)
    db.session.commit()
    return jsonify({"message": "Review added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)

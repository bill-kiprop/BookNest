import os
from datetime import timedelta
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
<<<<<<< HEAD
from models import db, User, Property, Room, Booking, Review, Profile, Amenity
import os
=======
from models import db, User, Property, Review
>>>>>>> origin/cynan

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
    username=data['username']
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"}), 400
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
        access_token = create_access_token(identity={'id': user.id, 'username': user.username, 'role': user.role})
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

# Get All Properties
@app.route('/properties', methods=['GET'])
def get_properties():
    properties = Property.query.all()
    return jsonify([p.as_dict() for p in properties]), 200

# Get Property by ID
@app.route('/properties/<int:property_id>', methods=['GET'])
def get_property(property_id):
    property = Property.query.get_or_404(property_id)
    return jsonify(property.as_dict()), 200

# Update Property
@app.route('/properties/<int:property_id>', methods=['PUT'])
@jwt_required()
def update_property(property_id):
    data = request.get_json()
    property = Property.query.get_or_404(property_id)
    property.name = data.get('name', property.name)
    property.description = data.get('description', property.description)
    property.address = data.get('address', property.address)
    db.session.commit()
    return jsonify({"message": "Property updated successfully"}), 200

# Delete Property
@app.route('/properties/<int:property_id>', methods=['DELETE'])
@jwt_required()
def delete_property(property_id):
    property = Property.query.get_or_404(property_id)
    db.session.delete(property)
    db.session.commit()
    return jsonify({"message": "Property deleted successfully"}), 200

# Add Amenity
@app.route('/amenities', methods=['POST'])
@jwt_required()
def add_amenity():
    data = request.get_json()
    new_amenity = Amenity(name=data['name'])
    db.session.add(new_amenity)
    db.session.commit()
    return jsonify({"message": "Amenity added successfully"}), 201

# Handle 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Resource not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

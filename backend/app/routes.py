from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .models import db, User, Property

# Create a blueprint for the API routes (to group the api routes together)
api_bp = Blueprint('api', __name__)

# Route for user registration
@api_bp.route('/register', methods=['POST'])
def register():
    # Get the data from the request body
    data = request.get_json()
    
    # Hash the user's password for security
    hashed_password = generate_password_hash(data['password'], method='sha256')
    
    # Create a new user instance
    new_user = User(
        username=data['username'], 
        email=data['email'], 
        password_hash=hashed_password, 
        role=data['role']

    )
    
    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    
    # Return a success message
    return jsonify({'message': 'User registered successfully!'})

# Route for user login
@api_bp.route('/login', methods=['POST'])
def login():
    # Get the data from the request body
    data = request.get_json()
    
    # Find the user by email
    user = User.query.filter_by(email=data['email']).first()
    
    # Check if user exists and password is correct
    if not user or not check_password_hash(user.password_hash, data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    # Create a JWT access token
    access_token = create_access_token(identity={'username': user.username, 'role': user.role})
    
    # Return the access token
    return jsonify({'token': access_token})

# Route to create a new property (requires authentication)
@api_bp.route('/properties', methods=['POST'])
@jwt_required()
def create_property():
    # Get the current user's identity from the JWT
    current_user = get_jwt_identity()
    
    # Find the user in the database
    user = User.query.filter_by(username=current_user['username']).first()
    
    # Check if the user has the 'host' role
    if user.role != 'host':
        return jsonify({'message': 'Permission denied'}), 403
    
    # Get the data from the request body
    data = request.get_json()
    
    # Create a new property instance
    new_property = Property(
        name=data['name'],
        description=data['description'],
        address=data['address'],
        host_id=user.id
    )
    
    # Add the new property to the database
    db.session.add(new_property)
    db.session.commit()
    
    # Return a success message
    return jsonify({'message': 'Property created successfully!'})

# Route to get all properties
@api_bp.route('/properties', methods=['GET'])
def get_properties():
    # Query all properties from the database
    properties = Property.query.all()
    
    # Return the properties as a list of dictionaries
    return jsonify([{
        'id': property.id,
        'name': property.name,
        'description': property.description,
        'address': property.address,
        'host_id': property.host_id
    } for property in properties])

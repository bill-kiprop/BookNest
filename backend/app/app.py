from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'  # Replace with your actual database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super_secret_key'

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Define your models here
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    images = db.Column(db.Integer, nullable=False)

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    host_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    images = db.Column(db.Integer, nullable=False)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Boolean, default=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    fullname = db.Column(db.Text, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    address = db.Column(db.Text, nullable=False)

# Routes and application logic
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(
        username=data['username'], 
        email=data['email'], 
        password_hash=hashed_password, 
        role=data['role']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully!'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password_hash, data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    access_token = create_access_token(identity={'username': user.username, 'role': user.role})
    return jsonify({'token': access_token})

@app.route('/properties', methods=['POST'])
@jwt_required()
def create_property():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user['username']).first()
    if user.role != 'host':
        return jsonify({'message': 'Permission denied'}), 403
    data = request.get_json()
    new_property = Property(
        name=data['name'],
        description=data['description'],
        address=data['address'],
        host_id=user.id
    )
    db.session.add(new_property)
    db.session.commit()
    return jsonify({'message': 'Property created successfully!'})

@app.route('/properties', methods=['GET'])
def get_properties():
    properties = Property.query.all()
    return jsonify([{
        'id': property.id,
        'name': property.name,
        'description': property.description,
        'address': property.address,
        'host_id': property.host_id
    } for property in properties])

# Main entry point for the application
if __name__ == "__main__":
    app.run(debug=True)

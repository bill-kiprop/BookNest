import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from models import db, User, Property, Review, Amenity, Booking, Room
from datetime import datetime

app = Flask(__name__)
app.config.from_object('config.Config')

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_ECHO'] = True

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)

# Routes

@app.route('/')
def home():
    return '<h1>Home page</h1>'

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    role = data.get('role')

    if not username or not password or not email or not role:
        return jsonify({"message": "Missing required fields"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"}), 400

    new_user = User(username=username, email=email, role=role, images=0)
    new_user.set_password(password)
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to register user", "error": str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity={'id': user.id, 'username': user.username, 'role': user.role})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/properties', methods=['POST'])
@jwt_required()
def add_property():
    data = request.get_json()
    current_user = get_jwt_identity()

    if not data or 'name' not in data or 'description' not in data or 'address' not in data:
        return jsonify({"message": "Missing required fields"}), 400

    new_property = Property(host_id=current_user['id'], name=data['name'], description=data['description'], address=data['address'], images=0)

    try:
        db.session.add(new_property)
        db.session.commit()
        return jsonify({"message": "Property added successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to add property", "error": str(e)}), 500

@app.route('/reviews', methods=['POST'])
@jwt_required()
def add_review():
    data = request.get_json()
    current_user = get_jwt_identity()

    if not data or 'property_id' not in data or 'rating' not in data or 'comment' not in data:
        return jsonify({"message": "Missing required fields"}), 400

    new_review = Review(user_id=current_user['id'], property_id=data['property_id'], rating=data['rating'], comment=data['comment'])

    try:
        db.session.add(new_review)
        db.session.commit()
        return jsonify({"message": "Review added successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to add review", "error": str(e)}), 500

@app.route('/properties', methods=['GET'])
def get_properties():
    properties = Property.query.all()
    return jsonify([p.as_dict() for p in properties]), 200

@app.route('/properties/<int:property_id>', methods=['GET'])
def get_property(property_id):
    property = Property.query.get_or_404(property_id)
    return jsonify(property.as_dict()), 200

@app.route('/properties/<int:property_id>', methods=['PUT'])
@jwt_required()
def update_property(property_id):
    data = request.get_json()
    property = Property.query.get_or_404(property_id)

    try:
        property.name = data.get('name', property.name)
        property.description = data.get('description', property.description)
        property.address = data.get('address', property.address)
        db.session.commit()
        return jsonify({"message": "Property updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to update property", "error": str(e)}), 500

@app.route('/properties/<int:property_id>', methods=['DELETE'])
@jwt_required()
def delete_property(property_id):
    property = Property.query.get_or_404(property_id)

    try:
        db.session.delete(property)
        db.session.commit()
        return jsonify({"message": "Property deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to delete property", "error": str(e)}), 500

@app.route('/amenities', methods=['POST'])
@jwt_required()
def add_amenity():
    data = request.get_json()

    new_amenity = Amenity(name=data['name'])

    try:
        db.session.add(new_amenity)
        db.session.commit()
        return jsonify({"message": "Amenity added successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to add amenity", "error": str(e)}), 500

@app.route('/properties/<int:property_id>/rooms', methods=['GET'])
@jwt_required()
def get_rooms(property_id):
    rooms = Room.query.filter_by(property_id=property_id).all()
    return jsonify([room.as_dict() for room in rooms]), 200

@app.route('/properties/<int:property_id>/availability', methods=['GET'])
@jwt_required()
def check_availability(property_id):
    data = request.args
    check_in_date = datetime.strptime(data['check_in_date'], '%Y-%m-%d').date()
    check_out_date = datetime.strptime(data['check_out_date'], '%Y-%m-%d').date()

    # Check if any room in the property is available for the given dates
    rooms = Room.query.filter_by(property_id=property_id).all()
    for room in rooms:
        bookings = Booking.query.filter_by(room_id=room.id).all()
        for booking in bookings:
            if check_in_date < booking.check_out_date and check_out_date > booking.check_in_date:
                return jsonify({"available": False}), 200
    return jsonify({"available": True}), 200

@app.route('/bookings', methods=['POST'])
@jwt_required()
def make_booking():
    data = request.get_json()
    current_user = get_jwt_identity()

    new_booking = Booking(
        user_id=current_user['id'],
        room_id=data['room_id'],
        check_in_date=datetime.strptime(data['check_in_date'], '%Y-%m-%d').date(),
        check_out_date=datetime.strptime(data['check_out_date'], '%Y-%m-%d').date()
    )

    try:
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({"message": "Booking created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to create booking", "error": str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Resource not found"}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"message": "Bad request", "error": str(error)}), 400

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({"message": "Unauthorized", "error": str(error)}), 401

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"message": "Internal server error", "error": str(error)}), 500

if __name__ == '__main__':
    app.run(debug=True)

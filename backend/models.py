from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_bcrypt import Bcrypt


# Initialize SQLAlchemy
db = SQLAlchemy()
bcrypt = Bcrypt()

# Naming conventions for SQLAlchemy
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

property_amenity = db.Table('property_amenity',
    db.Column('property_id', db.Integer, db.ForeignKey('property.id'), primary_key=True),
    db.Column('amenity_id', db.Integer, db.ForeignKey('amenity.id'), primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')
    images = db.Column(db.String(255), nullable=True)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    host_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    images = db.Column(db.String(255), nullable=True)
    amenities = db.relationship('Amenity', secondary=property_amenity, lazy='subquery',
                                backref=db.backref('properties', lazy=True))
    rooms = db.relationship('Room', backref='property', lazy=True)
    reviews = db.relationship('Review', backref='property', lazy=True)

    def as_dict(self):
        return {
            'id': self.id,
            'host_id': self.host_id,
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'images': self.images,
            'amenities': [amenity.name for amenity in self.amenities],
            'rooms': [room.as_dict() for room in self.rooms],
            'reviews': [review.as_dict() for review in self.reviews]
        }

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Boolean, default=True)

    def as_dict(self):
        return {
            'id': self.id,
            'property_id': self.property_id,
            'name': self.name,
            'price': self.price,
            'availability': self.availability
        }

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)

    def as_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'property_id': self.property_id,
            'rating': self.rating,
            'comment': self.comment
        }

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, unique=True)
    fullname = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    address = db.Column(db.Text, nullable=False)
    
    
    user = db.relationship('User', backref=db.backref('profile', uselist=False))

    def as_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'fullname': self.fullname,
            'phone_number': self.phone_number,
            'address': self.address
        }

class Amenity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)

class PasswordReset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    token = db.Column(db.String(128), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
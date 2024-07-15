import os
from datetime import datetime
from flask import Flask
from models import db, User, Profile, Booking, Review, Property, Room

app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Bind the SQLAlchemy instance to the Flask app
db.init_app(app)

def get_or_create(model, defaults=None, **kwargs):
    instance = db.session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        params = {k: v for k, v in kwargs.items() if not isinstance(v, db.Column)}
        params.update(defaults or {})
        instance = model(**params)
        db.session.add(instance)
        db.session.commit()
        return instance, True

def seed():
    with app.app_context():
        # Create users if they do not exist
        user1, created1 = get_or_create(User, username='paul ngugi', defaults=dict(email='paul@gmail.com', password_hash='jokester907', role='host', images='default.jpg'))
        user2, created2 = get_or_create(User, username='anne wanjiru', defaults=dict(email='anne@gmail.com', password_hash='mxyzptlk574', role='guest', images='default.jpg'))
        user3, created3 = get_or_create(User, username='mary wanjiru', defaults=dict(email='mary@gmail.com', password_hash='kol765red', role='guest', images='default.jpg'))
        user4, created4 = get_or_create(User, username='samuel ngugi', defaults=dict(email='samuel@gmail.com', password_hash='oid56890now', role='guest', images='default.jpg'))

        if created1:
            profile1 = Profile(fullname='paul ngugi', phone_number='0798654325', address='123 Main St', user_id=user1.id)
            db.session.add(profile1)

        if created2:
            profile2 = Profile(fullname='anne wanjiru', phone_number='0721353072', address='456 Elm St', user_id=user2.id)
            db.session.add(profile2)

        if created3:
            profile3 = Profile(fullname='mary wanjiru', phone_number='0704567890', address='789 Maple Ave', user_id=user3.id)
            db.session.add(profile3)

        if created4:
            profile4 = Profile(fullname='samuel ngugi', phone_number='0704317874', address='321 Oak St', user_id=user4.id)
            db.session.add(profile4)

        db.session.commit()

        # Create properties
        property1 = Property(host_id=user1.id, name='Sunset Villas', description='Beautiful beachfront villas', address='123 Beach Ave', images='villa.jpg')
        property2 = Property(host_id=user2.id, name='Mountain Retreat', description='Cozy cabins in the mountains', address='456 Hill St', images='mountain.jpg')
        property3 = Property(host_id=user3.id, name='City Loft', description='Modern apartments in the city center', address='789 City Rd', images='city.jpg')
        property4 = Property(host_id=user4.id, name='Lakeside Cottage', description='Quaint cottage by the lake', address='321 Lakeview Dr', images='lake.jpg')

        db.session.add(property1)
        db.session.add(property2)
        db.session.add(property3)
        db.session.add(property4)
        db.session.commit()

        # Create rooms
        room1 = Room(property_id=property1.id, name='Room A', price=1500.0)
        room2 = Room(property_id=property1.id, name='Room B', price=1000.0)
        room3 = Room(property_id=property2.id, name='Suite X', price=2000.0)
        room4 = Room(property_id=property2.id, name='Economy Y', price=4000.0)
        room5 = Room(property_id=property3.id, name='Studio E', price=1800.0)
        room6 = Room(property_id=property3.id, name='Apartment F', price=2500.0)
        room7 = Room(property_id=property4.id, name='Cottage Z', price=3000.0)

        db.session.add(room1)
        db.session.add(room2)
        db.session.add(room3)
        db.session.add(room4)
        db.session.add(room5)
        db.session.add(room6)
        db.session.add(room7)
        db.session.commit()

        # Create bookings
        booking1 = Booking(user_id=user1.id, room_id=room1.id, check_in_date=datetime(2024, 7, 15), check_out_date=datetime(2024, 7, 20))
        booking2 = Booking(user_id=user2.id, room_id=room3.id, check_in_date=datetime(2024, 8, 1), check_out_date=datetime(2024, 8, 5))
        booking3 = Booking(user_id=user3.id, room_id=room5.id, check_in_date=datetime(2024, 8, 10), check_out_date=datetime(2024, 8, 15))
        booking4 = Booking(user_id=user4.id, room_id=room7.id, check_in_date=datetime(2024, 8, 20), check_out_date=datetime(2024, 8, 25))

        db.session.add(booking1)
        db.session.add(booking2)
        db.session.add(booking3)
        db.session.add(booking4)
        db.session.commit()

        # Create reviews
        review1 = Review(user_id=user1.id, property_id=property1.id, rating=5, comment='Great stay!')
        review2 = Review(user_id=user2.id, property_id=property2.id, rating=4, comment='Nice place, but a bit noisy.')
        review3 = Review(user_id=user3.id, property_id=property3.id, rating=4, comment='Convenient location, clean rooms.')
        review4 = Review(user_id=user4.id, property_id=property4.id, rating=5, comment='Perfect getaway spot!')

        db.session.add(review1)
        db.session.add(review2)
        db.session.add(review3)
        db.session.add(review4)
        db.session.commit()

if __name__ == '__main__':
    seed()

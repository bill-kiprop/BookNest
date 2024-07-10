from app import create_app, db
from app.models import User, Profile, Booking, Review, Property, Room
from datetime import datetime

app = create_app()

def seed():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create users
        user1 = User(username='john_doe', email='john@example.com', password='password')
        user2 = User(username='jane_doe', email='jane@example.com', password='password')
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

        # Create profiles
        profile1 = Profile(first_name='John', last_name='Doe', phone_number='1234567890', user_id=user1.id)
        profile2 = Profile(first_name='Jane', last_name='Doe', phone_number='0987654321', user_id=user2.id)
        db.session.add(profile1)
        db.session.add(profile2)

        # Create properties
        property1 = Property(name='Sunset Villas', address='123 Beach Ave')
        property2 = Property(name='Mountain Retreat', address='456 Hill St')
        db.session.add(property1)
        db.session.add(property2)
        db.session.commit()

        # Create rooms
        room1 = Room(property_id=property1.id, room_number='101', room_type='Deluxe', price_per_night=150.0)
        room2 = Room(property_id=property1.id, room_number='102', room_type='Standard', price_per_night=100.0)
        room3 = Room(property_id=property2.id, room_number='201', room_type='Suite', price_per_night=200.0)
        room4 = Room(property_id=property2.id, room_number='202', room_type='Economy', price_per_night=80.0)
        db.session.add(room1)
        db.session.add(room2)
        db.session.add(room3)
        db.session.add(room4)

        # Create bookings
        booking1 = Booking(user_id=user1.id, room_id=room1.id, check_in=datetime(2024, 7, 15), check_out=datetime(2024, 7, 20))
        booking2 = Booking(user_id=user2.id, room_id=room3.id, check_in=datetime(2024, 8, 1), check_out=datetime(2024, 8, 5))
        db.session.add(booking1)
        db.session.add(booking2)

        # Create reviews
        review1 = Review(user_id=user1.id, property_id=property1.id, rating=5, comment='Great stay!')
        review2 = Review(user_id=user2.id, property_id=property2.id, rating=4, comment='Nice place, but a bit noisy.')
        db.session.add(review1)
        db.session.add(review2)

        # Commit the changes
        db.session.commit()

if __name__ == '__main__':
    seed()

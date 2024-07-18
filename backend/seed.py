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
        user1, created1 = get_or_create(User, username='paul ngugi', defaults=dict(email='paul@gmail.com', password_hash='jokester907', role='host', images='https://www.listchallenges.com/f/items/4ecde67d-6c43-4739-8bce-eafe9f9cb52e.jpg'))
        user2, created2 = get_or_create(User, username='anne wanjiru', defaults=dict(email='anne@gmail.com', password_hash='mxyzptlk574', role='guest', images='https://www.listchallenges.com/f/items/46aa4f76-bd8d-4f66-bd94-ce5c5efab1ff.jpg'))
        user3, created3 = get_or_create(User, username='mary wanjiru', defaults=dict(email='mary@gmail.com', password_hash='kol765red', role='guest', images='https://www.listchallenges.com/f/items/908c82a9-ab11-400a-973c-a99872195811.jpg'))
        user4, created4 = get_or_create(User, username='samuel ngugi', defaults=dict(email='samuel@gmail.com', password_hash='oid56890now', role='guest', images='https://www.listchallenges.com/f/items/9e4578dd-3741-4ea5-aeb5-19e1f70ac75e.jpg'))
        user5, created5 = get_or_create(User, username='john smith', defaults=dict(email='john@gmail.com', password_hash='pass123', role='guest', images='https://www.listchallenges.com/f/items/b163cb32-9206-48d3-96cf-34d0f0eca644.jpg'))
        user6, created6 = get_or_create(User, username='jane foster', defaults=dict(email='jane@gmail.com', password_hash='secret456', role='guest', images='https://www.listchallenges.com/f/items/9fd758b4-de9d-4c6e-b92d-ef0ce7856448.jpg'))
        user7, created7 = get_or_create(User, username='david brown', defaults=dict(email='david@gmail.com', password_hash='password789', role='guest', images='https://www.listchallenges.com/f/items/f9573949-70f6-4b66-8a53-a1b70d84cd8e.jpg'))
        user8, created8 = get_or_create(User, username='emily white', defaults=dict(email='emily@gmail.com', password_hash='testpass321', role='guest', images='https://www.listchallenges.com/f/items/22644821-231c-4c72-9a16-7bce86c2337b.jpg'))
        user9, created9 = get_or_create(User, username='mark miller', defaults=dict(email='mark@gmail.com', password_hash='securepass987', role='guest', images='https://www.listchallenges.com/f/items/95fdfebc-a852-40ef-af8e-3168804eeee6.jpg'))
        user10, created10 = get_or_create(User, username='linda johnson', defaults=dict(email='linda@gmail.com', password_hash='pwd1234', role='guest', images='https://www.listchallenges.com/f/items/d7bcdb1a-c367-4d1c-8819-73a34a0bccb5.jpg'))
        user11, created11 = get_or_create(User, username='michael jackson', defaults=dict(email='michael@gmail.com', password_hash='moonwalk123', role='guest', images='https://www.listchallenges.com/f/items/6c5d561a-092e-47c6-b64c-2a05aabc5dff.jpg'))
        user12, created12 = get_or_create(User, username='sarah williams', defaults=dict(email='sarah@gmail.com', password_hash='p@ssw0rd!', role='guest', images='https://www.listchallenges.com/f/items/e9061226-2362-4f31-89a4-c5b27b00cd5c.jpg'))
        user13, created13 = get_or_create(User, username='chris evans', defaults=dict(email='chris@gmail.com', password_hash='captainamerica', role='guest', images='https://www.listchallenges.com/f/items/1b8c47bc-ff89-4c7a-ba22-ed108738e362.jpg'))
        user14, created14 = get_or_create(User, username='amanda king', defaults=dict(email='amanda@gmail.com', password_hash='queenbee', role='guest', images='https://www.listchallenges.com/f/items/92c38c61-97b6-41f2-b841-a283c7fa06bc.jpg'))
        user15, created15 = get_or_create(User, username='peter parker', defaults=dict(email='peter@gmail.com', password_hash='spiderman123', role='guest', images='https://www.listchallenges.com/f/items/94288c6d-8e81-438b-ad0a-e61a7608be0c.jpg'))
        user16, created16 = get_or_create(User, username='elizabeth taylor', defaults=dict(email='elizabeth@gmail.com', password_hash='diamonds567', role='guest', images='https://www.listchallenges.com/f/items/97246d7e-0dc0-4883-a8cb-2cc84f646ed7.jpg'))
        user17, created17 = get_or_create(User, username='brad pitt', defaults=dict(email='brad@gmail.com', password_hash='hollywoodstar', role='guest', images='https://www.listchallenges.com/f/items/c5deaf04-678f-4323-80d9-6a53eca9a466.jpg'))
        user18, created18 = get_or_create(User, username='angelina jolie', defaults=dict(email='angelina@gmail.com', password_hash='mr&mrs.smith', role='guest', images='https://www.listchallenges.com/f/items/fcd1b15a-ccf8-4918-9bfd-8ca9dabd189c.jpg'))
        user19, created19 = get_or_create(User, username='leonardo dicaprio', defaults=dict(email='leo@gmail.com', password_hash='oscarwinner', role='guest', images='https://www.listchallenges.com/f/items/26e74086-ad49-4da7-9ebd-1190318e5d7c.jpg'))
        user20, created20 = get_or_create(User, username='natalie portman', defaults=dict(email='natalie@gmail.com', password_hash='blackswan', role='guest', images='https://www.listchallenges.com/f/items/cb860f40-dee2-4a98-8751-f3d86cb3b856.jpg'))
        
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
        if created5:
            profile5 = Profile(fullname='john doe', phone_number='0723456789', address='567 Sunset Blvd', user_id=user5.id)
            db.session.add(profile5)
        if created6:
            profile6 = Profile(fullname='jane smith', phone_number='0787654321', address='890 Sunrise Ave', user_id=user6.id)
            db.session.add(profile6)
        if created7:
            profile7 = Profile(fullname='david brown', phone_number='0765432109', address='123 Moonlight Rd', user_id=user7.id)
            db.session.add(profile7)
        if created8:
            profile8 = Profile(fullname='emily white', phone_number='0712345678', address='456 Starry Lane', user_id=user8.id)
            db.session.add(profile8)
        if created9:
            profile9 = Profile(fullname='mark miller', phone_number='0776543210', address='789 Galaxy Blvd', user_id=user9.id)
            db.session.add(profile9)
        if created10:
            profile10 = Profile(fullname='linda johnson', phone_number='0754321098', address='321 Milky Way', user_id=user10.id)
            db.session.add(profile10)
        if created11:
            profile11 = Profile(fullname='michael jackson', phone_number='0732109876', address='654 Comet St', user_id=user11.id)
            db.session.add(profile11)
        if created12:
            profile12 = Profile(fullname='sarah williams', phone_number='0723456789', address='987 Lunar Ave', user_id=user12.id)
            db.session.add(profile12)
        if created13:
            profile13 = Profile(fullname='chris evans', phone_number='0787654321', address='543 Solar Rd', user_id=user13.id)
            db.session.add(profile13)
        if created14:
            profile14 = Profile(fullname='amanda king', phone_number='0765432109', address='210 Pluto Blvd', user_id=user14.id)
            db.session.add(profile14)
        if created15:
            profile15 = Profile(fullname='peter parker', phone_number='0712345678', address='876 Mars Ave', user_id=user15.id)
            db.session.add(profile15)
        if created16:
            profile16 = Profile(fullname='elizabeth taylor', phone_number='0776543210', address='234 Jupiter St', user_id=user16.id)
            db.session.add(profile16)
        if created17:
            profile17 = Profile(fullname='brad pitt', phone_number='0754321098', address='789 Saturn Lane', user_id=user17.id)
            db.session.add(profile17)
        if created18:
            profile18 = Profile(fullname='angelina jolie', phone_number='0732109876', address='123 Neptune Blvd', user_id=user18.id)
            db.session.add(profile18)
        if created19:
            profile19 = Profile(fullname='leonardo dicaprio', phone_number='0723456789', address='456 Uranus Ave', user_id=user19.id)
            db.session.add(profile19)
        if created20:
            profile20 = Profile(fullname='natalie portman', phone_number='0787654321', address='789 Mercury Rd', user_id=user20.id)
            db.session.add(profile20)

        db.session.commit()

        # Create properties
        property1 = Property(host_id=user1.id, name='Sunset Villas', description='Luxurious villas with sunset views', address='123 Beach Rd', images='https://cf.bstatic.com/xdata/images/hotel/max1024x768/464265022.jpg?k=825cc73af021e3bd7aeed1f90dfdc232589b16c81518e256b2b434b67caa95cb&o=&hp=1')
        property2 = Property(host_id=user1.id, name='Mountain Retreat', description='Cozy cabins in the mountains', address='456 Hill St', images='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTk306z6lxKqMzvjy-TW16OlufK8TQZuop955s30DVpMnQmODYPm0LfpYXsTaTaGSrlnO0&usqp=CAU')
        property3 = Property(host_id=user1.id, name='City Center Loft', description='Modern loft in the heart of the city', address='789 Downtown Blvd', images='https://a0.muscache.com/im/pictures/miso/Hosting-639738307310746577/original/5a25a891-f00b-45ea-a561-bf90322b2728.jpeg?im_w=720')
        property4 = Property(host_id=user1.id, name='Lakeview Cottage', description='Escape to Lakeview Cottage: Where modern comfort meets serene lakefront views.', address='321 Lake Shore Dr', images='https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1d/47/4a/10/lakeview-house-cottages.jpg?w=700&h=-1&s=1')
        property5 = Property(host_id=user2.id, name='Coastal Getaway', description='Relaxing getaway on the coast', address='543 Ocean Blvd', images='https://www.avoyatravel.com/images/dblibrary/104217-190228105900_900x509.jpg')
        property6 = Property(host_id=user2.id, name='Rustic Cabin', description='Rustic cabin retreat in the woods', address='876 Forest Rd', images='https://cf.bstatic.com/xdata/images/hotel/max1024x768/496535583.jpg?k=e2ed74a2c88128c01db40f91e561eb708d8e28419eaba9c9363246a6a6a02640&o=&hp=1')
        property7 = Property(host_id=user2.id, name='Luxury Penthouse', description='Luxurious penthouse with city views', address='109 Skyline Ave', images='https://as1.ftcdn.net/v2/jpg/05/58/93/80/1000_F_558938097_t0hpe87N1zNrE51VtC4gNHWWBEB9TIK1.jpg')
        property8 = Property(host_id=user2.id, name='Ski Chalet', description='Ski-in/ski-out chalet near the slopes', address='210 Snowy Lane', images='https://www.alpineanswers.co.uk/media/W1siZiIsIjIwMTYvMTAvMjYvNmZuMHdkdm1oal9Ta2lfaW5fc2tpX291dF9jaGFsZXRzLmpwZyJdLFsicCIsInRodW1iIiwiNDYweDM2MCMiXV0/23929c70ef34fb21/Ski_in_ski_out_chalets.jpg')
        property9 = Property(host_id=user3.id, name='Vineyard Villa', description='Villa overlooking vineyards and hills', address='432 Vineyard Rd', images='https://www.cdvillas.com/media/23220848/TOURELLE-BASTIDE-EXT-04.jpg?id=114990&scale=both&mode=crop&quality=90&width=1200&height=800')
        property10 = Property(host_id=user3.id, name='Desert Oasis', description='Oasis retreat in the desert', address='765 Sand Dune Dr', images='https://design-middleeast.com/wp-content/uploads/2020/04/Al-Badayer-1.jpg')
        property11 = Property(host_id=user3.id, name='Historic Manor', description='Historic manor house with gardens', address='098 Manor Ave', images='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcRagwC3gv0PAK82SB6j96R5zeFRlsvLbAz-A3Kv0u1l4r4XQRKRKznKlDAchvs2U7eSc&usqp=CAU')
        property12 = Property(host_id=user3.id, name='Island Paradise', description='Private island paradise with ocean views', address='567 Island Dr', images='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRMmKbDTHDsOA2s0dTYYwm2ASI1pXNPZPVjEWGOawVKlN2t_EMCy-2mct6zpbKwk7yl2Y&usqp=CAU')
        property13 = Property(host_id=user4.id, name='Farmhouse Cottage', description='Quaint farmhouse cottage in the countryside', address='890 Farm Rd', images='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRA3EOTEUeVqMBhA-QBFv1B56pSjXj64rRMy11WdmRusQr2QnHCmQu47NjRUotkKePXW1k&usqp=CAU')
        property14 = Property(host_id=user4.id, name='Urban Studio', description='Modern studio apartment in the city', address='345 Urban Blvd', images='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTw5zOThyfIIEdpwtSRXStsfHFJO4B4NM0cnZKLUTFC2ZfY2rpNKRMd7X0uuPB0Y-J71jY&usqp=CAU')
        property15 = Property(host_id=user4.id, name='Treehouse Retreat', description='Secluded treehouse retreat in the woods', address='678 Treehouse Rd', images='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXaIb42o7mrUSnwoIcAojMHqRdPiQDq6CR9fGfO_M4QO2XvcjUq1LJ4Er3pCEGmyPTZD4&usqp=CAU')
        property16 = Property(host_id=user4.id, name='Castle Keep', description='Castle keep with medieval charm', address='901 Castle Ln', images='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnx5mFyoEffdN82w0LKGygT2kpRk5eN_-fhGQN9BdzQfNrWt7BGznmSZhGtyIXYYwlBHk&usqp=CAU')
        property17 = Property(host_id=user5.id, name='Cottage by the Sea', description='Quaint cottage with sea views', address='234 Sea Breeze Ave', images='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRd88Cyd73Ks1uke2cnN-pnFiP58UyRn6RTlRTfBhZ9cgx4R8CKZqLfQ8zzlLvzIE6M0zA&usqp=CAU')
        property18 = Property(host_id=user5.id, name='Tropical Bungalow', description='Tropical bungalow retreat', address='567 Palm Tree Dr', images='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgHzvv5qKQGAHkr876-Ud7C335hS0cmUzrhH3KzaC6TOhMABMzBbX_cMxkP8YbMuO4Yhk&usqp=CAU')
        property19 = Property(host_id=user5.id, name='Mountain View Lodge', description='Lodge with stunning mountain views', address='890 Mountain Rd', images='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPuW7PvrsKhDNeyXj8RC2g2e7CRoqW67j4_98Tgq8uZoLIIdWVsTM-IS3CLGeYlw0My5A&usqp=CAU')
        property20 = Property(host_id=user5.id, name='Art Deco Apartment', description='Art Deco style apartment in historic building', address='123 Art Deco Ave', images='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiclAf4w5YUqgSis7PMR5ocS-56zjg66oMaKwU3iOcqEi0_mbhKXqhFpJBzqTUluV4nmA&usqp=CAU')

        db.session.add(property1)
        db.session.add(property2)
        db.session.add(property3)
        db.session.add(property4)
        db.session.add(property5)
        db.session.add(property6)
        db.session.add(property7)
        db.session.add(property8)
        db.session.add(property9)
        db.session.add(property10)
        db.session.add(property11)
        db.session.add(property12)
        db.session.add(property13)
        db.session.add(property14)
        db.session.add(property15)
        db.session.add(property16)
        db.session.add(property17)
        db.session.add(property18)
        db.session.add(property19)
        db.session.add(property20)

        db.session.commit()

        # Create rooms
        room1 = Room(property_id=property1.id, name='Master Suite', price=3000.0)
        room2 = Room(property_id=property1.id, name='Ocean View Room', price=2500.0)
        room3 = Room(property_id=property2.id, name='Cozy Cabin', price=2000.0)
        room4 = Room(property_id=property2.id, name='Mountain View Room', price=1800.0)
        room5 = Room(property_id=property3.id, name='City Loft', price=2200.0)
        room6 = Room(property_id=property3.id, name='Downtown View Room', price=2000.0)
        room7 = Room(property_id=property4.id, name='Lakeview Room', price=1800.0)
        room8 = Room(property_id=property4.id, name='Garden Cottage', price=1500.0)
        room9 = Room(property_id=property5.id, name='Beachfront Room', price=2800.0)
        room10 = Room(property_id=property5.id, name='Sunset Suite', price=3200.0)
        room11 = Room(property_id=property6.id, name='Rustic Cabin Room', price=1900.0)
        room12 = Room(property_id=property6.id, name='Forest View Room', price=1700.0)
        room13 = Room(property_id=property7.id, name='Luxury Penthouse Suite', price=5000.0)
        room14 = Room(property_id=property7.id, name='City Skyline Room', price=4000.0)
        room15 = Room(property_id=property8.id, name='Ski Chalet Room', price=3000.0)
        room16 = Room(property_id=property8.id, name='Slopeside View Room', price=2500.0)
        room17 = Room(property_id=property9.id, name='Vineyard View Room', price=2800.0)
        room18 = Room(property_id=property9.id, name='Hilltop Suite', price=3200.0)
        room19 = Room(property_id=property10.id, name='Desert Oasis Room', price=2000.0)
        room20 = Room(property_id=property10.id, name='Sand Dune View Room', price=1800.0)

        db.session.add(room1)
        db.session.add(room2)
        db.session.add(room3)
        db.session.add(room4)
        db.session.add(room5)
        db.session.add(room6)
        db.session.add(room7)
        db.session.add(room8)
        db.session.add(room9)
        db.session.add(room10)
        db.session.add(room11)
        db.session.add(room12)
        db.session.add(room13)
        db.session.add(room14)
        db.session.add(room15)
        db.session.add(room16)
        db.session.add(room17)
        db.session.add(room18)
        db.session.add(room19)
        db.session.add(room20)

        db.session.commit()

        # Create bookings
        booking1 = Booking(user_id=user1.id, room_id=room1.id, check_in_date=datetime(2024, 7, 15), check_out_date=datetime(2024, 7, 20))
        booking2 = Booking(user_id=user2.id, room_id=room3.id, check_in_date=datetime(2024, 8, 1), check_out_date=datetime(2024, 8, 5))
        booking3 = Booking(user_id=user3.id, room_id=room5.id, check_in_date=datetime(2024, 8, 10), check_out_date=datetime(2024, 8, 15))
        booking4 = Booking(user_id=user4.id, room_id=room7.id, check_in_date=datetime(2024, 8, 20), check_out_date=datetime(2024, 8, 25))
        booking5 = Booking(user_id=user5.id, room_id=room9.id, check_in_date=datetime(2024, 9, 1), check_out_date=datetime(2024, 9, 5))
        booking6 = Booking(user_id=user6.id, room_id=room11.id, check_in_date=datetime(2024, 9, 10), check_out_date=datetime(2024, 9, 15))
        booking7 = Booking(user_id=user7.id, room_id=room13.id, check_in_date=datetime(2024, 9, 20), check_out_date=datetime(2024, 9, 25))
        booking8 = Booking(user_id=user8.id, room_id=room15.id, check_in_date=datetime(2024, 10, 1), check_out_date=datetime(2024, 10, 5))
        booking9 = Booking(user_id=user9.id, room_id=room17.id, check_in_date=datetime(2024, 10, 10), check_out_date=datetime(2024, 10, 15))
        booking10 = Booking(user_id=user10.id, room_id=room19.id, check_in_date=datetime(2024, 10, 20), check_out_date=datetime(2024, 10, 25))
        booking11 = Booking(user_id=user11.id, room_id=room2.id, check_in_date=datetime(2024, 11, 1), check_out_date=datetime(2024, 11, 5))
        booking12 = Booking(user_id=user12.id, room_id=room4.id, check_in_date=datetime(2024, 11, 10), check_out_date=datetime(2024, 11, 15))
        booking13 = Booking(user_id=user13.id, room_id=room6.id, check_in_date=datetime(2024, 11, 20), check_out_date=datetime(2024, 11, 25))
        booking14 = Booking(user_id=user14.id, room_id=room8.id, check_in_date=datetime(2024, 12, 1), check_out_date=datetime(2024, 12, 5))
        booking15 = Booking(user_id=user15.id, room_id=room10.id, check_in_date=datetime(2024, 12, 10), check_out_date=datetime(2024, 12, 15))
        booking16 = Booking(user_id=user16.id, room_id=room12.id, check_in_date=datetime(2025, 1, 1), check_out_date=datetime(2025, 1, 5))
        booking17 = Booking(user_id=user17.id, room_id=room14.id, check_in_date=datetime(2025, 1, 10), check_out_date=datetime(2025, 1, 15))
        booking18 = Booking(user_id=user18.id, room_id=room16.id, check_in_date=datetime(2025, 1, 20), check_out_date=datetime(2025, 1, 25))
        booking19 = Booking(user_id=user19.id, room_id=room18.id, check_in_date=datetime(2025, 2, 1), check_out_date=datetime(2025, 2, 5))
        booking20 = Booking(user_id=user20.id, room_id=room20.id, check_in_date=datetime(2025, 2, 10), check_out_date=datetime(2025, 2, 15))

        db.session.add(booking1)
        db.session.add(booking2)
        db.session.add(booking3)
        db.session.add(booking4)
        db.session.add(booking5)
        db.session.add(booking6)
        db.session.add(booking7)
        db.session.add(booking8)
        db.session.add(booking9)
        db.session.add(booking10)
        db.session.add(booking11)
        db.session.add(booking12)
        db.session.add(booking13)
        db.session.add(booking14)
        db.session.add(booking15)
        db.session.add(booking16)
        db.session.add(booking17)
        db.session.add(booking18)
        db.session.add(booking19)
        db.session.add(booking20)

        db.session.commit()

        # Create reviews
        review1 = Review(user_id=user1.id, property_id=property1.id, rating=5, comment='Great stay!')
        review2 = Review(user_id=user2.id, property_id=property2.id, rating=4, comment='Nice place, but a bit noisy.')
        review3 = Review(user_id=user3.id, property_id=property3.id, rating=4, comment='Convenient location, clean rooms.')
        review4 = Review(user_id=user4.id, property_id=property4.id, rating=5, comment='Perfect getaway spot.')
        review5 = Review(user_id=user5.id, property_id=property5.id, rating=5, comment='Amazing views and service!')
        review6 = Review(user_id=user6.id, property_id=property6.id, rating=4, comment='Relaxing atmosphere, great for families.')
        review7 = Review(user_id=user7.id, property_id=property7.id, rating=4, comment='Central location, modern amenities.')
        review8 = Review(user_id=user8.id, property_id=property8.id, rating=5, comment='Luxurious experience, highly recommended.')
        review9 = Review(user_id=user9.id, property_id=property9.id, rating=4, comment='Spacious rooms, friendly staff.')
        review10 = Review(user_id=user10.id, property_id=property10.id, rating=5, comment='Perfect for ski enthusiasts!')
        review11 = Review(user_id=user11.id, property_id=property11.id, rating=4, comment='Beautiful beachfront property.')
        review12 = Review(user_id=user12.id, property_id=property12.id, rating=5, comment='Secluded and peaceful.')
        review13 = Review(user_id=user13.id, property_id=property13.id, rating=4, comment='Vibrant neighborhood, great nightlife.')
        review14 = Review(user_id=user14.id, property_id=property14.id, rating=5, comment='Excellent wine tasting experience.')
        review15 = Review(user_id=user15.id, property_id=property15.id, rating=4, comment='Relaxing lakeside retreat.')
        review16 = Review(user_id=user16.id, property_id=property16.id, rating=5, comment='Breathtaking views from the penthouse.')
        review17 = Review(user_id=user17.id, property_id=property17.id, rating=4, comment='Quaint and charming.')
        review18 = Review(user_id=user18.id, property_id=property18.id, rating=5, comment='Golfers paradise!')
        review19 = Review(user_id=user19.id, property_id=property19.id, rating=4, comment='Magical winter wonderland.')
        review20 = Review(user_id=user20.id, property_id=property20.id, rating=5, comment='Exotic and luxurious.')

        db.session.add(review1)
        db.session.add(review2)
        db.session.add(review3)
        db.session.add(review4)
        db.session.add(review5)
        db.session.add(review6)
        db.session.add(review7)
        db.session.add(review8)
        db.session.add(review9)
        db.session.add(review10)
        db.session.add(review11)
        db.session.add(review12)
        db.session.add(review13)
        db.session.add(review14)
        db.session.add(review15)
        db.session.add(review16)
        db.session.add(review17)
        db.session.add(review18)
        db.session.add(review19)
        db.session.add(review20)

        db.session.commit()

        print("Database seeded successfully!")

if __name__ == '__main__':
    seed()


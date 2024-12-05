import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import Navigationbar from './navbar';
import BookingFormModal from './BookingFormModal';
import './hotels.css'; 

function HotelPage() {
  const [hotel, setHotel] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [selectedRoom, setSelectedRoom] = useState(null);
  const { id } = useParams();
  const navigate = useNavigate();

  const fetchHotelData = () => {
    fetch(`http://localhost:5000/properties/${id}`)
      .then((res) => {
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
        return res.json();
      })
      .then((data) => {
        setHotel(data);
      })
      .catch((err) => {
        console.error('Error fetching data:', err);
      });
  };

  useEffect(() => {
    fetchHotelData();
  }, [id]);

  const handleDelete = () => {
    fetch(`http://localhost:5000/properties/${id}`, {
      method: 'DELETE',
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
        navigate('/properties');
      })
      .catch((err) => {
        console.error('Error deleting hotel:', err);
      });
  };

  const handleBookClick = (room) => {
    const token = localStorage.getItem('token');
    if (!token) {
      navigate('/login');
      alert('Log-in required');
      return;
    }
    setSelectedRoom(room);
    setShowModal(true);
  };

  if (!hotel) {
    return <div>Loading...</div>;
  }

  const availableRooms = hotel.rooms.filter(room => room.availability);

  return (
    <div>
      <Navigationbar />
      <div className="hotelPage">
        <div className="hotelDetails">
          <img src={hotel.images} alt="Hotel" className="pageImage" />
          <div className="detailsText">
            <h2>{hotel.name}</h2>
            <h3>{hotel.address}</h3>
            <p>{hotel.description}</p>
          </div>
        </div>
        <div className="rooms">
          <h4>Rooms:</h4>
          {availableRooms.length > 0 ? (
            <ul>
              {hotel.rooms.map((room) => (
                <li key={room.id}>
                  {room.name}:<br/> {room.availability ? 'available' :
                   (<p style={{fontStyle:'italic', color:'GrayText'}}>Booked</p>)
                   }<br />Price: ${room.price}
                  {room.availability && <button onClick={() => handleBookClick(room)} className="button">Book</button>}
                </li>
              ))}
            </ul>
          ) : (
            <p style={{fontStyle:'italic', color:'GrayText'}}>The hotel is fully booked.</p>
          )}
        </div>
        <div className='reviews'>
          <h3>Reviews:</h3>
          {Array.isArray(hotel.reviews) && hotel.reviews.length > 0 ? (
            <ul>
              {hotel.reviews.map((review) => (
                <li key={review.id}>
                  <p><strong>Rating:</strong> {review.rating}</p>
                  <p><strong>Comment:</strong> {review.comment}</p>
                </li>
              ))}
            </ul>
          ) : (
            <p>No reviews available.</p>
          )}
        </div>
      </div>
      <BookingFormModal
        show={showModal}
        handleClose={() => setShowModal(false)}
        room={selectedRoom}
        onBookingSuccess={fetchHotelData} // Pass the function to refresh hotel data
      />
    </div>
  );
}

export default HotelPage;

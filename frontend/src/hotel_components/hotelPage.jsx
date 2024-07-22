import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import Navigationbar from './navbar';
import BookingFormModal from './BookingFormModal'; // Import the BookingFormModal component

function HotelPage() {
  const [hotel, setHotel] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [selectedRoom, setSelectedRoom] = useState(null); // To store the selected room data
  const { id } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
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
      return;
    }
    setSelectedRoom(room); // Set the selected room
    setShowModal(true); // Show the modal
  };

  if (!hotel) {
    return <div>Loading...</div>; // Show a loading message while data is being fetched
  }

  return (
    <div>
      <Navigationbar />
      <div className='hotelPage' style={{ paddingTop: '10px' }}>
        <div style={{ paddingLeft: '10px' }}>
          <img src={hotel.images} alt="Hotel" className='pageImage' />
          <h2>{hotel.name}</h2>
          <h3>{hotel.address}</h3>
          <p>{hotel.description}</p>
          <div>
            <h4>Rooms:</h4>
            <ul>
              {hotel.rooms.map((room) => (
                <li key={room.id}>
                  {room.name}: {room.availability ? 'Available' : 'Not available'}<br />Price: ${room.price}
                  <button onClick={() => handleBookClick(room)}>Book</button>
                </li>
              ))}
            </ul>
          </div>
          <button onClick={handleDelete} className='button-primary'>Delete</button>
        </div>
      </div>
      <BookingFormModal 
        show={showModal} 
        handleClose={() => setShowModal(false)} 
        room={selectedRoom} 
      />
    </div>
  );
}

export default HotelPage;

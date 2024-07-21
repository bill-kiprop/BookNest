import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

function HotelPage() {
  const [hotel, setHotel] = useState(null);
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
        // Redirect to the properties list or home page after successful deletion
        navigate('/properties');
      })
      .catch((err) => {
        console.error('Error deleting hotel:', err);
      });
  };

  if (!hotel) {
    return <div>Loading...</div>; // Show a loading message while data is being fetched
  }

  return (
    <div className='hotelPage'>
      <div>
        <img src={hotel.images} alt="Hotel" className='pageImage' />
        <h2>{hotel.name}</h2>
        <h3>{hotel.address}</h3>
        <p>{hotel.description}</p>
        <button onClick={handleDelete} className='button-primary'>Delete</button>
      </div>
    </div>
  );
}

export default HotelPage;

import React, { useEffect, useState } from 'react'
// import useParams from 'react-router-dom'
import { useParams } from 'react-router-dom';

function HotelPage() {
  const [hotel, setHotel] = useState([]);
  const params = useParams()
  
    

useEffect(() => {
  fetch(`http://localhost:5000/${params.id}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  })
    .then((res) => res.json())
    .then((data) => {
      setHotel(data);
    })
    .catch((err) => console.log(err));
}, [params.id]);

  return (
    <div>
      <div>
        {hotel.image}
      </div>
        {hotel.description}
    </div>
  )
}

export default HotelPage
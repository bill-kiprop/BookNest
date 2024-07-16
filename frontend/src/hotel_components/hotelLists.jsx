import React, { useEffect } from 'react'
import { useState } from 'react';
import { BASE_URL } from './utils';
import { Col, Container, Row } from 'react-bootstrap';
import Hotelcard from './hotelcard';

function HotelLists() {
 const [hotels, setHotels] = useState([]);

    useEffect(() => {
      fetch(`http://localhost:5000/properties`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      })
        .then((res) => res.json())
        .then((data) => {
          setHotels(data);
        })
        .catch((err) => console.log(err));
    }, []);
  return (
    <div>
   <Container>
    <Row>
    {hotels.map((hotel) =>
(       <Col key={hotel.id}>
            <Hotelcard
            id={hotel.id}
            name={hotel.name}
            address={hotel.address}
            image={hotel.images}
            />

        </Col>
    ))}    
    </Row>
   </Container>

    </div>
  )
}

export default HotelLists
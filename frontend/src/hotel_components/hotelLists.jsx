import React, { useEffect, useState } from 'react';
import { Container, Row, Col, Modal, Button, Form, Navbar } from 'react-bootstrap';
import Hotelcard from './hotelcard';
import { BASE_URL } from './utils';
import Navigationbar from './navbar';

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
    <div className='page'>
      <div>
        <Navigationbar/>
      </div>
      <div style={{paddingTop:'10px'}}>
      <Container>
        <Row>
          {hotels.map((hotel) => (
            <Col key={hotel.id}>
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

    </div>
  );
}

export default HotelLists;

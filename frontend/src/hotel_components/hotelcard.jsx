import React from 'react';
import Card from 'react-bootstrap/Card';
import './hotels.css';
import { NavLink } from 'react-router-dom';

function Hotelcard({ id, name, image, address, isHost, onDelete, onUpdate }) {
  return (
    <div style={{paddingBottom:'10px'}}>
    <Card style={{ width: '300px', border: '1px', paddingBottom:'10px' }}>
      <img variant="top" src={image} className='image' style={{ objectFit: 'cover', borderRadius: '5px' }} />
      <Card.Body className='cards'>
        <Card.Title>{name}</Card.Title>
        <Card.Text>
          ADDRESS: {address}
        </Card.Text>
        <NavLink to={`/properties/${id}`}>
        <button className='button-primary'>VIEW</button>
        </NavLink>
        
      </Card.Body>
    </Card>
    </div>
  );
}

export default Hotelcard;

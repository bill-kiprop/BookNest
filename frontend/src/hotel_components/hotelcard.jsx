import React from 'react';
import Card from 'react-bootstrap/Card';
import './hotels.css';

function Hotelcard({ id, name, image, address, isHost, onDelete, onUpdate }) {
  return (
    <Card style={{ width: '300px', border: '1px' }}>
      <img variant="top" src={image} className='image' style={{ objectFit: 'cover', borderRadius: '5px' }} />
      <Card.Body className='cards'>
        <Card.Title>{name}</Card.Title>
        <Card.Text>
          ADDRESS: {address}
        </Card.Text>
        {isHost && (
          <>
            <button onClick={() => onUpdate(id)} className='button-primary'>Update</button>
            <button onClick={() => onDelete(id)} className='button-danger'>Delete</button>
          </>
        )}
        <button className='button-primary'>Book</button>
      </Card.Body>
    </Card>
  );
}

export default Hotelcard;

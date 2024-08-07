import React from 'react';
import Card from 'react-bootstrap/Card';
import './hotels.css';
import { NavLink } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTrashAlt, faEdit } from '@fortawesome/free-solid-svg-icons';

function Hotelcard({ id, name, image, address, onDelete, onUpdate }) {
  return (
    <div style={{ paddingBottom: '10px' }}>
      <Card style={{ width: '300px', border: '1px', paddingBottom: '10px', backgroundColor: '#D2691E' }}>
        <img variant="top" src={image} className='image' style={{ objectFit: 'cover', borderRadius: '5px' }} />
        <Card.Body className='cards' style={{ backgroundColor: '#D2691E' }}>
          <Card.Title>{name}</Card.Title>
          <Card.Text>
            ADDRESS: {address}
          </Card.Text>
          <NavLink to={`/properties/${id}`}>
            <button className='button-primary'>VIEW</button>
          </NavLink>
          <FontAwesomeIcon icon={faEdit} onClick={onUpdate} style={{ marginLeft: '100px', cursor: 'pointer', color: '#5D4037', marginTop:'10px'}} />
          <FontAwesomeIcon icon={faTrashAlt} onClick={onDelete} style={{ marginLeft: '10px', cursor: 'pointer', color: '#5D4037' }} />
        </Card.Body>
      </Card>
    </div>
  );
}

export default Hotelcard;

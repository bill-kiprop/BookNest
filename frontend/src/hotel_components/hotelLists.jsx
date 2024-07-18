import React, { useEffect, useState } from 'react';
import { Container, Row, Col, Modal, Button, Form } from 'react-bootstrap';
import Hotelcard from './hotelcard';
import { BASE_URL } from './utils';

function HotelLists() {
  const [hotels, setHotels] = useState([]);
  const [isHost, setIsHost] = useState(true); // Change this based on actual host logic
  const [showModal, setShowModal] = useState(false);
  const [currentHotel, setCurrentHotel] = useState(null);

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

  const handleDelete = (id) => {
    fetch(`http://localhost:5000/properties/${id}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((res) => {
        if (res.ok) {
          setHotels(hotels.filter(hotel => hotel.id !== id));
        }
      })
      .catch((err) => console.log(err));
  };

  const handleUpdate = (hotel) => {
    setCurrentHotel(hotel);
    setShowModal(true);
  };

  const handleCloseModal = () => {
    setShowModal(false);
    setCurrentHotel(null);
  };

  const handleSave = () => {
    fetch(`http://localhost:5000/properties/${currentHotel.id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(currentHotel),
    })
      .then((res) => res.json())
      .then((updatedHotel) => {
        setHotels(hotels.map(hotel => (hotel.id === updatedHotel.id ? updatedHotel : hotel)));
        handleCloseModal();
      })
      .catch((err) => console.log(err));
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCurrentHotel(prevHotel => ({ ...prevHotel, [name]: value }));
  };

  return (
    <div>
      <Container>
        <Row>
          {hotels.map((hotel) => (
            <Col key={hotel.id}>
              <Hotelcard
                id={hotel.id}
                name={hotel.name}
                address={hotel.address}
                image={hotel.images}
                isHost={isHost}
                onDelete={() => handleDelete(hotel.id)}
                onUpdate={() => handleUpdate(hotel)}
              />
            </Col>
          ))}
        </Row>
      </Container>

      {currentHotel && (
        <Modal show={showModal} onHide={handleCloseModal}>
          <Modal.Header closeButton>
            <Modal.Title>Update Hotel</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <Form>
              <Form.Group controlId="formHotelName">
                <Form.Label>Name</Form.Label>
                <Form.Control
                  type="text"
                  name="name"
                  value={currentHotel.name}
                  onChange={handleChange}
                />
              </Form.Group>
              <Form.Group controlId="formHotelAddress">
                <Form.Label>Address</Form.Label>
                <Form.Control
                  type="text"
                  name="address"
                  value={currentHotel.address}
                  onChange={handleChange}
                />
              </Form.Group>
              <Form.Group controlId="formHotelImage">
                <Form.Label>Image URL</Form.Label>
                <Form.Control
                  type="text"
                  name="images"
                  value={currentHotel.images}
                  onChange={handleChange}
                />
              </Form.Group>
            </Form>
          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={handleCloseModal}>
              Close
            </Button>
            <Button variant="primary" onClick={handleSave}>
              Save Changes
            </Button>
          </Modal.Footer>
        </Modal>
      )}
    </div>
  );
}

export default HotelLists;

import React, { useEffect, useState } from 'react';
import { Container, Row, Col, Modal, Button, Form, Navbar } from 'react-bootstrap';
import Hotelcard from './hotelcard';
import { BASE_URL } from './utils';
import Navigationbar from './navbar';
import axios from 'axios';
import DeleteConfirmationModal from './delete';

function HotelLists() {
  const [hotels, setHotels] = useState([]);
  const [showUpdateModal, setShowUpdateModal] = useState(false);
  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const [selectedHotel, setSelectedHotel] = useState(null);
  const [updatedData, setUpdatedData] = useState({
    name: '',
    description: '',
    address: ''
  });

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

  const handleDelete = async () => {
    try {
      await axios.delete(`http://localhost:5000/properties/${selectedHotel.id}`, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
      });
      setHotels(hotels.filter((hotel) => hotel.id !== selectedHotel.id));
      setShowDeleteModal(false);
      setSelectedHotel(null);
    } catch (error) {
      console.error('Failed to delete property', error);
    }
  };

  const handleUpdate = (hotel) => {
    setSelectedHotel(hotel);
    setUpdatedData({
      name: hotel.name,
      description: hotel.description,
      address: hotel.address
    });
    setShowUpdateModal(true);
  };

  const handleUpdateChange = (e) => {
    const { name, value } = e.target;
    setUpdatedData((prevData) => ({
      ...prevData,
      [name]: value
    }));
  };

  const handleUpdateSubmit = async () => {
    try {
      await axios.put(`http://localhost:5000/properties/${selectedHotel.id}`, updatedData, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
      });
      setHotels(hotels.map((hotel) => (hotel.id === selectedHotel.id ? { ...hotel, ...updatedData } : hotel)));
      setShowUpdateModal(false);
    } catch (error) {
      console.error('Failed to update property', error);
    }
  };

  const confirmDelete = (hotel) => {
    setSelectedHotel(hotel);
    setShowDeleteModal(true);
  };

  return (
    <div className='page'>
      <div>
        <Navigationbar />
      </div>
      <div style={{ paddingTop: '10px' }}>
        <Container>
          <Row>
            {hotels.map((hotel) => (
              <Col key={hotel.id}>
                <Hotelcard
                  id={hotel.id}
                  name={hotel.name}
                  address={hotel.address}
                  image={hotel.images}
                  onDelete={() => confirmDelete(hotel)}
                  onUpdate={() => handleUpdate(hotel)}
                />
              </Col>
            ))}
          </Row>
        </Container>
      </div>
      <Modal show={showUpdateModal} onHide={() => setShowUpdateModal(false)}>
        <Modal.Header closeButton>
          <Modal.Title>Update Property</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form>
            <Form.Group controlId="formName">
              <Form.Label>Name</Form.Label>
              <Form.Control
                type="text"
                name="name"
                value={updatedData.name}
                onChange={handleUpdateChange}
              />
            </Form.Group>
            <Form.Group controlId="formDescription">
              <Form.Label>Description</Form.Label>
              <Form.Control
                type="text"
                name="description"
                value={updatedData.description}
                onChange={handleUpdateChange}
              />
            </Form.Group>
            <Form.Group controlId="formAddress">
              <Form.Label>Address</Form.Label>
              <Form.Control
                type="text"
                name="address"
                value={updatedData.address}
                onChange={handleUpdateChange}
              />
            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={() => setShowUpdateModal(false)}>
            Close
          </Button>
          <Button variant="primary" onClick={handleUpdateSubmit}>
            Save Changes
          </Button>
        </Modal.Footer>
      </Modal>
      <DeleteConfirmationModal
        show={showDeleteModal}
        handleClose={() => setShowDeleteModal(false)}
        handleDelete={handleDelete}
        hotelName={selectedHotel?.name}
      />
    </div>
  );
}

export default HotelLists;

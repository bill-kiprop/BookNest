import React, { useState } from 'react';
import { Button, Form, Modal } from 'react-bootstrap';

const BookingFormModal = ({ show, handleClose }) => {
  const [roomId, setRoomId] = useState('');
  const [checkIn, setCheckIn] = useState('');
  const [checkOut, setCheckOut] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission logic here
    console.log({ roomId, checkIn, checkOut });
    handleClose(); // Close the modal on successful submission
  };

  return (
    <Modal show={show} onHide={handleClose}>
      <Modal.Header closeButton>
        <Modal.Title>Book a Room</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Form onSubmit={handleSubmit}>
          <Form.Group controlId="formRoomId">
            <Form.Label>Room ID</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter Room ID"
              value={roomId}
              onChange={(e) => setRoomId(e.target.value)}
              required
            />
          </Form.Group>

          <Form.Group controlId="formCheckIn">
            <Form.Label>Check-in Date</Form.Label>
            <Form.Control
              type="datetime-local"
              value={checkIn}
              onChange={(e) => setCheckIn(e.target.value)}
              required
            />
          </Form.Group>

          <Form.Group controlId="formCheckOut">
            <Form.Label>Check-out Date</Form.Label>
            <Form.Control
              type="datetime-local"
              value={checkOut}
              onChange={(e) => setCheckOut(e.target.value)}
              required
            />
          </Form.Group>

          <Button variant="primary" type="submit">
            Book Now
          </Button>
        </Form>
      </Modal.Body>
    </Modal>
  );
};

export default BookingFormModal;

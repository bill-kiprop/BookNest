import React, { useState, useEffect } from 'react';
import { Button, Form, Modal } from 'react-bootstrap';

const BookingFormModal = ({ show, handleClose, room }) => {
  const [roomId, setRoomId] = useState('');
  const [checkIn, setCheckIn] = useState('');
  const [checkOut, setCheckOut] = useState('');

  useEffect(() => {
    if (room) {
      setRoomId(room.id);
    }
  }, [room]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const token = localStorage.getItem('token');
    const bookingData = {
      room_id: roomId,
      check_in_date: checkIn,
      check_out_date: checkOut
    };

    try {
      const response = await fetch('http://localhost:5000/bookings', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(bookingData)
      });

      if (response.ok) {
        const result = await response.json();
        console.log('Booking successful:', result);
        handleClose(); // Close the modal on successful submission
      } else {
        const errorData = await response.json();
        console.error('Error booking room:', errorData);
      }
    } catch (error) {
      console.error('Error:', error);
    }
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
              value={roomId}
              readOnly
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


import React, { useState } from 'react';
import { Modal, Button, Form } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';

const AddPropertyModal = ({ show, handleClose }) => {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [address, setAddress] = useState('');
  const [images, setImages] = useState('');

  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();

    const token = localStorage.getItem('token');
    if (!token) {
      alert('You must be logged in to add a property.');
      return;
    }

    fetch('http://localhost:5000/properties', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({
        name,
        description,
        address,
        images
      })
    })
    .then(res => {
      if (!res.ok) {
        throw new Error('Failed to add property');
      }
      return res.json();
    })
    .then(data => {
      alert('Property added successfully!');
      handleClose();
      navigate('/properties'); 
    })
    .catch(err => {
      console.error('Error:', err);
      alert('Failed to add property');
    });
  };

  return (
    <Modal show={show} onHide={handleClose}>
      <Modal.Header closeButton>
        <Modal.Title>Add New Property</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Form onSubmit={handleSubmit}>
          <Form.Group controlId="formName">
            <Form.Label>Name</Form.Label>
            <Form.Control 
              type="text" 
              placeholder="Enter property name" 
              value={name} 
              onChange={(e) => setName(e.target.value)} 
              required 
            />
          </Form.Group>
          <Form.Group controlId="formDescription">
            <Form.Label>Description</Form.Label>
            <Form.Control 
              as="textarea" 
              rows={3} 
              placeholder="Enter property description" 
              value={description} 
              onChange={(e) => setDescription(e.target.value)} 
              required 
            />
          </Form.Group>
          <Form.Group controlId="formAddress">
            <Form.Label>Address</Form.Label>
            <Form.Control 
              type="text" 
              placeholder="Enter property address" 
              value={address} 
              onChange={(e) => setAddress(e.target.value)} 
              required 
            />
          </Form.Group>
          <Form.Group controlId="formImages">
            <Form.Label>Images (URL)</Form.Label>
            <Form.Control 
              type="text" 
              placeholder="Enter property image URL" 
              value={images} 
              onChange={(e) => setImages(e.target.value)} 
              required 
            />
          </Form.Group>
         
          <Button variant="primary" type="submit">
            Add Property
          </Button>
        </Form>
      </Modal.Body>
    </Modal>
  );
};

export default AddPropertyModal;

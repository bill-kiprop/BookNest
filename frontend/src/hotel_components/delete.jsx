import React from 'react';
import { Modal, Button } from 'react-bootstrap';

function DeleteConfirmationModal({ show, handleClose, handleDelete, hotelName }) {
  return (
    <Modal show={show} onHide={handleClose}>
      <Modal.Header closeButton>
        <Modal.Title>Delete Property</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        Are you sure you want to delete the property "{hotelName}"?
      </Modal.Body>
      <Modal.Footer>
        <Button variant="secondary" onClick={handleClose}>
          Cancel
        </Button>
        <Button variant="danger" onClick={handleDelete}>
          Delete
        </Button>
      </Modal.Footer>
    </Modal>
  );
}

export default DeleteConfirmationModal;

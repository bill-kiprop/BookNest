import React, { useState } from 'react';
import Carousel from './Carousel'; 
import BookingFormModal from './BookingFormModal'; 
import { Button, Card, Container } from 'react-bootstrap'; 

const Home = () => {
  const [showModal, setShowModal] = useState(false);

  const handleShow = () => setShowModal(true);
  const handleClose = () => setShowModal(false);

  return (
    <div className="container mt-5">
      <h1 className="text-center mb-4">Welcome to Booknest</h1>
      
      <Carousel />
      
      <div className="text-center mt-4 mb-4">
        <Button variant="primary" onClick={handleShow}>
          Book a Room
        </Button>
      </div>
      
      <Container className="mt-4">
        <h3 className="text-center mb-4">More</h3>
        
        <div className="row">
          <div className="col-lg-6 mb-4">
            <Card>
              <Card.Img variant="top" src="https://cf.bstatic.com/xdata/images/hotel/max1024x768/568230409.jpg?k=ec5695ed4c0204bc501efa07da8adf96f7ef131dc5531434655653cf3ae863f1&o=&hp=1" alt="About Us" />
              <Card.Body>
                <Card.Title>About Us </Card.Title>
                <Card.Text>
                  Welcome to Booknest! We are dedicated to helping travelers find the perfect stay and hosts showcase their properties with ease. Our platform offers a seamless booking experience with user-friendly interfaces for both guests and hosts.
                </Card.Text>
                <Card.Text>
                  Our mission is to provide an effortless way to book accommodations and manage properties. Whether you're looking for a cozy getaway or wanting to list your property, Booknest has you covered.
                </Card.Text>
              </Card.Body>
            </Card>
          </div>
          
          <div className="col-lg-6 mb-4">
            <Card>
            <Card.Img variant="top" src="https://media.istockphoto.com/id/1455997571/vector/online-flight-ticket-reservation-for-vacation-hand-holding-phone-with-airplane-route.jpg?s=612x612&w=0&k=20&c=FeVhgdk3hNZGmGtxPttMa6T3NpYiy50exVLSbLWBTEE=" alt="About Us" />

              <Card.Body>
                <Card.Title>Our Values</Card.Title>
                <Card.Text>
                  <ul>
                    <li>Customer Satisfaction</li>
                    <li>Transparency</li>
                    <li>Reliability</li>
                    <li>Innovation</li>
                  </ul>
                </Card.Text>
              </Card.Body>
            </Card>
          </div>
        </div>
      </Container>
      
      <BookingFormModal show={showModal} handleClose={handleClose} />
    </div>
  );
};

export default Home;

import React, { useState, useEffect } from 'react';
import { Container, Nav, Navbar, Row, Col } from 'react-bootstrap';
import { NavLink, useNavigate } from 'react-router-dom';
import AddPropertyModal from './addProperty';
import './navbar.css';
import axios from 'axios';

function Navigationbar() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const navigate = useNavigate();
  const [user, setUser] = useState(null);
  const [message, setMessage] = useState('');

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const userResponse = await axios.get('http://localhost:5000/users', {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        });
        setUser(userResponse.data);
      } catch (error) {
        setMessage('Failed to fetch user data');
        console.error('There was an error fetching user data!', error);
      }
    };

    fetchUser();
  }, []);

  const openModal = () => setIsModalOpen(true);
  const closeModal = () => setIsModalOpen(false);

  return (
    <div className='navbar1'>
      <Container>
        <Row>
          <Col xs={6}>
            <Navbar.Brand>
              <h2 className='title'>BOOKNEST</h2>
            </Navbar.Brand>
          </Col>
          <Col>
            <Nav>
              <NavLink to={"/"}>
                <button className='button-primary'> HOME</button>
              </NavLink>
          
              <NavLink to={'/login'}>
                <button className='button-primary'>
                  LOGIN
                </button>
              </NavLink>
              
              {user && user.role === 'admin' && (
                <button className='button-primary' onClick={openModal}>
                  +
                </button>
              )}
              {user && (
              <NavLink to={'/profile'}>
                {user.image && <img src={user.image} alt="User profile" className='profile-image' style={{ borderRadius: '50%', height: '50px', width: '50px' }} />}
              </NavLink>
            )}
            </Nav>

          </Col>
        </Row>
      </Container>
      <AddPropertyModal show={isModalOpen} handleClose={closeModal} />
    </div>
  );
}

export default Navigationbar;

import React from 'react'
import { Container, Nav,Navbar, Row,Col } from 'react-bootstrap'
import { NavLink, useNavigate } from 'react-router-dom'
import './navbar.css'


function Navigationbar() {
  const previousPage = useNavigate()
  return (
    
     <div className='navbar1'>
        <Container>
        <Row>
          
        <Col xs={8}>
        <Navbar.Brand >
            <h2 className='title'>GET A PET</h2>
          </Navbar.Brand>
        </Col>
        <Col >
          <Nav>
            <NavLink to ={"/"}>
               <button className='button-primary'> HOME</button>
               </NavLink>
               <NavLink to={'/users'}>
               <button className='button-primary'>PROFILES</button>
               </NavLink>
               
              
               
              
          </Nav></Col>
      </Row>
          
         
        </Container>
        </div>
    
  )
}

export default Navigationbar
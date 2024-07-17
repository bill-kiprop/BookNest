
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './hotel_components/Header';
import Carousel from './hotel_components/Carousel'; 
import AboutUs from './hotel_components/AboutUs';
import Login from './hotel_components/Login';
import Profile from './hotel_components/Profile';

import './App.css'
import { Button, Card } from 'react-bootstrap'
import Hotelcard from './hotel_components/hotelcard'

function App() {


  return (
    <>
    <Hotelcard/>
    <Router>
      <div className="App">
        <Header />
        <Routes>
          <Route path="/" element={<Carousel />} /> {/* Update Carousel route */}
          <Route path="/about" element={<AboutUs />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </div>
    </Router>
   

    </>
  )
}

export default App

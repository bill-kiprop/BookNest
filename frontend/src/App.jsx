import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './hotel_components/Header';
import Carousel from './hotel_components/Carousel'; 
import AboutUs from './hotel_components/AboutUs';
import Login from './hotel_components/Login';
import Profile from './hotel_components/Profile';

const App = () => {
  // Mock user data for demonstration
  const user = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    bookings: [] 
  };

  return (
    <Router>
      <div className="App">
        <Header />
        <Routes>
          <Route path="/" element={<Carousel />} /> 
          <Route path="/about" element={<AboutUs />} />
          <Route path="/profile" element={<Profile user={user} />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

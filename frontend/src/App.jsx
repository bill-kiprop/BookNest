import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './hotel_components/Header';
import Carousel from '.hotel_/components/Carousel'; 
import AboutUs from '.hotel_/components/AboutUs';
import Login from '.hotel_/components/Login';
import Profile from '.hotel_/components/Profile';

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
          <Route path="/carousel" element={<Carousel />} /> 
          <Route path="/about" element={<AboutUs />} />
          <Route path="/profile" element={<Profile user={user} />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

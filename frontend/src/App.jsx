import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './hotel_components/Header';
import Home from './hotel_components/Home'; 
import Login from './hotel_components/Login';
import Profile from './hotel_components/Profile';
import BookingForm from './hotel_components/BookingFormModal'; // Correct import

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
          <Route path="/" element={<Home />} />
          <Route path="/profile" element={<Profile user={user} />} />
          <Route path="/login" element={<Login />} />
          <Route path="/booking/:id" element={<BookingForm />} /> {/* Correct path for BookingForm */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;

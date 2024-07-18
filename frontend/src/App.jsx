
import { useState } from 'react'

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/Login.jsx';
import Signup from './components/Signup.jsx';
import Profile from './components/Profile.jsx';
import Header from './components/Header.jsx';
import Footer from './components/Footer.jsx';
import './App.css';

const App = () => {
    const [users, setUsers] = useState([]);
    const [currentUser, setCurrentUser] = useState(null);

    return (
        <Router>
            <Header currentUser={currentUser} setCurrentUser={setCurrentUser} />
            <main>
                <Routes>
                  
                    <Route path="/login" element={<Login users={users} setCurrentUser={setCurrentUser} />} />
                    <Route path="/signup" element={<Signup setUsers={setUsers} />} />
                    <Route path="/profile" element={<Profile currentUser={currentUser} setCurrentUser={setCurrentUser} />} />
                </Routes>
            </main>
            <Footer />
        </Router>
    );
};

export default App;



import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './hotel_components/Header';
import Home from './hotel_components/Home'; 
import Login from './hotel_components/Login';
import Profile from './hotel_components/Profile';
import BookingForm from './hotel_components/BookingFormModal'; 
import Footer from './hotel_components/Footer';
import Reviews from './hotel_components/Reviews'


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
          <Route path="/booking/:id" element={<BookingForm />} />
          <Route path="/reviews" element={<Reviews />} /> 
        </Routes>
        <Footer />
      </div>
    </Router>
  );

}

export default App;


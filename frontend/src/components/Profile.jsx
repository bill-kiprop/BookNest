import React, { useState } from 'react';
import axios from 'axios';
import Navigationbar from '../hotel_components/navbar';
import './Login.css';

const ProfileForm = () => {
  const [fullname, setFullname] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [address, setAddress] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/profile', 
        {
          fullname,
          phone_number: phoneNumber,
          address,
        },
        {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`,
          },
        }
      );
      setMessage(response.data.message);
    } catch (error) {
      setMessage('Failed to update profile');
      console.error('There was an error!', error);
    }
  };

  return (
    <div className='homepage'>
      <div>
        <Navigationbar />
      </div>
      <div className='login-container'>
        <h2>Create Profile</h2>
        <form onSubmit={handleSubmit}>
          <div>
            <label>Full Name:</label>
            <input
              type="text"
              value={fullname}
              onChange={(e) => setFullname(e.target.value)}
              required
            />
          </div>
          <div>
            <label>Phone Number:</label>
            <input
              type="text"
              value={phoneNumber}
              onChange={(e) => setPhoneNumber(e.target.value)}
              required
            />
          </div>
          <div>
            <label>Address:</label>
            <input
              type="text"
              value={address}
              onChange={(e) => setAddress(e.target.value)}
              required
            />
          </div>
          <button type="submit" className='button-primary'>Create Profile</button>
        </form>
        {message && <p>{message}</p>}
      </div>
    </div>
  );
};

export default ProfileForm;

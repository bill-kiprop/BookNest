import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Navigationbar from '../hotel_components/navbar';
import './Login.css';
import './Profile.css'

const ProfileDisplay = () => {
  const [profile, setProfile] = useState(null);
  const [user, setUser] = useState(null);
  const [message, setMessage] = useState('');

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const profileResponse = await axios.get('http://localhost:5000/profile', {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        });
        setProfile(profileResponse.data);
      } catch (error) {
        setMessage('Failed to fetch profile');
        console.error('There was an error fetching profile!', error);
      }
    };

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

    fetchProfile();
    fetchUser();
  }, []);

  return (
    <div className='homepage'>
      <div>
        <Navigationbar />
      </div>
      <div className='profile-page'>
        <h2></h2>
        {message && <p>{message}</p>}
        {user && profile ? (
          <div>
             <h2><strong></strong> {user.username}</h2>
            {user.image && <img src={user.image} alt="User profile" className='profile-image' style={{borderRadius:'50%', height:'200px', width:'200px'}}/>}
           
            <p><strong>Email:</strong> {user.email}</p>
            <p><strong>Full Name:</strong> {profile.fullname}</p>
            <p><strong>Phone Number:</strong> {profile.phone_number}</p>
            <p><strong>Address:</strong> {profile.address}</p>
          </div>
        ) : (
          <p>Loading profile...</p>
        )}
      </div>
    </div>
  );
};

export default ProfileDisplay;

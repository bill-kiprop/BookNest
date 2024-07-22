import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Navigationbar from '../hotel_components/navbar';

const Profile = () => {
    const [profile, setProfile] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchProfile = async () => {
            const token = localStorage.getItem('token');
            if (!token) {
                navigate('/login');
                return;
            }

            try {
                const response = await fetch('http://localhost:5000/profile', {
                    method: 'PUT',
                    headers: { 
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${token}`
                    },
                    body: JSON.stringify(profile)
                });
    
                if (response.ok) {
                    alert('Profile updated successfully');
                } else {
                    const { message } = await response.json();
                    alert(message);
                }
            } catch (error) {
                console.error('Error:', error);
            }
            try {
                const response = await fetch('http://localhost:5000/profile', {
                    headers: { 'Authorization': `Bearer ${token}` }
                });

                if (response.ok) {
                    const data = await response.json();
                    setProfile(data);
                // } else {
                //     navigate('/login');
                }
            } catch (error) {
                console.error('Error:', error);
                // navigate('/login');
            }
        };

        fetchProfile();
    }, [navigate]);

    const handleUpdate = async (e) => {
        e.preventDefault();
        const token = localStorage.getItem('token');

        
    };

    if (!profile) return <div>
        <Navigationbar/>
        Loading...</div>;

    return (
        <div>
            <div>
                <Navigationbar/>
            </div>
            <h2>Profile</h2>
            <form onSubmit={handleUpdate}>
                <input
                    type="text"
                    value={profile.username}
                    onChange={(e) => setProfile({ ...profile, username: e.target.value })}
                />
                <input
                    type="email"
                    value={profile.email}
                    onChange={(e) => setProfile({ ...profile, email: e.target.value })}
                />
                <input
                    type="text"
                    value={profile.role}
                    onChange={(e) => setProfile({ ...profile, role: e.target.value })}
                />
                <button type="submit">Update Profile</button>
            </form>
        </div>
    );
};

export default Profile;

import React, { useState } from 'react';
import PropTypes from 'prop-types';

const Profile = ({ currentUser, setCurrentUser }) => {
    const [email, setEmail] = useState(currentUser?.email || '');
    const [name, setName] = useState(currentUser?.name || '');

    const handleSave = (e) => {
        e.preventDefault();
        const updatedUser = { ...currentUser, email, name };
        setCurrentUser(updatedUser);
        alert('Profile updated successfully!');
    };

    if (!currentUser) return <p>Please log in to view your profile.</p>;

    return (
        <div>
            <h1>Profile</h1>
            <form onSubmit={handleSave}>
                <div>
                    <label>Name:</label>
                    <input
                        type="text"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                    />
                </div>
                <div>
                    <label>Email:</label>
                    <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                    />
                </div>
                <button type="submit">Save</button>
            </form>
            <h2>Your Profile</h2>
            <p><strong>Username:</strong> {currentUser.username}</p>
            <p><strong>Name:</strong> {currentUser.name}</p>
            <p><strong>Email:</strong> {currentUser.email}</p>
        </div>
    );
};

Profile.propTypes = {
    currentUser: PropTypes.shape({
        username: PropTypes.string.isRequired,
        email: PropTypes.string,
        name: PropTypes.string,
    }),
    setCurrentUser: PropTypes.func.isRequired,
};

export default Profile;
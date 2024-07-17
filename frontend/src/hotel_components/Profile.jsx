import React from 'react';

const Profile = ({ user }) => {
  return (
    <div className="profile">
      <h2>Welcome, {user.name}!</h2>
      <p>Email: {user.email}</p>
      {/* Display booking history or other profile information */}
    </div>
  );
}

export default Profile;

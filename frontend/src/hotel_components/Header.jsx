import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

// Simulated authentication check function
const isAuthenticated = () => {
  // Implement authentication logic here
  // For demonstration now, this function  will return true
  return true;
};

const Header = () => {
  const auth = isAuthenticated(); //  actual authentication logic

  return (
    <header className="header">
      <div className="logo">
        <p>BookNest</p>
        <img
          src="https://c8.alamy.com/comp/2B147DT/initial-bn-letter-logo-with-creative-modern-business-typography-vector-template-creative-abstract-letter-bn-logo-design-2B147DT.jpg"
          alt="BNB App Logo"
        />
      </div>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          {auth && <li><Link to="/profile">Profile</Link></li>}
          {auth ? (
            <>
              <li><Link to="/booking">Bookings</Link></li>
              <li><Link to="/reviews">Reviews</Link></li>
              <li><Link to="/login">Login</Link></li> 
            </>
          ) : (
            <li><Link to="/login">Login</Link></li>
          )}
        </ul>
      </nav>
    </header>
  );
};

export default Header;

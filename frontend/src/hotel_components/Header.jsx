import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css'; 

const isAuthenticated = () => {
  return true; // utareplace with actual authentication logic
};

const Header = () => {
  const auth = isAuthenticated();

  return (
    <header className="bg-light py-3 d-flex justify-content-between align-items-center border-bottom shadow-sm">
      <div className="d-flex align-items-center">
        <p className="booknest-title mb-0">BookNest</p>
        <img
          src="https://c8.alamy.com/comp/2B147DT/initial-bn-letter-logo-with-creative-modern-business-typography-vector-template-creative-abstract-letter-bn-logo-design-2B147DT.jpg"
          alt="BNB App Logo"
          className="ml-3" 
          style={{ height: '60px' }} 
        />
      </div>
      <nav>
        <ul className="nav">
          <li className="nav-item"><Link className="nav-link" to="/">Home</Link></li>
          {auth && <li className="nav-item"><Link className="nav-link" to="/profile">Profile</Link></li>}
          {auth ? (
            <>
              <li className="nav-item"><Link className="nav-link" to="/booking">Bookings</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/reviews">Reviews</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/login">Login</Link></li> 
            </>
          ) : (
            <li className="nav-item"><Link className="nav-link" to="/login">Login</Link></li>
          )}
        </ul>
      </nav>
    </header>
  );
};

export default Header;

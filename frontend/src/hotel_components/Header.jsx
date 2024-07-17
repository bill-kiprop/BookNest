import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css'; 

const Header = () => {
  return (
    <header className="header">
      p<>BookNest
      </>
      <div className="logo">
        <img src="https://images-platform.99static.com//bQcR1Oxo7dSk0X8Ivoein66R9g4=/29x2022:1986x3979/fit-in/500x500/99designs-contests-attachments/94/94697/attachment_94697235" alt="BNB App Logo" />
      </div>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/profile">Profile</Link></li>
          <li><Link to="/about">About Us</Link></li>
          <li><Link to="/login">Login</Link></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;

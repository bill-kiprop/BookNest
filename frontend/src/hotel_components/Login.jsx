import React, { useState } from 'react';
import './Login.css'; // Assuming you have a CSS file named Login.css for styling

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [firstName, setFirstName] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [isLogin, setIsLogin] = useState(true); // State to toggle between login and signup forms

  const handleLogin = () => {
    // Implement login logic
    console.log('Logging in with:', email, password);
  };

  const handleSignup = () => {
    // Implement signup logic
    console.log('Signing up with:', firstName, email, password, confirmPassword);
    // You can add validation logic here before submitting
  };

  const toggleForm = () => {
    setIsLogin(!isLogin); // Toggle between login and signup forms
  };

  return (
    <div className="card">
      <div className="card2">
        <form className="form">
          <p id="heading">{isLogin ? 'Login' : 'Sign Up'}</p>
          {!isLogin && (
            <div className="field">
              <input
                type="text"
                className="input-field"
                placeholder="Firstname"
                value={firstName}
                onChange={(e) => setFirstName(e.target.value)}
              />
            </div>
          )}
          <div className="field">
            <input
              type="text"
              className="input-field"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div className="field">
            <input
              type="password"
              className="input-field"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          {!isLogin && (
            <div className="field">
              <input
                type="password"
                className="input-field"
                placeholder="Confirm Password"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
              />
            </div>
          )}
          <div className="btn">
            <button className="button1" onClick={isLogin ? handleLogin : handleSignup}>
              {isLogin ? 'Login' : 'Sign Up'}
            </button>
            <button className="button2" onClick={toggleForm}>
              {isLogin ? 'Sign Up' : 'Sign In'}
            </button>
          </div>
          <button className="button3">Forgot Password</button>
        </form>
      </div>
    </div>
  );
};

export default Login;

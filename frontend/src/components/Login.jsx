import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import Navigationbar from '../hotel_components/navbar';
import './Login.css';


const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleLogin = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch('http://localhost:5000/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });

            if (response.ok) {
                const { access_token } = await response.json();
                localStorage.setItem('token', access_token); // Save token to local storage
                navigate('/profile'); // Redirect to profile page
            } else {
                const { message } = await response.json();
                alert(message);
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <div className='homepage'>
            <Navigationbar />
            <div className="login-container">
                <h2>Login</h2>
                <form onSubmit={handleLogin}>
                    <input
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        placeholder="Username"
                        required
                    />
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        placeholder="Password"
                        required
                    />
                    <button type="submit" className='button-primary'>Login</button>
                </form>
                <p>Don't have an account? <Link to="/signup">Signup</Link></p>
                {/* <button onClick={() => navigate('/signup')} className='button-primary'>Sign Up</button> */}
            </div>
        </div>
    );
};

export default Login;

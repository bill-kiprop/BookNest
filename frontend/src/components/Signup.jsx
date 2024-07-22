import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import Navigationbar from '../hotel_components/navbar';
import './Login.css'; // Import the same CSS file

const Signup = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [role, setRole] = useState('');
    const navigate = useNavigate();

    const handleSignup = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch('http://localhost:5000/register', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password, email, role })
            });

            if (response.ok) {
                const loginResponse = await fetch('http://localhost:5000/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username, password })
                });

                if (loginResponse.ok) {
                    const { access_token } = await loginResponse.json();
                    localStorage.setItem('token', access_token);
                    navigate('/profile');
                } else {
                    const { message } = await loginResponse.json();
                    alert(message);
                }
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
                <h2>Signup</h2>
                <form onSubmit={handleSignup}>
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
                    <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        placeholder="Email"
                        required
                    />
                    <input
                        type="text"
                        value={role}
                        onChange={(e) => setRole(e.target.value)}
                        placeholder="Role"
                        required
                    />
                    <button type="submit" className='button-primary'>Signup</button>
                </form>
                <p>already have an account?<Link to={'/login'}>Login</Link></p>
            </div>
        </div>
    );
};

export default Signup;

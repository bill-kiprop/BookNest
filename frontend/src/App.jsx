import { useState } from 'react'

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/Login.jsx';
import Signup from './components/Signup.jsx';
import Profile from './components/Profile.jsx';
import Header from './components/Header.jsx';
import Footer from './components/Footer.jsx';
import './App.css';

const App = () => {
    const [users, setUsers] = useState([]);
    const [currentUser, setCurrentUser] = useState(null);

    return (
        <Router>
            <Header currentUser={currentUser} setCurrentUser={setCurrentUser} />
            <main>
                <Routes>
                  
                    <Route path="/login" element={<Login users={users} setCurrentUser={setCurrentUser} />} />
                    <Route path="/signup" element={<Signup setUsers={setUsers} />} />
                    <Route path="/profile" element={<Profile currentUser={currentUser} setCurrentUser={setCurrentUser} />} />
                </Routes>
            </main>
            <Footer />
        </Router>
    );
};

export default App;


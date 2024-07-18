
import { Link } from 'react-router-dom';
import './Header.css';

const Header = ({ currentUser, setCurrentUser }) => {
    const handleLogout = () => {
        setCurrentUser(null);
    };

    return (
        <header className="header">
            <div className="container">
                <h1 className="logo"><Link to="/">Booknest</Link></h1>
                <nav>
                    <ul>
                        
                        {currentUser ? (
                            <>
                                <li><Link to="/profile">Profile</Link></li>
                                <li><button onClick={handleLogout}>Logout</button></li>
                            </>
                        ) : (
                            <>
                                <li><Link to="/login">Login</Link></li>
                                <li><Link to="/signup">Signup</Link></li>
                            </>
                        )}
                    </ul>
                </nav>
            </div>
        </header>
    );
};

export default Header;
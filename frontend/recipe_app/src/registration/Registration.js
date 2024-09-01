import React from 'react';
import './registration.css';
import { useNavigate } from 'react-router-dom';

const Registration = () => {
    const navigate = useNavigate();

    const handleLoginClick = () => { 
        navigate('/login');
    };

    const handleHomeClick = () => { 
      navigate('/home');
    };

  return (
    <div className="homepage-container">
      <header className="header">
        <div className="logo-container">
        <a href="home" onClick={handleHomeClick}>
        <h1>Recipe App</h1>
        </a>
          <p>Sponsored by A-G Associates</p>
        </div>
      </header>
      <main className="main">
        <section className="registration-form">
          <h2>Create Your Account</h2>
          <form>
            <label htmlFor="username">Username</label>
            <input type="text" id="username" name="username" required />
            <label htmlFor="email">Email</label>
            <input type="email" id="email" name="email" required />
            <label htmlFor="password">Password</label>
            <input type="password" id="password" name="password" required />
            <label htmlFor="confirm-password">Confirm Password</label>
            <input type="password" id="confirm-password" name="confirm-password" required />
            <button type="submit">Register</button>
          </form>
          <p>Already have an account? <a href="login" onClick={handleLoginClick}>Login</a></p>
        </section>
      </main>
      <footer className="footer">
        <p>&copy; {new Date().getFullYear()} Recipe App</p>
      </footer>

      
    </div>
  );
};

export default Registration;

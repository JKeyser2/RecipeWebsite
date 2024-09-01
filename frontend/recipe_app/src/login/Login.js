import React from 'react';
import { useState } from 'react';
import './Login.css';
import { useNavigate } from 'react-router-dom';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    
    const navigate = useNavigate();

    const handleUsernameChange = (event) => {
        setUsername(event.target.value);
    };
      
    const handlePasswordChange = (event) => {
        setPassword(event.target.value);
    };

    const handleSignUpClick = () => {
        navigate('/register');
    };

    const handleHomeClick = () => {
      navigate('/home');
    };

    const handleSubmit = (e) => {
      e.preventDefault();

      console.log('Username:', username);
      console.log('Password:', password);

      navigate('/dashboard'); //Remove when login button can verify username and password

      const formData2 = {
        the_username: username,
        the_password: password
      };
    
      fetch('http://localhost:3001/loginuser', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData2)
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        // if (data.success) {
        //   console.log("Response:", data);
        //   navigate('/dashboard');
        // } else {
        //   console.log("Login Failed!");
        // }
        //Add when verifying login for user
      })
      .catch(error => {
        console.error('Error:', error);
      });
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
            <section className="login-form">
                <h2>Welcome Back!</h2>
                <form onSubmit={handleSubmit}>
                    <label htmlFor="username">Username</label>
                    <input type="text" id="username" name="username" required onChange={handleUsernameChange}/>
                    <label htmlFor="password">Password</label>
                    <input type="password" id="password" name="password" required onChange={handlePasswordChange}/>
                    <button type="submit">Login</button>
                </form>
                <p>Don't have an account? <a onClick={handleSignUpClick} href="register">Sign Up</a></p>
            </section>
        </main>
        <footer className="footer">
            <p>&copy; {new Date().getFullYear()} Recipe App</p>
        </footer>
    </div>
);
};

export default Login;
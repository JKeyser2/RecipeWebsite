import React from 'react';
import './Homepage.css';
import { useNavigate } from 'react-router-dom';

const Homepage = () => {
  const benefits = [
    "Find Amazing Recipes",
    "Browse Through Recipes",
    "Submit Your Own Recipes",
  ];

  const navigate = useNavigate();

  const [currentBenefitIndex, setCurrentBenefitIndex] = React.useState(0);

  const handleBenefitChange = () => {
    setCurrentBenefitIndex((prevIndex) => (prevIndex + 1) % benefits.length);
  };

  const handleLoginClick = () => { 
      navigate('/login');
  };

  const handleRegisterClick = () => { 
    navigate('/register');
  };

  const handleHomeClick = () => { 
    navigate('/home');
  };


  React.useEffect(() => {
    const intervalId = setInterval(handleBenefitChange, 3000);

    return () => clearInterval(intervalId);
  }, [benefits.length]);

  return (
    <div className="homepage-container">
      <header className="header">
        <div className="logo-container">
        <a href="home" onClick={handleHomeClick}>
        <h1>Recipe App</h1>
        </a>
          <p>Sponsored by A-G Associates</p>
        </div>
        <nav className="nav">
          <a href="login" className="login" onClick={handleLoginClick}>Login</a>
        </nav>
      </header>
      <main className="main">
        <section className="benefits-container">
          <h2>Unlock Culinary Potential</h2>
          <div className="benefit-text">{benefits[currentBenefitIndex]}</div>
        </section>
        <section className="summary">
          <h3>Manage Recipes More Efficiently</h3>
          <p>
            Our Recipe App empowers you to find
            inspiration for every meal with our vast collection of recipes
            submitted by passionate food enthusiasts. Submit your own recipes to share what you enjoy
            and keep track of recipes that you need and what you do not need. Discover and expand your culinary horizons.
          </p>
        </section>
        <section className="get-started">
          <button type="button" className="get-started-btn" onClick={handleRegisterClick}>Get Started</button>
        </section>
      </main>
      <footer className="footer">
        <p>&copy; {new Date().getFullYear()} Recipe App</p>
      </footer>
    </div>
  );
};

export default Homepage;

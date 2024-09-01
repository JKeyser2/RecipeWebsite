import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './dashboard.css';

const Dashboard = () => {
  const navigate = useNavigate();

  const [activeSection, setActiveSection] = useState('search'); // Set initial state to 'search'
  const [recipes, setRecipes] = useState([]);
  const [searchText,setSearchText] = useState(''); // State to store search term

  const handleSearchChange = (event) => {
    setSearchText(event.target.value);
  }

  const handleHomeClick = () => { 
    navigate('/home');
  };

  const filteredRecipes = recipes.filter(recipe => recipe.name.toLowerCase().includes(searchText.toLowerCase())); // Filter recipes based on search term

  return (
    <div className="dashboard-container">
      <header className="dashboard-header">
        <div className="header-content">
          <a href="home" onClick={handleHomeClick}>
          <h1>Recipe App</h1>
          </a>
          <button onClick={() => navigate('/login')}>Logout</button>
        </div>

      </header>
      <div className="dashboard-wrapper">
        <nav className="dashboard-nav">
          <button
            className={activeSection === 'search' ? 'active' : ''}
            onClick={() => setActiveSection('search')}
          >
            Search
          </button>
          <button
            className={activeSection === 'view' ? 'active' : ''}
            onClick={() => setActiveSection('view')}
          >
            View Recipes
          </button>
        </nav>
        <div className="dashboard-content">
          {activeSection === 'search' && (
            <div className="search-section">
              <h3>Search Recipes</h3>
              <input type="text" value={searchText} onChange={handleSearchChange} placeholder="Search by recipe name" />
              {filteredRecipes.length === 0 ? (
                <p>No recipes found for your search.</p>
              ) : (
                <ul className="recipe-list">
                  {filteredRecipes.map((recipe, index) => (
                    <RecipeListItem
                      key={index}
                      recipe={recipe}
                    />
                  ))}
                </ul>
              )}
            </div>
          )}
          {activeSection === 'view' && (
            <div className="view-section">
              <h3>Your Recipes</h3>
              {recipes.length === 0 ? (
                <p>You haven't added any recipes yet!</p>
              ) : (
                <ul className="recipe-list">
                  {recipes.map((recipe, index) => (
                    <RecipeListItem
                      key={index}
                      recipe={recipe}
                    />
                  ))}
                </ul>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};


const RecipeForm = ({ onAddRecipe }) => {

  const handleSubmit = (event) => {
    event.preventDefault();
    const newRecipe = {
      // Get recipe data from form fields (name, ingredients, instructions, etc.)
    };
    onAddRecipe(newRecipe);
  };

  return (
    <form onSubmit={handleSubmit}>
      <button type="submit">Add Recipe</button>
    </form>
  );
};

const RecipeListItem = ({ recipe }) => {
  return (
    <li key={recipe.id}> 
      <h4>{recipe.name}</h4>
      <p>{recipe.description}</p>
    </li>
  );
};

export default Dashboard;

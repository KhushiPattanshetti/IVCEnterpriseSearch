import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Header.css';

function Header() {
  const navigate = useNavigate();

  const handleNavigateToChatbot = () => {
    navigate('/chatbot'); // Navigate to the chatbot route
  };

  return (
    <div className="header">
      <h1>Good afternoon, User</h1>
      <div className="search-container">
        <input
          type="text"
          className="search-box"
          placeholder="Ask anything about work"
        />
        <button 
          className="search-button" 
          onClick={handleNavigateToChatbot}
        >
          Search
        </button>
      </div>
    </div>
  );
}

export default Header;

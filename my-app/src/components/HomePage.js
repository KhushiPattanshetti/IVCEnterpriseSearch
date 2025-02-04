import React from 'react';
import { Link } from 'react-router-dom';

function HomePage() {
  return (
    <div>
      <h1>Welcome to My App</h1>
      <Link to="/comparison">
        <button>search</button>
      </Link>
    </div>
  );
}

export default HomePage;

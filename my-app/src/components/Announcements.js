import React from 'react';
import './Announcements.css';

function Announcements() {
  return (
    <div className="announcements">
      <h2>Announcements</h2>
      <div className="tabs">
        <span>Suggested</span>
        <span>Recent</span>
        <span>Mentions</span>
      </div>
      <div className="mentions">
        <p>Mentioned 4 times - 10m ago</p>
        <p>Mentioned once - 15h ago</p>
      </div>
    </div>
  );
}

export default Announcements;

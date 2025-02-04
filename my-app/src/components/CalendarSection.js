import React from 'react';
import './CalendarSection.css';

function CalendarSection() {
  return (
    <div className="calendar-section">
      <h3>Today</h3>
      <div className="event">
        <p>10:30-11:30 AM</p>
        <p>Conference Room B (5 Guests)</p>
        <button className="join-btn">Join</button>
      </div>
    </div>
  );
}

export default CalendarSection;

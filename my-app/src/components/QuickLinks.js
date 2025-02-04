import React from 'react';
import './QuickLinks.css';

const links = [
  { name: 'Mail', icon: '📧' },
  { name: 'Calendar', icon: '📅' },
  { name: 'My Jira', icon: '📓' },
  { name: 'Confluence', icon: '📝' },
  { name: 'OKRs', icon: '📊' },
  { name: 'Roadmap', icon: '🛣️' },
  { name: 'All Hands', icon: '🤝' },
  { name: 'PRs', icon: '🛠️' },
];

function QuickLinks() {
  return (
    <div className="quick-links">
      {links.map((link) => (
        <div className="link-item" key={link.name}>
          <span className="icon">{link.icon}</span>
          <span>{link.name}</span>
        </div>
      ))}
    </div>
  );
}

export default QuickLinks;

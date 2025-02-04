import React, { useState } from 'react';
import './Chatbot.css';

function Chatbot() {
  const [messages, setMessages] = useState([
    { sender: 'bot', text: 'Hello! How can I assist you today?' }
  ]);
  const [input, setInput] = useState('');

  const handleSend = () => {
    if (input.trim()) {
      setMessages([...messages, { sender: 'user', text: input.trim() }]);
      setInput('');

      // Simulate bot response
      setTimeout(() => {
        setMessages(prevMessages => [
          ...prevMessages,
          { sender: 'bot', text: 'This is a simulated response. Ask me anything!' }
        ]);
      }, 1000);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSend();
    }
  };

  const handleFileUpload = (e) => {
    const file = e.target.files[0];
    if (file) {
      setMessages([...messages, { sender: 'user', text: `Uploaded file: ${file.name}` }]);

      // Simulate bot response to file upload
      setTimeout(() => {
        setMessages(prevMessages => [
          ...prevMessages,
          { sender: 'bot', text: `File "${file.name}" received. Processing...` }
        ]);
      }, 1000);
    }
  };

  return (
    <div className="chatbot-container">
      
      <div className="chatbot-messages">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`chatbot-message ${msg.sender === 'bot' ? 'bot' : 'user'}`}
          >
            {msg.text}
          </div>
        ))}
      </div>
      <div className="chatbot-input">
        <input
          type="text"
          placeholder="Type a message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
        />
        <button onClick={handleSend}>Send</button>
      </div>
      <div className="chatbot-upload">
        <input
          id="file-upload"
          type="file"
          className="file-upload-input"
          onChange={handleFileUpload}
        />
      </div>
    </div>
  );
}

export default Chatbot;

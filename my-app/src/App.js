"IVC Ventures International Innovation Pvt Ltd (IVC Ventures) Confidential."
 "No license grant and not for distribution of any nature. All Rights Reserved."
import React from 'react';
import { BrowserRouter, Routes, Route} from 'react-router-dom'; 
import './App.css';
import Header from './components/Header';
import QuickLinks from './components/QuickLinks';
import Announcements from './components/Announcements';
import CalendarSection from './components/CalendarSection';
import Chatbot from './components/Chatbot'; 

function App() {
  return (
    <BrowserRouter>
      <div className="app">
        <Routes>
          {/* Main dashboard */}
          <Route 
            path="/" 
            element={
              <>
                <Header />
                <QuickLinks />
                <div className="main-content">
                  <Announcements />
                  <CalendarSection />
                </div>
              </>
            } 
          />
          
          {/* Chatbot page */}
          <Route path="/chatbot" element={<Chatbot />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;

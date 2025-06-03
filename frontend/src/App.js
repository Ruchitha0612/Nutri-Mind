import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import FoodIntakeForm from './FoodIntakeForm';
import Dashboard from './Dashboard';
import GutHealthChatbot from './GutHealthChatbot';

function App() {
  return (
    <Router>
      <div style={{ padding: 20 }}>
        <nav style={{ marginBottom: 24 }}>
          <Link to="/" style={{ marginRight: 16 }}>Food Log</Link>
          <Link to="/dashboard" style={{ marginRight: 16 }}>Dashboard</Link>
          <Link to="/chat">Chatbot</Link>
        </nav>
        <Routes>
          <Route path="/" element={<FoodIntakeForm />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/chat" element={<GutHealthChatbot />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App; 
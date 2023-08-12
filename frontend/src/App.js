// src/App.js
import React from 'react';
import Navbar from './components/Navbar';
import Dashboard from './components/Dashboard';
import ActivityForm from './components/ActivityForm';
import './App.css';

function App() {
  return (
    <div className="App">
      <Navbar />
      <Dashboard />
      <ActivityForm />
    </div>
  );
}

export default App;

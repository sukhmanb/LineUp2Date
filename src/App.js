import React from 'react';
import logo from './logo.svg';
import Welcome from './Welcome.js'
// import mattyice from '/public/design/8780.png'
import './App.css';
// THIS IS WHAT IS RENDERED BY THE APP!
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <Welcome/>
      </header>
    </div>
  );
}

export default App;

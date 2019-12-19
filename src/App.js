import React from 'react';
import logo from './logo.svg';
// import Welcome from './Welcome.js'
import Layout from './Layout.js'
// import mattyice from '/public/design/8780.png'
import './App.css';
// THIS IS WHAT IS RENDERED BY THE APP!
// THERE WILL BE A LOT OF COMPONENTS AND CONDITIONALS
//  (I.E. IF app.state.email is blank, show signup stuff <Welcome/>)
// Else show <Roster/> etc
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Layout />
      </header>
    </div>
  );
}

export default App;
// <img src={logo} className="App-logo" alt="logo" />

import './App.css';
import Dashboard from './dashboard/Dashboard';
import Homepage from './homepage/Homepage';
import Login from './login/Login';
import Registration from './registration/Registration';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Router>
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route path="/login" element={<Login />} />
        <Route path="register" element={<Registration />}/>
        <Route path="dashboard" element={<Dashboard />}/>
        <Route path="/home" element={<Homepage />} />
      </Routes>
    </Router>
    </div>
  );
}

export default App;

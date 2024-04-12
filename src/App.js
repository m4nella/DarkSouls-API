import react from 'react'
import { BrowserRouter as Router, Link, Route, Switch } from 'react-router-dom'
import NavBar from './components/NavBar'

function App() {
  return (
    <div>
      <Router>
        <Switch>
          <NavBar />
        </Switch>
      </Router>
    </div>
  );
}

export default App;

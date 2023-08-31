// routes.js
import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Header from "./components/Header";
import Sidebar from "./components/Sidebar";
import TextEditor from "./components/TextEditor";
import Toolbar from "./components/Toolbar";
const App = () => {
  return (
    <Router>
      <div className="app">
        <Header />
        <Sidebar />
        <main>
          <Switch>
            <Route path="/text-editor">
              <TextEditor />
            </Route>
            <Route path="/">
              <Toolbar />
            </Route>
          </Switch>
        </main>
      </div>
    </Router>
  );
};
export default App;

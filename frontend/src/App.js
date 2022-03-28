import React from "react";
import "./styles.css";
import Results from "./Results";
import Search from "./Search";
// import Search from './Search';

function App() {
  return (
    <div id="pagedisplay" className="App">
      <Search />
      <Results />
    </div>
  );
}

export default App;

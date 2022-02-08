import React from "react";
import { render } from 'react-dom';

import ExampleComponent from "./components/ExampleComponent";

function App() {
  return (
    <ExampleComponent />
  )
}

const rootElement = document.getElementById("root")
render(<App />, rootElement)
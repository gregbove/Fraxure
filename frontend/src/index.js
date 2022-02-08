import React from "react";
import { render } from 'react-dom';

import ExampleComponent from "./components/ExampleComponent";

function App() {
  return (
    <Header />
  )
}

const rootElement = document.getElementById("root")
render(<App />, rootElement)
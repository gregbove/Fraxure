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

// https://stackoverflow.com/questions/41956465/how-to-create-multiple-page-app-using-react
import { BrowserRouter } from 'react-router-dom';
ReactDOM.render((
  <BrowserRouter>
    <App /> {/* The various pages will be displayed by the `Main` component. */}
  </BrowserRouter>
  ), document.getElementById('root')
);

import React from "react";
import { render } from 'react-dom';

import ExampleComponent from "./components/ExampleComponent";

function App() {
  return (
    <html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple website</title>
    <link rel="stylesheet" href="css/main.css">
  </head>
  <body class="light-theme">
    <h1>Welcome to Fraxure!</h1>
    <p id="msg">Here is what we have:</p>
    <ul>
      <li class="list">Buttons!</li> 
      <li>
        
        <button class="btn">Dark</button> 
      </li> 
      <li class="list">Search bars!</li> 

      <li>
        <p id="search1"></p>
        <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Keywords to search for in filing documents">
      </li>
      <li>
        <p id="search2"></p>
        <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Company name, ticker, CIK number or individual's name">
      </li>
      <li>
        <p id="search3"></p>
        <input type="text" id="myInput" onkeyup="myFunction()" placeholder="">
      </li>  
      
      <li class="list">Another Page!</li> 
      <li>
        <a href="html/results.html">Check out the results</a>
      </li>

    </ul> 
    <script src="app.js"></script>
    <noscript>You need to enable JavaScript to view the full site.</noscript> 
  </body>
</html>
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

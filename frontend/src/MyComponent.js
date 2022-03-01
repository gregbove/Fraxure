import React from "react";
import './styles.css';
import './index.js'

const MyComponent = () => {
  return <div>
  <head> 
      <meta charset="utf-8" />
      <meta http-equiv="X-UA-Compatible" content="IE=edge" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Simple website</title>
      <link href="./styles.css" rel="stylesheet" />
  </head>
  <title>
      TITLE
  </title>
  <body class="light-theme">
      <h1>Welcome to Fracture!</h1>
      <p id="msg">Here is what we have:</p> 
      <ul>
      <li class="list">Buttons :(</li>
      <button class="btn">Dark</button>  
      <li class="list">Search bars!</li> 
      <p id="search1"></p>
      <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Keywords to search for in filing documents" /> 
      <p id="search2"></p>
      <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Company name, ticker, CIK number or individual's name" />
      <p id="search3"></p>
      <input type="text" id="myInput" onkeyup="myFunction()" placeholder="" /> 
    </ul> 
    <script src="./index.js"></script>
    <noscript>You need to enable JavaScript to view the full site.</noscript> 
  </body>
  </div>;
};

export default MyComponent; 
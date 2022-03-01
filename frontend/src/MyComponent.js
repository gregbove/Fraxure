import React from "react";
import './styles.css';
import './index.js'
 
// <li class="list">Search bars!</li> 

const MyComponent = () => {
  return <html lang="en">
  <div>
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
  <body id="body" class="light-theme">
    <h1>Fracture</h1>
    <h2>A user friendly web interface for facilitating the process of gathering information from SEC.org</h2>
    <h2>We hope this site closely resembles that of the SEC so that searches performed there can easily be performed here</h2>
    <p id="msg"></p> 
    <ul> 
      <button class="btn" >Light</button>   
      <h3 id="search1">Document word or phrase</h3> 
      <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Keywords to search for in filing documents" /> 
      <h3 id="search2">Company name, ticker, CIK number or individual's name</h3>
      <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Company name, ticker, CIK number or individual's name" />
      <h3 id="search3">Filing types</h3>
      <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Enter the filing types"/> 
      <h3 id="search3">Filed date range</h3>
      <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Select from the dropdown"/> 
      <h3 id="search3">Principle executive offices in</h3>
      <input type="text" id="myInput" onkeyup="myFunction()" placeholder="Select a state"/>  
    </ul> 
    <script src="./index.js"></script>
    <noscript>You need to enable JavaScript to view the full site.</noscript> 
  </body>
  </div>
  </html>; 
};

export default MyComponent; 
import React from "react";
import './styles.css'; 
import './index.js';

// <button class="mbtn" >Light</button>
const Demo = () => {
  return <html lang="en">
  <div class="light-theme"> 
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
    <h1>Fraxure</h1>
    <h2>A user friendly web interface for facilitating the process of gathering information from SEC.org</h2>
    <h2>We hope this site closely resembles that of the SEC so that searches performed there can easily be performed here</h2>
    <button class="linkbtn">Go to SEC.org</button>  
    <p id="msg"></p> 
    <ul>  
      <h3 id="search1">TagTog Username</h3> 
      <input type="text" id="user" onkeyup="myFunction()" placeholder="TagTog Username" /> 
      <h3 id="search2">TagTog Password</h3>
      <input type="text" id="pass" onkeyup="myFunction()" placeholder="TagTog Password" /> 
      <h3 id="search3">TagTog Project</h3>
      <input type="text" id="proj" onkeyup="myFunction()" placeholder="TagTog Project Name" /> 
      <h3 id="search3">Form Type</h3>
      <input type="text" id="type" onkeyup="myFunction()" placeholder="10-K" /> 
      <h3 id="search3">Form Ticker</h3>
      <input type="text" id="cik" onkeyup="myFunction()" placeholder="Ticker" /> 
      <h3 id="search4">Inbetween the dates of</h3>
      <input type="text" id="pre" onkeyup="myFunction()" placeholder="YYYY-MM-DD" />  
      <input type="text" id="post" onkeyup="myFunction()" placeholder="YYYY-MM-DD" /> 
      <h3 id="search4">Would you like to send invididual sections to a TagTog folder? (Y/N)</h3>
      <p>*** YOU MUST CREATE A FOLDER IN TAGTOG FIRST, AND NAME IT AFTER THE TICKER ***</p>
      <input type="text" id="folder" onkeyup="myFunction()" placeholder="N" />  
    </ul>  
    <button class="searchbtn">Enter</button>  
    <script src="./index.js"></script>
    <noscript>You need to enable JavaScript to view the full site.</noscript> 
  </body>   
  </div>
  </html>;
};

export default Demo; 
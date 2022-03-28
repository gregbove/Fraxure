import React from "react";
import './styles.css'; 
import './index.js';

// <button class="mbtn" >Light</button>
const Results = () => {
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
    <h1>Fracture</h1>
    <h2>A user friendly web interface for facilitating the process of gathering information from SEC.org</h2>
    <h2>We hope this site closely resembles that of the SEC so that searches performed there can easily be performed here</h2>
    <button class="linkbtn">Go to SEC.org</button>  
    <p id="msg"></p> 
    <ul>
    <table>
         <tr>
            <th>Form & File</th>
            <th>Filed</th>
            <th>Reporting for</th>
            <th>Filing entity/person</th>
            <th>Open with TagTog</th>
            <th>Select</th>
         </tr>
         <tr>
            <td>10-K (Annual report)</td> 
            <td>2022-03-02</td>
            <td>2021-12-31</td> 
            <td>Company A</td>  
            <td>*link*</td>  
            <td><input type="checkbox"></input></td>
         </tr>
         <tr>
            <td>10-K (Annual report)</td> 
            <td>2022-03-02</td>
            <td>2021-12-31</td> 
            <td>Company B</td>  
            <td>*link*</td>  
            <td><input type="checkbox"></input></td>
         </tr>
         <tr>
            <td>10-K (Annual report)</td> 
            <td>2022-03-02</td>
            <td>2021-12-31</td> 
            <td>Company C</td>  
            <td>*link*</td>  
            <td><input type="checkbox"></input></td>
         </tr>
         <tr>
            <td>. . . </td> 
            <td>. . . </td>
            <td>. . . </td> 
            <td>. . . </td>  
            <td>. . . </td>  
            <td>. . . </td>
         </tr>
         <tr>
            <td>. . . </td> 
            <td>. . . </td>
            <td>. . . </td> 
            <td>. . . </td>  
            <td>. . . </td>  
            <td>. . . </td>
         </tr>
         <tr>
            <td>10-K (Annual report)</td> 
            <td>2022-03-02</td>
            <td>2021-12-31</td> 
            <td>Company W</td>  
            <td>*link*</td>  
            <td><input type="checkbox"></input></td>
         </tr>
         <tr>
            <td>10-K (Annual report)</td> 
            <td>2022-03-02</td>
            <td>2021-12-31</td> 
            <td>Company X</td>  
            <td>*link*</td> 
            <td><input type="checkbox"></input></td>
         </tr>
         <tr>
            <td>10-K (Annual report)</td> 
            <td>2022-03-02</td>
            <td>2021-12-31</td> 
            <td>Company Y</td>  
            <td>*link*</td> 
            <td><input type="checkbox"></input></td>
         </tr>
         <tr>
             <td>10-K (Annual report)</td> 
            <td>2022-03-02</td>
            <td>2021-12-31</td> 
            <td>Company Z</td>  
            <td>*link*</td>
            <td><input type="checkbox"></input></td>
         </tr>
      </table>
    </ul>  
    <form>
        <button class="left">Back</button>  
        <button class="dwnldbtn">Download Selected Files</button>  
    </form>
    <script src="./index.js"></script>
    <noscript>You need to enable JavaScript to view the full site.</noscript> 
  </body>  
  </div>
  </html>;
};

export default Results; 
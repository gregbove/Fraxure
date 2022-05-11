import React from "react";
import ReactDOM from "react-dom";
import "./styles.css";
import App from "./App";

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);

// https://stackoverflow.com/questions/41956465/how-to-create-multiple-page-app-using-react

const linker = document.querySelector(".linkbtn");
linker.addEventListener("click", function () {
  window.open(
    "https://www.sec.gov/edgar/search/#/category=custom&forms=10-K",
    "_blank"
  );
  console.log("button clicked");
});

/*
const switcher = document.querySelector('.mbtn');

switcher.addEventListener('click', function() {   
    var element = document.getElementById('wrapper');
    var class_ = element.className;

    if (class_ === "dark-theme") {
        console.log('Dark theme --> Light Theme'); 
        element.classList.toggle('dark-theme'); 
        element.classList.toggle('light-theme');   
        this.textContent = "Light";
    }  
    else if(class_ === "light-theme") {
        console.log('Light theme --> Dark Theme'); 
        element.classList.toggle('light-theme');  
        element.classList.toggle('dark-theme');  
        this.textContent = "Dark"; 
    } 
    console.log('current class name: ' + element.className);

});
*/

const searcher = document.querySelector(".searchbtn");

searcher.addEventListener("click", function () {
  var username = document.getElementById("user");
  var password = document.getElementById("pass");
  var project = document.getElementById("proj");
  var type = document.getElementById("type");
  var cik = document.getElementById("cik");
  var pre = document.getElementById("pre");
  var post = document.getElementById("post");
  var yORn = document.getElementById("yORn");

  
  
  // WORKS
  // var url = "localhost:5000/tagtog/init/" + username.value + "/" + password.value + "/" + project.value + "/" + type.value + "/" + cik.value;
  
  var url = "http://127.0.0.1:5000/tagtog/init/" + username.value + "/" + password.value + "/" + project.value + "/" + type.value + "/" + cik.value;
  // var url = "empty"
  if (pre.value !== "") { 
    // url = "not_empty"
    url = "http://127.0.0.1:5000/tagtog/init/" + username.value + "/" + password.value + "/" + project.value + "/" + type.value + "/" + cik.value + "/" + pre.value + "/" + post.value + "/" + yORn.value;
  }

  // var url = "localhost:5000/tagtog/init/" + username.value + "/" + password.value + "/" + project.value;

  // var url = "localhost:5000/tagtog/init/" + username.value + "/" + password.value + "/" + project.value + "/" + type.value + "/" + cik.value + "/" + pre.value + "/" + post.value;

  fetch(url) 
  /*
  window.open(
    url,
    "_blank"
  ); 
  // window.close()
  */
  
  
  var url = "http://www.tagtog.net/" + username.value + "/" + project.value + "/"
  fetch(url) 
  window.open(
    url,
    "_blank"
  ); 
  
  

});

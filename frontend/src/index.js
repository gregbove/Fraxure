import React from "react"; 
import { render } from "react-dom";  
import MyComponent from "./MyComponent";

function App() {
  return <div><MyComponent /></div>; 
}

const rootElement = document.getElementById("root");
render(<App />, rootElement); 

// https://stackoverflow.com/questions/41956465/how-to-create-multiple-page-app-using-react

const switcher = document.querySelector('.btn');

switcher.addEventListener('click', function() {   
    var element = document.getElementById('body');
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
    console.log('current class name: ' + class_);

});

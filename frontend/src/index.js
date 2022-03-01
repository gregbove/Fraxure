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
    document.body.classList.toggle('dark-theme'); 

    var className = document.body.className;
    if(className === "light-theme") {
        this.textContent = "Dark"; 
    }
    else {
        this.textContent = "Light";  
    }

    console.log('current class name: ' + className);

});

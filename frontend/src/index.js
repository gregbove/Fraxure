import React from "react"; 
import ReactDOM from "react-dom";  
import "./styles.css"; 
import App from './App';    

const rootElement = document.getElementById("root");
ReactDOM.render(<App />,rootElement); 

// https://stackoverflow.com/questions/41956465/how-to-create-multiple-page-app-using-react

const linker = document.querySelector('.linkbtn');
linker.addEventListener('click', function() {   
    window.open('https://www.sec.gov/edgar/search/#/category=custom&forms=10-K', '_blank');
    console.log('button clicked');
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

const searcher = document.querySelector('.searchbtn');
searcher.addEventListener('click', function() {   
    // var element = document.getElementById('pagedisplay');
    // var class_ = element.className;
});

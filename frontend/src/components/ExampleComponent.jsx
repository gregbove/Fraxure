import React from "react";

const text = 'Michael Jordan ate lunch yesterday in Chicago.'

const spans = [
    {start: 0, end: 14, type: 'person'},
    {start: 25, end: 34, type: 'date'},
    {start: 38, end: 45, type: 'location'}
]

const ents = [
    {type: 'person', color: {r: 166, g: 226, b: 45}},
    {type: 'location', color: {r: 67, g: 198, b: 252}},
    {type: 'date', color: {r: 47, g: 187, b: 171}}
]

document.getElementById('ip').addEventListener('mouseup',function(e)
{
        var txt = this.innerText;
        var selection = window.getSelection();
        var start = selection.anchorOffset;
        var end = selection.focusOffset;
        if (start >= 0 && end >= 0){
    	    console.log("start: " + start);
    	    console.log("end: " + end);
        }
});

const ExampleComponent = () => {
  return (
    <Taggy text={text} spans={spans} ents={ents} />
  );
};

export default ExampleComponent;
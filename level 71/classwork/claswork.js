//1
function generateParagraph() {
    const div = document.getElementById("myDiv");
  
    const paragraph = document.createElement("p");
  
    paragraph.textContent = "ეს პარაგრაფი ავტომატურად შეიქმნა საიტის ჩატვირთვისას.";
  
    div.appendChild(paragraph);
  }
  
  window.onload = generateParagraph;
  
//2
function removeChildElement() {
    const parentDiv = document.getElementById("parentDiv");
    const childDiv = document.getElementById("childDiv");
  
    if (parentDiv && childDiv) {
      parentDiv.removeChild(childDiv);
    }
  }
  
//3
function replaceParagraph() {
    const parentDiv = document.getElementById("parentDiv");
    const oldParagraph = document.getElementById("oldParagraph");
  
    const newParagraph = document.createElement("p");
    newParagraph.textContent = "ეს არის ახალი პარაგრაფი, რომელიც ჩანაცვლდა ჩატვირთვისას.";
  
    parentDiv.replaceChild(newParagraph, oldParagraph);
  }
  
  window.onload = replaceParagraph;
  
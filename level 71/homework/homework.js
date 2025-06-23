// 2
const paragraph = document.createElement("p");
paragraph.textContent = "ეს არის დინამიურად დამატებული პარაგრაფი.";
document.body.appendChild(paragraph);

// 3
const heading = document.createElement("h1");
heading.textContent = "ეს არის სათაური";

const containerDiv = document.createElement("div");
containerDiv.appendChild(heading);
document.body.appendChild(containerDiv);

// 4
const image = document.createElement("img");
image.src = "https://via.placeholder.com/150";
image.alt = "მაგალითის სურათი";
document.body.appendChild(image);

// 5
const button = document.createElement("button");
button.textContent = "Click me";
document.body.appendChild(button);

// 6
const UL = document.createElement("ul");

const li1 = document.createElement("li");
li1.textContent = "პირველი ელემენტი";

const li2 = document.createElement("li");
li2.textContent = "მეორე ელემენტი";

const li3 = document.createElement("li");
li3.textContent = "მესამე ელემენტი";

ul.appendChild(li1);
ul.appendChild(li2);
ul.appendChild(li3);

document.body.appendChild(ul);

//7
const contentDiv = document.getElementById("content");

if (contentDiv && contentDiv.firstChild) {
  const firstChild = contentDiv.firstElementChild;
  if (firstChild) {
    contentDiv.removeChild(firstChild);
  }
}

//8

const uL = document.createElement("ul");

const li1 = document.createElement("li");
li1.textContent = "პირველი";

const li2 = document.createElement("li");
li2.textContent = "მეორე";

const li3 = document.createElement("li");
li3.textContent = "მესამე";

ul.appendChild(li1);
ul.appendChild(li2);
ul.appendChild(li3);

document.body.appendChild(ul);

const lastLi = ul.lastElementChild;
if (lastLi) {
  ul.removeChild(lastLi);
}

//9
const textContainer = document.getElementById("textContainer");
const oldParagraph = textContainer.querySelector("p");

const newParagraph = document.createElement("p");
newParagraph.textContent = "ეს არის ახალი პარაგრაფი.";

if (oldParagraph) {
  textContainer.replaceChild(newParagraph, oldParagraph);
}

//10
const divWithButton = document.querySelector("div"); 
const oldButton = divWithButton.querySelector("button");

const newSpan = document.createElement("span");
newSpan.textContent = "ახალი სპანი";

if (oldButton) {
  divWithButton.replaceChild(newSpan, oldButton);
}

//11
const ul = document.querySelector("ul");
const oldLi = ul.querySelector("li");

const newLi = document.createElement("li");
newLi.textContent = "ახალი სიის ელემენტი";

if (oldLi) {
  ul.replaceChild(newLi, oldLi);
}

//12
const h2 = document.querySelector("h2");
const parent = h2.parentElement;

const newH1 = document.createElement("h1");
newH1.textContent = "ახალი სათაური";

if (h2 && parent) {
  parent.replaceChild(newH1, h2);
}

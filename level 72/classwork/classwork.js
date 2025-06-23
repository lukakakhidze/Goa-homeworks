//1
const para = document.getElementById("myParagraph");

para.addEventListener("click", () => {
  document.body.style.backgroundColor = "black";

  document.body.style.color = "white";

  document.body.style.textAlign = "center";
});

//2
const button = document.getElementById("myButton");

button.addEventListener("click", (e) => {
  console.log(e);

  e.target.style.backgroundColor = "black";
});

//1
document.getElementById("alertButton").addEventListener("click", () => {
    alert("ღილაკი დააჭირეს!");
  });
  
//3
  const hoverParagraph = document.getElementById("hoverParagraph");
  hoverParagraph.addEventListener("mouseenter", () => {
    hoverParagraph.textContent = "მაუშის წამოღება შენიშვნა!";
  });
  hoverParagraph.addEventListener("mouseleave", () => {
    hoverParagraph.textContent = "დააყენე მაუსი აქ";
  });
  
 // 4
  const colorToggleDiv = document.getElementById("colorToggleDiv");
  let isGray = true;
  colorToggleDiv.addEventListener("click", () => {
    colorToggleDiv.style.backgroundColor = isGray ? "lightgreen" : "lightgray";
    isGray = !isGray;
  });

//5
  document.getElementById("logInput").addEventListener("click", (e) => {
    console.log("ინფუთის მნიშვნელობა:", e.target.value);
  });
  
//6
  const toggleImageButton = document.getElementById("toggleImageButton");
  const toggleImage = document.getElementById("toggleImage");
  toggleImageButton.addEventListener("click", () => {
    toggleImage.style.display = (toggleImage.style.display === "none" || toggleImage.style.display === "") ? "block" : "none";
  });
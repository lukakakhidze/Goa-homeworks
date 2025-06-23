//1
function changeButtonColor() {
    const color = prompt("შეიყვანეთ ფერი (მაგ: red, green, #ff0000):");
    const button = document.getElementById("changeColorBtn");
  
    if (color) {
      button.style.backgroundColor = color;
    }
  }
  
  document.getElementById("changeColorBtn").addEventListener("click", changeButtonColor);
  

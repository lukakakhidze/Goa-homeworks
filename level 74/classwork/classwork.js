//1
const button = document.getElementById('colorButton');
const colors = ['red', 'green', 'blue', 'orange', 'purple'];
let count = 0;
let intervalId = null;

button.addEventListener('click', () => {
  if (intervalId !== null) return;

  intervalId = setInterval(() => {
    if (count >= colors.length) {
      clearInterval(intervalId);
      intervalId = null;
      return;
    }

    button.style.backgroundColor = colors[count];
    count++;
  }, 2000); // 2 წამში ერთხელ
});

//2
const input = document.getElementById('colorInput');
const Button = document.getElementById('applyColorBtn');

button.addEventListener('click', () => {
  const color = input.value.trim();

  const isValidHex = /^#([0-9A-Fa-f]{3}){1,2}$/.test(color);

  if (isValidHex) {
    document.body.style.backgroundColor = color;
  } else {
    alert("გთხოვთ შეიყვანოთ სწორი HEX ფერი. მაგ: #ff0000 ან #0f0");
  }
});

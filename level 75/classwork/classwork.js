//1
const div = document.getElementById('myDiv');
const paragraphsInDiv = div.getElementsByTagName('p');

for (let i = 0; i < paragraphsInDiv.length; i++) {
  paragraphsInDiv[i].style.color = 'green';
  paragraphsInDiv[i].style.backgroundColor = 'black';
}

//2
function startGrowing() {
    const paragraph = document.getElementById('growingText');
    let fontSize = 10;
  
    setInterval(() => {
      fontSize++;
      paragraph.style.fontSize = fontSize + 'px';
    }, 1000);
  }

  
//3
const button = document.getElementById('moveBtn');
let leftOffset = 0;

button.addEventListener('click', () => {
  setInterval(() => {
    leftOffset -= 50;
    button.style.left = leftOffset + 'px';
  }, 1000);
});



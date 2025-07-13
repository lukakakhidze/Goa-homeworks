//1
const allParagraphs = document.querySelectorAll('p');
alert(`Total <p> tags: ${allParagraphs.length}`);

//2
const allH2s = document.querySelectorAll('h2');
allH2s.forEach(h2 => {
  h2.style.color = 'blue';
});

//3
const allListItems = document.querySelectorAll('li');
allListItems.forEach(li => {
  console.log(li.textContent);
});

//4
const allDivs = document.querySelectorAll('div');
allDivs.forEach(div => {
  div.style.backgroundColor = 'lightgray';
});

//5
const firstImg = document.querySelector('img');
if (firstImg) {
  firstImg.src = 'https://via.placeholder.com/300x200?text=New+Image';
}

//6
const highlights = document.querySelectorAll('.highlight');
highlights.forEach(el => {
  el.style.backgroundColor = 'yellow';
});

//7
const cards = document.querySelectorAll('.card');
console.log(`Total .card elements: ${cards.length}`);

//8
const errors = document.querySelectorAll('.error');
errors.forEach(el => {
  el.style.color = 'red';
});

//9
const items = document.querySelectorAll('.item');
items.forEach(el => {
  console.log(el.innerHTML);
});

//10
const firstButton = document.querySelector('.button');
if (firstButton) {
  firstButton.textContent = 'Clicked!';
}

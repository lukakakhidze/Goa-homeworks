//2
let count = 1;
const interval1 = setInterval(() => {
  console.log(count);
  if (count === 5) {
    clearInterval(interval1);
  }
  count++;
}, 1000);

//3
const interval2 = setInterval(() => {
  console.log("ეს მესიჯი გამოვა 2 წამში ერთხელ");
}, 2000);

setTimeout(() => {
  clearInterval(interval2);
  console.log("შეტყობინებები შეჩერებულია");
}, 10000);

//4
const colors = ["red", "blue", "green", "orange", "purple"];
let colorIndex = 0;
const interval3 = setInterval(() => {
  document.body.style.backgroundColor = colors[colorIndex];
  colorIndex++;
  if (colorIndex >= 5) {
    clearInterval(interval3);
    console.log("ფონის ფერის ცვლილება შეჩერებულია");
  }
}, 3000);

//5
let timeCount = 0;
const interval4 = setInterval(() => {
  const now = new Date();
  console.log("მიმდინარე დრო:", now.toLocaleTimeString());
  timeCount++;
  if (timeCount === 15) {
    clearInterval(interval4);
    console.log("დროის ჩვენება შეჩერებულია");
  }
}, 1000);

//6
let timerCount = 0;
const interval5 = setInterval(() => {
  timerCount++;
  console.log(`ტაიმერი: ${timerCount} წამი`);
  if (timerCount === 10) {
    clearInterval(interval5);
    console.log("ტაიმერი დასრულდა");
  }
}, 1000);

//7
const numbers1 = [10, 20, 30, 40];
console.log("მეორე ელემენტი:", numbers1[1]);

//8
numbers1[0] = 100;
console.log("ცვლილებით მასივი:", numbers1);

//9
const strings = ["პირველი", "მეორე", "მესამე"];
console.log(strings[0]);
console.log(strings[1]);
console.log(strings[2]);

//10
const numbers2 = [5, 10, 15, 20, 25];
const sum = numbers2[0] + numbers2[numbers2.length - 1];
console.log("პირველი და ბოლო ელემენტის ჯამი:", sum);


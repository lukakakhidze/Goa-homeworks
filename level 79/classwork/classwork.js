//1
let password;
do {
  password = prompt("Enter the password:");
} while (password !== "js123");

console.log("Correct password entered!");

//2
let num = 51;

do {
  if (num % 7 === 0) {
    console.log("First number over 50 divisible by 7 is:", num);
    break;
  }
  num++;
} while (true);

//3
const numbers = [10, 3, 5, 6, 8, 11, 20];
let evenSum = 0;
let oddSum = 0;

for (const num of numbers) {
  if (num % 2 === 0) {
    evenSum += num;
  } else {
    oddSum += num;
  }
}

console.log("Even sum:", evenSum);
console.log("Odd sum:", oddSum);

//4
const names = ['john', 'mike', 'anna', 'lisa'];

for (const name of names) {
  const capitalized = name.charAt(0).toUpperCase() + name.slice(1);
  console.log(capitalized);
}

//5
const input = "Hello World!";
let vowelCount = 0;
const vowels = "aeiouAEIOU";

for (const char of input) {
  if (vowels.includes(char)) {
    vowelCount++;
  }
}

console.log("Number of vowels:", vowelCount);

//6
const original = [2, 5, 7, 10];
const doubled = [];

for (const num of original) {
  doubled.push(num * 2);
}

console.log("Doubled numbers:", doubled);

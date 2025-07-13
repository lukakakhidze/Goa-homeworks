//1
for (let i = 1; i <= 20; i++) {
  if (i === 13) break;
  console.log(i);
}

//2
const colors = ["red", "green", "yellow", "blue", "orange"];
for (const color of colors) {
  if (color === "blue") break;
  console.log(color);
}

//3
for (let i = 1; i <= 50; i++) {
  if (i % 4 === 0 && i % 5 === 0) break;
  console.log(i);
}

//4
const word = "example";
for (const letter of word) {
  if (letter === "a") break;
  console.log(letter);
}

//5
let sum = 0;
let num = 1;
while (true) {
  sum += num;
  if (sum >= 100) break;
  num++;
}
console.log("Sum reached:", sum);

for (let i = 1; i <= 20; i++) {
    if (i === 13) continue;
    console.log(i);
  }
  
//6
  const fruits = ["apple", "banana", "grape", "banana", "orange"];
  for (const fruit of fruits) {
    if (fruit === "banana") continue;
    console.log(fruit);
  }
  
//7
  for (let i = 1; i <= 30; i++) {
    if (i % 3 === 0) continue;
    console.log(i);
  }
  
//8
  const text = "elephant";
  for (const ch of text) {
    if (ch === "e") continue;
    console.log(ch);
  }
  
//9
  for (let i = 1; i <= 50; i++) {
    if (i % 2 === 0) continue;
    console.log(i);
  }

//10
const add = (a, b) => a + b;

//11
const greet = name => `Hello, ${name}!`;

//12
const doubleArray = arr => arr.map(n => n * 2);

//13
const isEven = n => n % 2 === 0;

//14
const lengthOfString = str => str.length;

console.log(add(3, 7));           
console.log(greet("David"));     
console.log(doubleArray([1,2,3])); 
console.log(isEven(10));          
console.log(lengthOfString("hello")); 

//15
function printArgs() {
    for (const arg of arguments) {
      console.log(arg);
    }
  }
  
//16
  function countArgs() {
    console.log("Number of arguments:", arguments.length);
  }
  
//17
  function sumArgs() {
    let total = 0;
    for (const arg of arguments) {
      if (typeof arg === "number") total += arg;
    }
    console.log("Sum:", total);
  }
  
//18
  function printUntilZero() {
    for (const arg of arguments) {
      if (arg === 0) break;
      console.log(arg);
    }
  }
  
//19
  function printNumbersOnly() {
    for (const arg of arguments) {
      if (typeof arg === "string") continue;
      console.log(arg);
    }
  }
  
  printArgs(1, "a", 3, 0);
  countArgs(1, 2, 3);
  sumArgs(1, "b", 5, 10);
  printUntilZero(4, 5, 0, 6);
  printNumbersOnly(1, "hello", 2, "world", 3);
  
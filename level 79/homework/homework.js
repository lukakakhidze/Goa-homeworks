//1
const person = { name: 'John', age: 30 };
const keys = [];

for (const key in person) {
  keys.push(key);
}

console.log(keys); 

//2
const data = { a: 10, b: 'hi', c: 20 };
let total = 0;

for (const key in data) {
  if (typeof data[key] === 'number') {
    total += data[key];
  }
}

console.log("Total:", total);

//3
const obj = { name: 'John', age: 30, city: 'Paris' };
let result = "";

for (const key in obj) {
  result += `${key}=${obj[key]}, `;
}

result = result.slice(0, -2);
console.log(result); 

//4
const Person = { name: 'Alice', age: 25, isStudent: true };

for (const key in person) {
  console.log(`${key}: ${typeof person[key]}`);
}

//5
const object = {
    name: "Tom",
    age: 40,
    address: {
      city: "Tbilisi"
    }
  };
  
  for (const key in obj) {
    if (typeof obj[key] === 'object' && obj[key] !== null && !Array.isArray(obj[key])) {
      console.log(`Nested object found at key: ${key}`);
    }
  }
  
//6
const words = ["hello", "elephant", "sky", "mountain", "cat"];

for (const word of words) {
  if (word.length > 5) {
    console.log(word);
  }
}

//7
const chars = ['H', 'e', 'l', 'l', 'o'];
let word = "";

for (const ch of chars) {
  word += ch;
}

console.log(word); 

//8
let num = 1;

do {
  console.log(num);
  num *= 2;
} while (num <= 1000);

//9
const inputs = [];
let value;

do {
  value = prompt("Enter a number (type 'stop' to finish):");
  if (value.toLowerCase() !== "stop") {
    inputs.push(value);
  }
} while (value.toLowerCase() !== "stop");

console.log(inputs);

//10
let count = 30;

do {
  console.log(count);
  count -= 3;
} while (count >= 0);

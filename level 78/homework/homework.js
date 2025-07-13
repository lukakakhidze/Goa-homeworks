// 4. Print numbers from 1 to 5 using do...while
let i = 1;
do {
  console.log("4:", i);
  i++;
} while (i <= 5);

// 5. Even numbers from 2 to 10 using do...while
let j = 2;
do {
  if (j % 2 === 0) {
    console.log("5:", j);
  }
  j++;
} while (j <= 10);

// 6. Numbers from 10 down to 1 using do...while
let k = 10;
do {
  console.log("6:", k);
  k--;
} while (k >= 1);

// 7. Ask for number > 100
let num;
do {
  num = parseFloat(prompt("7: Enter a number greater than 100:"));
} while (num <= 100);
console.log("7: You entered", num);

// 8. Sum numbers from 1 to 10
let sum = 0;
let m = 1;
do {
  sum += m;
  m++;
} while (m <= 10);
console.log("8: Total sum is", sum);

// 9. Print each number in array
let numbers = [3, 7, 12, 5, 9];
for (let n of numbers) {
  console.log("9:", n);
}

// 10. Print each character of string
let word = "hello";
for (let char of word) {
  console.log("10:", char);
}

// 11. Sum all numbers in array
let nums = [1, 2, 3, 4, 5];
let total = 0;
for (let n of nums) {
  total += n;
}
console.log("11: Sum is", total);

// 12. Print even numbers from array
let numArr = [2, 5, 8, 11, 14, 17];
for (let n of numArr) {
  if (n % 2 === 0) {
    console.log("12:", n);
  }
}

// 13. Print all names from array
let names = ["Ana", "Luka", "Mariam", "Gio"];
for (let name of names) {
  console.log("13:", name);
}

// 14. Print all keys of object
let person = {
  name: "Nino",
  age: 22,
  country: "Georgia"
};
for (let key in person) {
  console.log("14: Key:", key);
}

// 15. Print all values of object
for (let key in person) {
  console.log("15: Value:", person[key]);
}

// 16. Count number of properties
let count = 0;
for (let key in person) {
  count++;
}
console.log("16: Property count:", count);

// 17. Check if key exists
let checkKey = "age";
let found = false;
for (let key in person) {
  if (key === checkKey) {
    found = true;
    break;
  }
}
console.log("17: Key exists?", found);

// 18. Create string listing all keys
let keyString = "";
for (let key in person) {
  keyString += key + ", ";
}
keyString = keyString.slice(0, -2);
console.log("18: All keys:", keyString);

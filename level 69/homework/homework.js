//2
let number = parseInt(prompt("2) Enter a number to check even or odd:"));
console.log("Result:", number % 2 === 0 ? "Even" : "Odd");

//3
let score = parseInt(prompt("3) Enter your score:"));
if (score >= 90) console.log("Grade A");
else if (score >= 80) console.log("Grade B");
else if (score >= 70) console.log("Grade C");
else if (score >= 60) console.log("Grade D");
else console.log("Fail");

//4
let a = parseFloat(prompt("4) Enter first number:"));
let b = parseFloat(prompt("Enter second number:"));
let c = parseFloat(prompt("Enter third number:"));
if (a === b && b === c) console.log("All numbers are equal.");
else if (a >= b && a >= c) console.log("Largest:", a);
else if (b >= a && b >= c) console.log("Largest:", b);
else console.log("Largest:", c);

//5
let char = prompt("5) Enter a letter:").toLowerCase();
if (char.length === 1 && /[a-z]/.test(char)) {
    if ("aeiou".includes(char)) console.log("Vowel");
    else console.log("Consonant");
} else {
    console.log("Invalid input.");
}

//6
let n = parseInt(prompt("6) Enter a number:"));
if (n % 3 === 0 && n % 5 === 0) console.log("Divisible by both");
else if (n % 3 === 0) console.log("Divisible by 3 only");
else if (n % 5 === 0) console.log("Divisible by 5 only");
else console.log("Not divisible by 3 or 5");

//7
let age = parseInt(prompt("7) Enter your age:"));
if (age >= 0 && age <= 12) console.log("Child");
else if (age >= 13 && age <= 19) console.log("Teenager");
else if (age >= 20 && age <= 59) console.log("Adult");
else if (age >= 60) console.log("Senior");
else console.log("Invalid age");

//8
let i = 1;
console.log("8) Numbers from 1 to 5:");
while (i <= 5) {
    console.log(i);
    i++;
}

//9
i = 2;
console.log("9) Even numbers from 2 to 10:");
while (i <= 10) {
    console.log(i);
    i += 2;
}

//10
i = 10;
console.log("10) Numbers from 10 down to 1:");
while (i >= 1) {
    console.log(i);
    i--;
}

//11
console.log("11) Numbers from 1 to 10:");
for (let j = 1; j <= 10; j++) {
    console.log(j);
}

//12
console.log("12) First 5 multiples of 3:");
for (let j = 1; j <= 5; j++) {
    console.log(j * 3);
}

//13
console.log("13) Numbers from 10 to 1 (reverse):");
for (let j = 10; j >= 1; j--) {
    console.log(j);
}

//14
console.log("14) Even numbers from 1 to 20:");
for (let j = 1; j <= 20; j++) {
    if (j % 2 === 0) console.log(j);
}

//15
let sum = 0;
for (let j = 1; j <= 5; j++) {
    sum += j;
}
console.log("15) Sum from 1 to 5:", sum);

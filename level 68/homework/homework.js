//2
let num1 = 15;
let num2 = 20;
console.log("Both greater than 10:", num1 > 10 && num2 > 10);

//3
let isSunny = true;
let isWeekend = false;
console.log("Is sunny or weekend:", isSunny || isWeekend);

//4
let isRaining = false;
console.log("Is not raining:", !isRaining);

//5
let a = 12;
let b = 5;
let c = true;
console.log("Complex logic:", (a > 10 && b < 10) || !c);

//6
let num = 123;
let strNum = String(num);
console.log("String version:", strNum, typeof strNum);

//7
let boolVal = true;
let strBool = String(boolVal);
console.log("String of boolean:", strBool, typeof strBool);

//8
let numericString = "456";
let convertedNum = Number(numericString);
console.log("Converted number:", convertedNum, typeof convertedNum);

//9
console.log("true as number:", Number(true));  
console.log("false as number:", Number(false));

//10
console.log("Non-numeric string to number:", Number("hello")); 

//11
let userInput = prompt("Enter a number:");
let userNumber = Number(userInput);
if (userNumber > 0) {
  alert("The number is positive.");
} else if (userNumber < 0) {
  alert("The number is negative.");
} else {
  alert("The number is zero.");
}

//12
let ageInput = prompt("Enter your age:");
let age = Number(ageInput);
if (age >= 18) {
  alert("You can vote!");
} else {
  alert("You are not eligible to vote.");
}

//13
let first = Number(prompt("Enter the first number:"));
let second = Number(prompt("Enter the second number:"));
if (first > second) {
  alert("The first number is larger.");
} else if (second > first) {
  alert("The second number is larger.");
} else {
  alert("Both numbers are equal.");
}

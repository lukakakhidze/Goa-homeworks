//1
const user = { name: "Nino", age: 28 };
const greeting = `Hello, ${user.name}! You are ${user.age} years old.`;
console.log(greeting);

//2
const poem = `Roses are red,
Violets are blue,
JavaScript is fun,
And so are you.`;

console.log(poem);

//3
const a = 5;
const b = 7;
const message = `Numbers: ${a} and ${b}
Sum: ${a + b}
Product: ${a * b}`;

console.log(message);

//4
const light = "yellow";

switch (light) {
  case "red":
    console.log("Stop");
    break;
  case "yellow":
    console.log("Get ready to move");
    break;
  case "green":
    console.log("Go");
    break;
  default:
    console.log("Invalid traffic light color");
}

//5
const operation = "multiply";
const num1 = 10;
const num2 = 5;
let result;

switch (operation) {
  case "add":
    result = num1 + num2;
    break;
  case "subtract":
    result = num1 - num2;
    break;
  case "multiply":
    result = num1 * num2;
    break;
  case "divide":
    result = num2 !== 0 ? num1 / num2 : "Cannot divide by zero";
    break;
  default:
    result = "Invalid operation";
}

console.log(`Result: ${result}`);

//6
const month = "March";
let season;

switch (month.toLowerCase()) {
  case "december":
  case "january":
  case "february":
    season = "Winter";
    break;
  case "march":
  case "april":
  case "may":
    season = "Spring";
    break;
  case "june":
  case "july":
  case "august":
    season = "Summer";
    break;
  case "september":
  case "october":
  case "november":
    season = "Autumn";
    break;
  default:
    season = "Unknown month";
}

console.log(`${month} is in ${season}`);

//7
const role = "editor";

switch (role) {
  case "admin":
    console.log("Full access granted.");
    break;
  case "editor":
    console.log("Can edit content.");
    break;
  case "subscriber":
    console.log("Can view content.");
    break;
  default:
    console.log("Role not recognized.");
}

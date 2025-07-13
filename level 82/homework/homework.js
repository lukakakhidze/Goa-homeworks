//1
const multiply = function(a, b) {
    return a * b;
  };
  console.log(multiply(4, 5)); // 20
  
//2
  const intervalId = setInterval(function() {
    console.log("Logging every 2 seconds...");
  }, 2000);
  
  
//3
  const button = document.createElement('button');
  button.textContent = "Click me";
  document.body.appendChild(button);
  
  button.addEventListener('click', function() {
    alert("Button clicked!");
  });
  
//4
const add = (a, b) => a + b;

//5
const isEven = n => n % 2 === 0;

//6
const lengths = arr => arr.map(str => str.length);

//7
const filterNegatives = arr => arr.filter(num => num >= 0);

console.log(add(3, 7));              
console.log(isEven(10));              
console.log(lengths(["hi", "hello"])); 
console.log(filterNegatives([-2, 3, 0, -5])); 

//8
(function() {
    console.log("Hello, world!");
  })();
  
//9
  (function(num) {
    console.log(num * num);
  })(5); 
  
//10
  (function(arr) {
    const sum = arr.reduce((acc, val) => acc + val, 0);
    console.log("Sum:", sum);
  })([1, 2, 3, 4]); 
  
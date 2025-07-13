//1
let i = 1;

while (i <= 20) {
  if (i >= 10 && i <= 15) {
    i++;
    continue;
  }
  console.log(i);
  i++;
}

//2
const isEven = (num) => num % 2 === 0;

console.log(isEven(4));  
console.log(isEven(7));  

//3
function processParams(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10) {
    const args = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10];
  
    for (let i = 0; i < args.length; i++) {
      if (typeof args[i] === 'number') {
        console.log(args[i]);
      } else if (typeof args[i] === 'string') {
        args[i] = 1;
      }
    }
  
    console.log("Final array:", args);
  }
  
  processParams(5, "hello", 12, "test", 100, 0, "js", 7, "data", 33);
  
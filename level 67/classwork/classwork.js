//3//
function compareNums(num1, num2) {
    console.log(`შედარება: ${num1} და ${num2}`);
  
    console.log(`${num1} > ${num2}:`, num1 > num2);
    console.log(`${num1} >= ${num2}:`, num1 >= num2);
    console.log(`${num1} < ${num2}:`, num1 < num2);
    console.log(`${num1} <= ${num2}:`, num1 <= num2);
    console.log(`${num1} == ${num2}:`, num1 == num2);
    console.log(`${num1} === ${num2}:`, num1 === num2);
    console.log(`${num1} != ${num2}:`, num1 != num2);
    console.log(`${num1} !== ${num2}:`, num1 !== num2);
  
    console.log('-------------------------');
  }
  
  compareNums(10, 5);        
  compareNums(7, 7);         
  compareNums("10", 10);    
  
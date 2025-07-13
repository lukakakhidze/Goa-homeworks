//1
const printValues = function(obj) {
    for (const key in obj) {
      console.log(obj[key]);
    }
  };
  
  const user = {
    name: "Nika",
    age: 25,
    city: "Tbilisi"
  };
  
  printValues(user);
  
//2
const result = ((arr) => {
    let product = 1;
    for (const num of arr) {
      product *= num;
    }
    return product;
  })([2, 3, 4]);  
  
  console.log("Product:", result); 
  
//3
const reversed = (function(str) {
    return str.split('').reverse().join('');
  })("JavaScript");
  
  console.log("Reversed:", reversed); 
  
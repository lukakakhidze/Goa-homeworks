//1
const product = {
    name: "Wireless Mouse",
    price: 49.99,
    inStock: true
  };
  
  const info = `Product: ${product.name}, Price: $${product.price}, Status: ${product.inStock ? "In stock" : "Out of stock"}`;
  console.log(info);
  
//2
const dayNumber = 3; 

switch (dayNumber) {
  case 1:
    console.log("Monday");
    break;
  case 2:
    console.log("Tuesday");
    break;
  case 3:
    console.log("Wednesday");
    break;
  case 4:
    console.log("Thursday");
    break;
  case 5:
    console.log("Friday");
    break;
  case 6:
    console.log("Saturday");
    break;
  case 7:
    console.log("Sunday");
    break;
  default:
    console.log("Invalid day number. Please enter 1 to 7.");
}

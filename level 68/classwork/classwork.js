//1//
function logicalFunc(bool1, bool2) {
    console.log(`true ${bool1}, false ${bool2}`);
    console.log("true && false", bool1 && bool2);  
    console.log("true || false", bool1 || bool2);  
    console.log("------------------------");
  }
  
  logicalFunc(true, true);     
  logicalFunc(true, false);    
  logicalFunc(false, false);  

//2//
function typeConvert() {
    let userInput = prompt("შეიყვანე რიცხვი:");
    
    console.log("მიღებული მნიშვნელობა:", userInput);
    console.log("ტიპი:", typeof userInput);
    
    let convertedNumber = Number(userInput);
    
    console.log("გარდაქმნილი მნიშვნელობა:", convertedNumber);
    console.log("ტიპი გარდაქმნის შემდეგ:", typeof convertedNumber);
  }
  

//3//
function forConditions() {
    let userNum = Number(prompt("Enter number:"));

    if (userNum >= 0 && userNum < 18) {
        console.log("not adult");
    } else if (userNum >= 18 && userNum < 65) {
        console.log("adult & not old");
    } else if (userNum >= 65 && userNum <= 113) {
        console.log("retired");
    } else if (userNum > 113) {
        console.log("lie");
    } else {
        console.log("Invalid age");
    }
}

//1
function usingWhileLoop() {
    let num = 0;

    while (num < 100){
        console.log(num);
        num++
    }
}

usingWhileLoop();

//2
function correctUserPassword() {
    const correctPassword = "mypassword"; 
    let attempts = 0;
    let userPassword;
  
    while (userPassword !== correctPassword) {
      userPassword = prompt("გთხოვ, შეიყვანე პაროლი:");
      attempts++;
    }
  
    alert("სწორია! ცდების რაოდენობა: " + attempts);
  }
  
  correctUserPassword();
  

//3
for (let i = 0; i < 10; i++) {
    console.log("ლუკა კახიძე");
}


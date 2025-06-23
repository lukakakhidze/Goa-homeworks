//1
let count = 0; 

let interval = setInterval(function() { 
    console.log("luka"); 
    count++; 

    if (count === 4) { 
        clearInterval(interval); 
    }
}, 5000);

//2
let myArray = ["Hello", 12, true, { name: "Luka", age: 12 }];

console.log(myArray);

console.log(myArray[1]);

//3
function printArrayElements(array) {
    for (let i = 0; i < array.length; i++) {
        console.log(array[i]); 
    }
}

printArrayElements([10, 20, 30, 40, 50]);

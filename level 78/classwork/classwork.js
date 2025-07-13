//1
let total = 0;
let number;

do {
  number = parseFloat(prompt("შეიყვანე რიცხვი:"));
  total += number;
} while (total <= 100);

alert("საკმარისია! ჯამი არის: " + total);

//2
let myObj = {
    name: "David",
    surname: "Tezelashvili",
    academy: "GOA",
    isMentor: true,
    num: 100,
    hobbies: ["programming", "bike", "basketball"],
    favColor: "Blue"
};

let ul = document.getElementById("myList");

for (let key in myObj) {
    let liKey = document.createElement("li");
    liKey.textContent = "Key: " + key;

    let liValue = document.createElement("li");

    if (Array.isArray(myObj[key])) {
        liValue.textContent = "Value: " + myObj[key].join(", ");
    } else {
        liValue.textContent = "Value: " + myObj[key];
    }

    ul.appendChild(liKey);
    ul.appendChild(liValue);
}

//3
let myArray = ["hello", "world", 5, 15, true, false];

for (let item of myArray) {
    if (typeof item === "string") {
        console.log(item);
    } else if (typeof item === "number") {
        console.log(item + 10);
    } else if (typeof item === "boolean") {
        console.log(!item);
    }
}

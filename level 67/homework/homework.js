//1//
let emptyObj = {};
console.log("Empty object:", emptyObj);

//2//
let person = {
  name: "luka",
  age: 11,
  city: "Tbilisi"
};
console.log("Person object:", person);

//3//
console.log("Name:", person.name);

//4//
person.hobby = "reading";
console.log("After adding hobby:", person);

//5//
let student = {
  id: 1,
  info: {
    name: "Nino",
    grade: 10,
    subjects: ["Math", "English"]
  }
};
console.log("Nested object (student):", student);
console.log("Student's grade:", student.info.grade);

//6//
person.age = 19;
console.log("Updated age in person object:", person);

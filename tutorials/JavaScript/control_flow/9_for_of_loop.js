// this loop is similar to python's for loop

// syntax
// for (variable of obj1) {
//     // prints all the keys in
//     // obj1 on the console
//     console.log(variable)
// }

// example 1
const array = [1,2,3,4,5];
for (const item of array) {
    console.log(item)
}


// example 2
const str = "Hello";
for (const char of str) {
    console.log(char)
}


// example 3
const map = new Map([
    ["name", "Akash"],
    ["age", 25],
    ["city", "Noida"]
]);

for (let [key, value] of map) {
    console.log(`${key}: ${value}`)
}


// example 4
let set = new Set([1,2,3,4,5]);
for (let value of set) {
    console.log(value)
}


// example 5
const person = {
    name: "Akash",
    age: 25,
    city: "Noida"
};

for (let key of Object.keys(person)) {
    console.log(`${key}: ${value}`)
}
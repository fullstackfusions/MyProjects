// arrow functions are same as lambda functions in python

const a = ["Hydrogen", "Helium", "Lithium", "Beryllium"]

// normal definition of function
const a2 = a.map(function (s) {
    return s.length
})
console.log("Normal way", a2)


// arrow function definition
const a3 = a.map((s) => s.length);
console.log("Using Arrow function ", a3);

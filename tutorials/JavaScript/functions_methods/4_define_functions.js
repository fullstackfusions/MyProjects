// functions can be initialized in following ways:

// example 1: function declarations (named function)
// example 2: function expressions
// example 3: function contructor
// example 4: function hoisting (possible with only function declaration)
// example 5: self-invoking functions
// example 6: functions are objects so it can have properties and methods
// example 7: arrow function
// example 8: anonymous function



// example 1: function declaration
function multiply( num1, num2 ) {
    return num1 * num2
}
console.log(multiply(24, 4))



// example 2: function expression
let var1 = function( num1, num2 ) {
    return num1 * num2
}
console.log(var1(24, 4))



// example 3: function constructor
let GFG = new Function("num1", "num2", "return num1 * num2")
let multiplied_value = GFG(24, 4)
console.log(multiplied_value)



// example 4: function hoisting
// hoising meaning move function declaration to the top of their scope, allowing them to be used before declaration
GeeksForGeeks();
function GeeksForGeeks() {
    console.log("Hello Geeks!")
}



// example 5: self-invoking functions
(function () {
    console.log("Hello I am self invoking")
})()



// example 6: functions as object
function Multiply(num1, num2) {
    return arguments.length
}
console.log(Multiply(4,3))



// example 7: arrow function
const var2 = (num1, num2) => num1 * num2
console.log(var2(3,4))



// example 8: anonymous function
let calSub = function (x, y) {
    let z = x - y;
    return z;
}
console.log("Subtraction: " + calSub(7, 4));
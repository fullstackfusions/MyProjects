// parameters or arguments refers same and can be passed as following:

// example 1: default parameters
// example 2: function rest parameter
// exmaple 3: arguments object
// example 4: arguments pass by value
// example 5: objects passed by reference



// example 1: default parameters
function GFG(num1, num2 = 2) {
    return num1 * num2
}
console.log(GFG(4))


// example 2: function rest parameter
function sum(...numbers) {
    return numbers.reduce((acc, num) => acc + num, 0);
}
console.log(sum(1,2,3)); // 6
console.log(sum(1,2,3,4,5,16)); // 31
console.log(sum(10)); // 10
console.log(sum()); // 0



// exmaple 3: arguments object
// arguments is an inherited feature from JavaScript Function.
function GMG() {
    let i;
    let maximum = -Infinity;
    for (i = 0; i < arguments.length; i++) {
        if (arguments[i] > maximum) {
            maxnum = arguments[i];
        }
    }
    return maxnum;
}
console.log(GMG(10, 12, 500, 5, 400, 231))



// example 4: arguments pass by value
function GeeksForGeeks(var1, var2) {
    console.log("Inside the GeeksForGeeks function");
    var1 = 100;
    var2 = 200;
    console.log("var1 =" + var1 + "var2 =" + var2);
}
var1 = 10;
var2 = 20;
console.log("Before function calling")
console.log("var1 =" + var1 + "var2 =" + var2);
GeeksForGeeks(var1, var2)
console.log("After function calling")
console.log("var1 =" + var1 + "var2 =" + var2);



// example 5: objects passed by reference
function GeeksForGeeksByReference(varObj) {
    console.log("Inside GeeksForGeeks function")
    varObj.a = 100;
    console.log(varObj.a);
}

varObj = {a: 1};
console.log("Before function calling")
console.log(varObj.a);

GeeksForGeeksByReference(varObj)
console.log("After function calling")
console.log(varObj.a)
// Block Scope
// Global Scope
// Function Scope

// Block Scope
{
    let num = 10;
    console.log(num); // 10
}
console.log(num); // ReferenceError: num is not defined


// Global Scope
let num = 10;
console.log(num);

function fun() {
    console.log(num);
}

fun();


// Function Scope
function fun() {
    let num = 10;
    console.log(num);
}

fun();
console.log(num); // ReferenceError: num is not defined
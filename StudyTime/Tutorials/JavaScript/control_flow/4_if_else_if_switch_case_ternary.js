
// if statement
let num = 20;
if (num % 2 === 0) {
    console.log('Given number is even number.')
}

if (num % 2 !== 0) {
    console.log('Given number is odd number.')
}


// if else statement
let age = 20;
if (age >= 18) {
    console.log('You are eligible for driving license.')
} else {
    console.log('You are not eligible for driving license.')
}


// if... else if... else statement
const n = 0
if (n > 0) {
    console.log('Given number is positive')
} else if (n < 0) {
    console.log('Given number is negative')
} else {
    console.log('Given numnber is zero.')
}



// switch case statement
const marks = 85;
let Branch;
switch (true) {
    case marks >= 90:
        Branch = 'Computer science engineering';
        break;
    case marks >= 80:
        Branch = 'Mechanical engineering';
        break;
    case marks >= 70:
        Branch = 'Chemical engineering';
        break;
    case marks >= 60:
        Branch = 'Electronics and Communication engineering';
        break;
    case marks >= 50:
        Branch = 'Civil engineering';
        break;
    default:
        Branch = 'Bio technology';
        break;
}
console.log(`Student Branch name is: ${Branch}`)



// Ternary Operator
let age = 21;
const result = (age >= 18) ? 'You are eligible to vote' : 'You are not eligible to vote'


// nested if else
let weather = 'sunny';
let temperature = 25;

if (weather === 'sunny') {
    if (temperature > 30) {
        console.log("It's a hot day!");
    } else if (temperature > 20) {
        console.log("It's a warm day.")
    } else {
        console.log("It's a bit cool today.")
    }
} else if (weather === 'rainy') {
    console.log("Don't forget your umbrella!");
} else {
    console.log("Check the weather forecast!")
}
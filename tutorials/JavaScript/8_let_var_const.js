// Assignment operator

y = 'Mihir'


// var
var a = "Hello World!";
var b = 10;
var c = 12;
var d = b + c;

console.log(a);
console.log(b);
console.log(c);
console.log(d);

var d = 10;
console.log(d); // this is possible with var even though it is defined earlier

var test1 = 12,
test2 = 14,
test3 = 16

function foo() {
    console.log(test1, test2, test3) // 12 14 16
}
foo()


// let
let a = "Hello World!";
let b = 10;
let c = 12;
let d = b + c;


console.log(a);
console.log(b);
console.log(c);
console.log(d);

let d = 10;      // with let, we cannot reassign the value in same block
console.log(d); // SyntaxError: Identifier 'd' has already been declared

// const
const a = 'Hello World!';
const b = 100;
const c = '12';
console.log(a);
console.log(b);
console.log(c);

const c = 'new';   // we cannot redeclare anywhere
console.log(c); // SyntaxError: Identifier 'c' has already been declared


// const values in different scope
const x = 22;
{
    const x = 90;
    console.log(x);
    {
        const x = 77;
        console.log(x);
    }
    {
        const x = 10;
        console.log(x);
    }
}
console.log(x);


// const array and chaning content in array
const arr1 = ['Pankaj', 'John', 'Mike', 'Gondal'];
console.log(arr1.toString());
arr1[2] = 'Narayan';
console.log(arr1.toString())


// const object and changing content in object
const person = {
    first_name: 'Pankaj',
    last_name: 'Singh',
    Age: 20,
    About: 'Web Developer and Competitive Programmer'
};
console.log(person);
// it is possible to change
person.first_name = 'Aryan';
person.last_name = 'Yadav';
person.Age = 22;
person.About = 'Commerce Graduate'

console.log(person);

// it is not possible to change as following
// const person = {
//     first_name: 'Aryan',
//     last_name: 'Yadav',
//     Age: 22,
//     About: 'Commerce Graduate'
// };
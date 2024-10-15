// Primitive type data types

// Number
// String
// Boolean
// null
// undefined
// Symbol
// BigInt

// Non-primitive type data types

// Object
// Array


// Number
let num = 2; // Integer
let num2 = 1.3; // Floating point number
let num3 = Infinity // Infinity
let num4 = 'something here too' / 2;    // NaN

// String
let str = 'Hello There';
let str2 = 'Single quotes work fine';
let phrase = `can embed ${str}`;

// Boolean
let isCoding = true;
let isOld = false;

// null
let age = null;

// undefined
let x;
console.log(x);  // output: undefined

// Symbol
// Symbols are primarily used for creating unique property keys in objects
let symbol1 = Symbol('Mihir')
let symbol2 = Symbol('Mihir')

// Each time Symbol() method is used to create new global symbol
console.log(symbol1 == symbol2); // false (becuase symbols are always unique)

// BigInt
// a way to represent whole numbers greater than 2^53.
let bigint = BigInt('0b1010101001010101001111111111111111')
console.log(bigint) // 11430854655n


// Object

let person = new Object();  // using object constructor syntax
let persons = {}; // object literal syntax

// Array
let numbers = [1, 2, 3, 4, 5];
let mixedArray = [1, 'two', {name: 'object'}, [3, 4, 5]]
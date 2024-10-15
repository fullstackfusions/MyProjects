// when a comma operator is placed in an expression, it executes each expression and returns the rightmost expression

function func1() {
    console.log('one');
    return 'one';
}

function func2() {
    console.log('two');
    return 'two';
}

function func3() {
    console.log('three');
    return 'three';
}

let x = (func1(), func2(), func3());
console.log(x)
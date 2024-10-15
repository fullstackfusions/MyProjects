
// example 1: using `this` in implicit binding
const person = {
    name: 'Ram',
    age: 22,
    greet: function() {
        return `Hello ${this.name}, you are ${this.age} years old`
    }
}

console.log(person.greet())


// example 2: using `this` in a function
function greet() {
    console.log('Hello, my name is ' + this.name);
}
const person = {
    name: 'John',
    sayHello: greet
};

const anotherPerson = {
    name: 'Alice'
};

greet();
person.sayHello();
greet.call(anotherPerson);


// example 3: using `this` in a method
const person = {
    name: 'John',
    age: 30,
    greet() {
        console.log('Hello, my name is ' + this.name + ' and I am ' + this.age + ' years old.')
    }
};
person.greet()


// example 4: using `this` alone
console.log(this)


// example 5: using `this` explicit binding
function ageVerify() {
    console.log(this.age)
    if(this.age > 18) {
        console.log('Yes you can drive');
    } else {
        console.log('No you cannot drive');
    }
}

const per1 = {age: 21};
const per2 = {age: 16};
ageVerify.call(per1);
ageVerify.call(per2);


// example 6: using `this` in default binding
// when this keyword is used in global scope this is set to window object
const age = 22;
function verifyAge () {
    return this.age;
}
console.log(verifyAge())


// example 7: using `this` in arrow function binding
// when this is used in the arrow function then this has lexical scope so without the function keyword this is unable to refer to the object in th outer scope
const person = {
    name: 'Ram',
    age: 22,
    greet: () => {
        return `Hello, you are ${this.age} years old`
    }
}
console.log(person.greet());
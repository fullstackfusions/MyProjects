// example 1: mix
// example 2: invoke normal function
// example 3: invoke arrow function
// example 4: using object parameter
// example 5: using `call` method
// example 6: using `apply` method
// example 7: simple calling function
// example 8: invoking specific function
// example 9: invoke a function with passing parameter
// example 10: invoke a function inside object with parameter using call


// example 1: mix
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

greet();  // simply calling function
person.sayHello();  // invoking object parameter
greet.call(anotherPerson);  // invoking function using `call` method



// example 2: invoke normal function
const person1 = {
    name: 'Ram',
    age: 22,
    greet: function() {
        return `Hello ${this.name}, you are ${this.age} years old`
    }
}
console.log(person1.greet())



// example 3: invoke arrow function
const person2 = {
    name: 'Ram',
    age: 22,
    greet: () => {
        return `Hello, you are ${this.age} years old`
    }
}
console.log(person2.greet());



// example 4: using object parameter
const person3 = {
    name: 'John',
    age: 30,
    greet() {
        console.log('Hello, my name is ' + this.name + ' and I am ' + this.age + ' years old.')
    }
};
person3.greet()



// example 5: using `call` method
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



// example 6: using `apply` method
const obj1 = {
    firstName: 'First_name',
    lastName: 'Last_name'
};
const obj2 = {
    firstName: 'Mihir',
    lastName: 'Patel'
};
function printName(profession, country) {
    console.log(this.firstName + ' ' + this.lastName + ' ' + profession + ' ' + country);
}
printName.apply(obj2, ['Developer', 'Canada'])




// example 7: simple calling function
const age = 22;
function verifyAge () {
    return this.age;
}
console.log(verifyAge())


// example 8: invoking specific function
const obj3 = {
    firstName: 'First_name',
    lastName: 'Last_name'
};
const obj4 = {
    firstName: 'First_name',
    lastName: 'Last_name'
};
function printName() {
    console.log(this.firstName + ' ' + this.lastName);
}
printName.call(obj3)



// example 9: invoke a function with passing parameter
const obj5 = {
    firstName: 'First_name',
    lastName: 'Last_name'
};
const obj6 = {
    firstName: 'Mihir',
    lastName: 'Patel'
};
function printName(profession, country) {
    console.log(this.firstName + ' ' + this.lastName + ' ' + profession + ' ' + country);
}
printName.call(obj6, 'Developer', 'Canada')



// example 10: invoke a function inside object with parameter using call
let employee = {
    details: function (designation, experience) {
        return this.name
            + ' '
            + this.id
            + designation
            + experience
    }
}
let emp1 = {
    name: "A",
    id: 123
}
let emp2 = {
    name: "B",
    id: 456
}
let x = employee.details.call(emp2, "Manager", "4 years")
console.log(x)
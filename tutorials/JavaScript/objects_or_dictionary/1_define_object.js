// We can initialize any objects using followings:

// using object literals
// using `new Object()` method
// using `Object.create()` method
// using `constructor functions`


// example: using object literals
let person = {
    name: 'Sarah',
    age: 20,
    gender: 'female'
};
console.log(person);
console.log(person.name + ' is a ' + person.age + ' year old ' + person.gender);
console.log(person.name + ' is a ' + person.age + ' year old ' + person['gender']);

// example: using `new Object()` method
let Person = new Object();
Person.name = 'Sarah';
Person['age'] = 20;
Person.gender = 'female';

console.log(Person);
console.log(Person.name + ' is a ' + Person.age + ' year old ' + Person.gender);
console.log(Person.name + ' is a ' + Person.age + ' year old ' + Person['gender']);

// example: using `Object.create()` method
let Person = Object.create({});
Person.name = 'Sarah';
Person['age'] = 20;
Person.gender = 'female';

console.log(Person);
console.log(Person.name + ' is a ' + Person.age + ' year old ' + Person.gender);
console.log(Person.name + ' is a ' + Person.age + ' year old ' + Person['gender']);


// example: using `constructor functions`
function Person(name, age, gender) {
    this.name = name;
    this.age = age;
    this.gender = gender;
}
let personOne = new Person('Sarah', 20, 'gender')
console.log(personOne);
console.log(personOne.name + ' is a ' + personOne.age + ' years old ' + personOne.gender);
console.log(personOne.name + ' is a ' + personOne.age + ' year old ' + personOne['gender']);
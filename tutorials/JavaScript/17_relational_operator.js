// in
let car = {
    make: 'Toyota',
    model: 'Camry',
    year: 2022
}

let hasMake = 'make' in car;
let hasColor = 'color' in car;

console.log('Has make property:', hasMake); // output: true
console.log('Has color property:', hasColor); // output: false

// instanceof
function Car(make, model, year) {
    this.make = make;
    this.model = model;
    this.year = year;
}

let myCar = new Car('Toyota', 'Camry', 2022);
let isCarInstance = myCar instanceof Car;
console.log('Is myCar an instance of Car?', isCarInstance); // output: true
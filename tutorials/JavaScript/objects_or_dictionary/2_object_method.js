// object methods in JavaScript can be accessed by using functions

// example 1: invoking object's method using parenthesis
// example 2: invoking object's method without parenthesis
// example 3: invoking object's method using parenthesis and extra details



// example 1: invoking object's method using parenthesis
let student = {
    firstName: 'Mihir',
    lastName: 'Patel',
    education: 'computer engineering',
    section: 'A',

    studentDetails: function () {
        return this.firstName + ' ' + this.lastName + ' ' + this.class + ' ' + this.section;
    }
};
console.log(student.studentDetails())   // Mihir Patel computer engineering A



// example 2: invoking object's method without parenthesis
let student = {
    firstName: 'Mihir',
    lastName: 'Patel',
    education: 'computer engineering',
    section: 'A',

    studentDetails: function () {
        return this.firstName + ' ' + this.lastName + ' ' + this.class + ' ' + this.section;
    }
};
console.log(student.studentDetails) // [Function: studentDetails]



// example 3: invoking object's method using parenthesis and extra details
let student = {
    firstName: 'Mihir',
    lastName: 'Patel',
    education: 'computer engineering',
    section: 'A',

    studentDetails: function () {
        return this.firstName + ' ' + this.lastName + ' ' + this.class + ' ' + this.section;
    }
};
console.log('STUDENT ' + student.studentDetails())
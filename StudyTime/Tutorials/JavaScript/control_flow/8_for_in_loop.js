// syntax
// for (let i in obj1) {
//     // prints all the keys in
//     // obj1 on the console
//     console.log(i)
// }


// example 1
const array = [1,2,3,4,5];
for (const value in array) {
    console.log(array[value])
}



// example 2
const courses = {
    firstCouse: "C++ STL",
    secondCourse: "DSA ML",
    thirdCourse: "CS Core"
};
const student1 = Object.create(courses);
student1.id = 123;
student1.firstName = "John";
student1.showEnrolledCourses = function () {
    console.log(courses)
}

for (let prop in student1) {
    console.log(prop + " -> " + student1[prop])
}
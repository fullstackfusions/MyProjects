// syntax:
// for (statement 1; statement 2; statement 3) {
//     code here...
// }
// statement 1: initialization of counter i.e. x = 2
// statement 2: condition for executing the code block
// statement 3: increment and decrement of the counter


// example 1:
let x;
for (x = 2; x <= 4; x++) {
    console.log('Value of x:' + x)
}



// example 2:
let y = 2;
for (; y <= 4; y++) {
    console.log('Value of y:' + y)
}


// example 3:
let z = 2;
for (; ; z++) {
    console.log('Value of z:' + z)
}


// example 4:
const subjects = ['Maths', 'Science', 'Social Science', 'History'];
let i = 0;
let len = subjects.length;
let gfg = "";
for (; i< len;) {
    gfg += subjects[i];
    i++;
}
console.log(gfg)
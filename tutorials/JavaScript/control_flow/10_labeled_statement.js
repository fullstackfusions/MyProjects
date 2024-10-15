// syntax
// label: statement (could be loop or block of code)


// example 1
let sum = 0, a = 1
outerloop: while (true) {
    a = 1;
    innerloop: while (a < 3) {
        sum += a;
        if (sum > 12) {
            break outerloop
        }
        console.log("sum = " + sum);
        a++;
    }
}


// example 2
blockOfCode: {
    console.log("This part will be executed");
    break blockOfCode;
    console.log("This part will not be executed")
}
console.log("out of the block")


// example 3
myLabel: function myLabeledFunction() {
    console.log("This is a labeled function.")
}
myLabeledFunction();
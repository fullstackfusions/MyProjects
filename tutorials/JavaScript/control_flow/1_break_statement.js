// example 1 break in switch case
const fruit = 'Mango';

switch (fruit) {
    case 'Apple':
        console.log('Apple is healthy for our body');
        break;
    case 'Mango':
        console.log('Mango is a National fruit of India');
        break;
    default:
        console.log("I don't like fruits")
}


// example 2 break in for loop
for (let i = 1; i < 6; i++) {
    if (i == 4) break;
    console.log(i)
}


// example 3 break in while loop
let i = 1;
while (i<= 5) {
    console.log(i);
    if (i === 3) {
        break;
    }
    i++;
}


// example 4 break in do while loop
let j = 1;
do {
    console.log(j);
    if (j === 3) {
        break;
    }
    j++;
} while (j <= 5);
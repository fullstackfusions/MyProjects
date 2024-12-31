// example 1 continue in for loop
for (let i = 0; i < 11; i++) {
    if (i % 2 == 0) continue;
    console.log(i)
}


// example 2 continue in while loop
let i = 0;
while (i < 11) {
    i++;
    if (i % 2 == 0) continue;
    console.log(i)
}
function Language() {
    let first = 'HTML',
        second = 'CSS',
        third = 'JavaScript'
    return {
        first, second, third
    };
}
let { first, second, third } = Language();
console.log(first);
console.log(second);
console.log(third);
// The bitwise operators in javascript is used to convert the number to a 32-bit binary number and perform the bitwise operation, the number is converted back to the 64-bit number after the result

// bitwise and
a = 6
b = 1
console.log(a & b) // 0

// bitwise or
a = 6
b = 1
console.log(a | b) // 7

// bitwise xor
a = 6
b = 1
console.log(a ^ b) // 7

// bitwise not
a = 6
console.log(~a) // -7

// bitwise left shift
a = 6
b = 1
console.log(a << b) // 12

// bitwise right shift
// in this two operators are used where the first operand is the number and the second operand is the number of bits to shift to the right
a = 6
b = 1
console.log(a >> b) // 3

// zero fill right shift
// it is same as a bitwise right shift the only difference is that overflowing bits are discarded
a = 6
b = 1
console.log(a >>> b) // 3
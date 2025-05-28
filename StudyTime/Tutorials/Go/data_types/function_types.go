package main

import "fmt"

// BinOp is a function type that takes two ints.
type BinOp func(int, int) int

func function_types() {
	var op BinOp // nil
	op = func(a, b int) int { return a + b }
	fmt.Println("2 + 3 =", op(2, 3))
}

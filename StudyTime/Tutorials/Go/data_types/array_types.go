package main

import "fmt"

func array_types() {
	// Array Types
	var a [3]int // zero value: [0 0 0]
	b := [3]string{"Go", "Rust", "Python"}
	fmt.Println("a:", a)
	fmt.Println("b:", b)
}

package main

import "fmt"

func pointer_types() {
	// Pointer Types
	x := 42
	var p *int // nil
	fmt.Println("nil p:", p)

	p = &x
	fmt.Println("addr of x:", p)
	fmt.Println("value at p:", *p)

	*p = 100 // modify x via p
	fmt.Println("x after:", x)
}

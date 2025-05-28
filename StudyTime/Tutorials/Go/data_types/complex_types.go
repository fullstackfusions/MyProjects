package main

import "fmt"

func complex_types() {
	// Complex Numbers
	c1 := complex(2, 3)     // complex128
	c2 := complex64(1 + 2i) // complex64
	fmt.Println("c1:", c1, "c2:", c2)
}

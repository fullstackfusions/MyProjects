package main

import "fmt"

func string_types() {
	// String Types
	s := "Hello, 世界"
	fmt.Println(s)
	fmt.Println("length in bytes:", len(s))
	for i, r := range s {
		fmt.Printf("rune %U at byte pos %d\n", r, i)
	}
}

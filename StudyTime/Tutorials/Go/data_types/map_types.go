package main

import "fmt"

func map_types() {
	// Map Types
	m := map[string]int{
		"apple":  5,
		"banana": 3,
	}
	m["cherry"] = 7
	fmt.Println("banana:", m["banana"])

	delete(m, "apple")
	fmt.Println("after delete:", m)
}

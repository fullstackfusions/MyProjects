package main

import "fmt"

func main() {

	// you can define similar to python
	var a = "initial"
	fmt.Println(a)

	// multi variable definition
	// here b and c both are considered as int
	var b, c int = 1, 2 // -> similar to var b int, c int = 1, 2
	fmt.Println(b, c)

	// boolean value definition
	var d = true
	fmt.Println(d)

	// just initialization of variable
	var e int
	fmt.Println(e)

	// most used approach to define variable, don't need to define the type
	f := "apple" // variable f will always expect string value
	fmt.Println(f)
}

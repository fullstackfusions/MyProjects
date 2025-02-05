package main

import "fmt"

func main() {

	i := 1 // now i will always expect int value
	for i <= 3 {
		fmt.Println(i)
		i = i + 1
	}

	for j := 0; j < 3; j++ {
		fmt.Println(j)
	}

	// range in for loop , here range is built-in method
	for i := range 3 {
		fmt.Println("range", i)
	}

	// unique for loop
	for {
		fmt.Println("loop")
		break
	}

	// for loop with continue statement
	for n := range 6 {
		if n%2 == 0 {
			continue
		}
		fmt.Println(n)
	}
}

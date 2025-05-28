package main

import "fmt"

func boolean() {
	var flag bool
	fmt.Println("zero value:", flag) // false

	flag = (2+2 == 4)
	fmt.Println("2+2==4?", flag) // true
}

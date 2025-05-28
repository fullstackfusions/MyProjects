package main

import "fmt"

// User is an example struct.
type User struct {
	ID   int
	Name string
	Age  int
}

func struct_types() {
	u := User{ID: 1, Name: "Alice", Age: 30}
	fmt.Printf("User: %+v\n", u)
}

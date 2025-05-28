package main

import "fmt"

// Stringer defines a String() method.
type Stringer interface {
	String() string
}

// Point implements Stringer.
type Point struct{ X, Y int }

func (p Point) String() string {
	return fmt.Sprintf("(%d, %d)", p.X, p.Y)
}

func interface_types() {
	var s Stringer = Point{3, 4}
	fmt.Println("Point:", s.String())
}

package main

import "fmt"

func main() {

	fmt.Println("go" + "lang")

	fmt.Println("1+1 =", 1+1)
	fmt.Println("7.0/3.0 =", 7.0/3.0)

	fmt.Println(true && false)
	fmt.Println(true || false)
	fmt.Println(!true)
}

// go default data types:
// bool
// string
// int
// uint32
// byte
// rune
// float64
// complex128

// It has some basic data types which is more for memory and performance optimization
// bool
// string
// int int8 int16 int32 int64
// uint uint8 uint16 uint32 uint64 uintptr
// byte alias for uint8
// rune alias for int32 represents a unicode point
// float32 float64
// complex64 complex128

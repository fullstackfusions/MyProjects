// ## Numeric Types

// ### Unsigned Integers (`uint*`)

// * `uint8`: 0…255 (alias `byte`)
// * `uint16`: 0…65535
// * `uint32`: 0…4 294 967 295
// * `uint64`: 0…18 446 744 073 709 551 615
package main

import "fmt"

func numeric1() {
	var i8 int8 = -128
	var i16 int16 = 32767
	var r rune = '世' // rune is alias for int32

	var b byte = 255 // byte is alias for uint8
	var u16 uint16 = 50000
	var u32 uint32 = 1 << 30
	var u64 uint64 = 1e18 // 1e18 is a float constant but fits into uint64

	fmt.Printf("i8: %d\n", i8)
	fmt.Printf("i16: %d\n", i16)
	fmt.Printf("rune for 世: %U\n\n", r)

	fmt.Printf("b   (byte):    %d\n", b)
	fmt.Printf("u16 (uint16):  %d\n", u16)
	fmt.Printf("u32 (uint32):  %d\n", u32)
	fmt.Printf("u64 (uint64):  %d\n", u64)
}

// ### Signed Integers (`int*`)

// * `int8`: –128…127
// * `int16`: –32768…32767
// * `int32`: –2 147 483 648…2 147 483 647 (alias `rune`)
// * `int64`: –9 223 372 036 854 775 808…9 223 372 036 854 775 807

func numeric2() {
	var i8 int8 = -128
	var i16 int16 = 32767
	var r rune = '世' // rune is alias for int32

	fmt.Printf("i8: %d, i16: %d\n", i8, i16)
	fmt.Printf("rune for 世: %U\n", r)
}

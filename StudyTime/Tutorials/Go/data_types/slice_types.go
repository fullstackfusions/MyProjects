package main

import "fmt"

func slice_types() {
	// Slice Types
	nums := []int{10, 20, 30}
	nums = append(nums, 40)
	fmt.Println("nums:", nums)

	sub := nums[1:3] // elements at indices 1 and 2
	fmt.Println("sub-slice:", sub)
}

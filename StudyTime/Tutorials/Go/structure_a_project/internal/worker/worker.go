package worker

import (
	"fmt"
	"time"
)

// Run is the main entrypoint for your worker.
func Run() {
	fmt.Println("Worker starting…")

	// Simple example loop
	for i := 1; i <= 5; i++ {
		fmt.Printf("Processing task #%d\n", i)
		// simulate work
		time.Sleep(500 * time.Millisecond)
	}

	fmt.Println("Worker finished all tasks.")
}

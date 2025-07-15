package main

import (
	"fmt"
	"sync"
)

type Counter struct {
	mu    sync.Mutex
	value int
}

func (c *Counter) Increment() {
	c.mu.Lock()   // Acquire the lock
	c.value++     // Modify shared resource
	c.mu.Unlock() // Release the lock
}

func main() {
	counter := Counter{}
	var wg sync.WaitGroup

	// Launch 10 goroutines to increment the counter
	for i := 0; i < 10; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			counter.Increment()
		}()
	}

	wg.Wait()
	fmt.Println("Final counter value:", counter.value) // Should print 10
}

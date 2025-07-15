package main

import (
	"fmt"
	"sync"
	"time"
)

type SafeMap struct {
	mu   sync.RWMutex
	data map[string]int
}

func (sm *SafeMap) Set(key string, value int) {
	sm.mu.Lock() // Exclusive write lock
	sm.data[key] = value
	sm.mu.Unlock() // remember to unlock after writing
}

func (sm *SafeMap) Get(key string) (int, bool) {
	sm.mu.RLock() // Shared read lock
	defer sm.mu.RUnlock()
	value, exists := sm.data[key]
	return value, exists
}

func main() {
	sm := SafeMap{data: make(map[string]int)}
	var wg sync.WaitGroup

	// Writer goroutine
	wg.Add(1)
	go func() {
		defer wg.Done()
		sm.Set("key1", 42)
	}()

	// Multiple reader goroutines
	for i := 0; i < 5; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			time.Sleep(10 * time.Millisecond) // Simulate work
			value, exists := sm.Get("key1")
			if exists {
				fmt.Printf("Read value: %d\n", value)
			}
		}()
	}

	wg.Wait()
}

package main

import "fmt"

func channel_types() {
	// Channel Types
	ch := make(chan string)

	go func() {
		ch <- "ping"
	}()

	msg := <-ch
	fmt.Println("received:", msg)
	close(ch)
}

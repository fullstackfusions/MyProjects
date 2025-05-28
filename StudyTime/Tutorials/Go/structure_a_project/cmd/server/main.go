package main

import "github.com/yourname/myapp/internal/server"

func main() {
	server.Start()
}

// to buiild the server module, run the following command in the terminal:
// go build -o bin/server ./cmd/server

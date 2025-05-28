package main

import (
	"github.com/yourname/myapp/internal/db"
	"github.com/yourname/myapp/internal/worker"
)

func main() {
	if err := db.Connect(); err != nil {
		panic(err)
	}
	worker.Run()
}

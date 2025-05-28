package server

import "github.com/yourname/myapp/internal/db"

func Start() {
	db.Connect()
	// ...
}

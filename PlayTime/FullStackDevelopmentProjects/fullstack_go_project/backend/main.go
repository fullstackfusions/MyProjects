package main

import (
	"fmt"
	"log"
	"net/http"
)

// CORS Middleware
func enableCORS(w http.ResponseWriter) {
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Header().Set("Access-Control-Allow-Methods", "GET, OPTIONS")
	w.Header().Set("Access-Control-Allow-Headers", "Content-Type")
}

// Greeting Handler
func greetHandler(w http.ResponseWriter, r *http.Request) {
	enableCORS(w)

	// Log request details
	log.Printf("Received request: %s %s", r.Method, r.URL.Path)

	// Handle OPTIONS request (preflight)
	if r.Method == "OPTIONS" {
		w.WriteHeader(http.StatusOK)
		return
	}

	name := r.URL.Query().Get("name")
	if name == "" {
		name = "World"
	}
	response := fmt.Sprintf("Hello, %s!", name)
	log.Printf("Response: %s", response)
	fmt.Fprint(w, response)
}

// Welcome Handler (Fix for 404)
func welcomeHandler(w http.ResponseWriter, r *http.Request) {
	enableCORS(w)
	log.Printf("Received request: %s %s", r.Method, r.URL.Path)
	fmt.Fprint(w, "Welcome to the Go Backend!")
}

func main() {
	http.HandleFunc("/", welcomeHandler) // Serves "/" instead of 404
	http.HandleFunc("/greet", greetHandler)

	log.Println("Server starting on port 8080...")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

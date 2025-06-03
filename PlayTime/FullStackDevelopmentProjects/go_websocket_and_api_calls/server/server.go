// server.go

// go get github.com/gorilla/websocket

package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"time"

	"github.com/gorilla/websocket"
)

// ─── 1) Define a shared schema (similar to your Pydantic TextResponse) ───────────
type TextResponse struct {
	Message   string  `json:"message"`
	Timestamp float64 `json:"timestamp"`
}

// ─── 2) Set up a Gorilla upgrader ────────────────────────────────────────────────
//
//	This handles the HTTP→WebSocket handshake.
var upgrader = websocket.Upgrader{
	ReadBufferSize:  1024,
	WriteBufferSize: 1024,
	// For dev/testing, allow any origin—lock this down in production.
	CheckOrigin: func(r *http.Request) bool { return true },
}

// ─── 3) WebSocket handler ───────────────────────────────────────────────────────
func wsHandler(w http.ResponseWriter, r *http.Request) {
	// 3.1) Upgrade the HTTP connection to a WebSocket
	conn, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		http.Error(w, "Failed to upgrade to WebSocket", http.StatusBadRequest)
		return
	}
	defer conn.Close()

	// 3.2) Simple echo loop: read a JSON text, send back TextResponse
	for {
		var incoming struct {
			Message string `json:"message"`
		}

		if err := conn.ReadJSON(&incoming); err != nil {
			// Client closed connection or sent invalid JSON
			fmt.Println("WebSocket read error:", err)
			return
		}

		// Build a TextResponse (JSON)
		resp := TextResponse{
			Message:   "Echo: " + incoming.Message,
			Timestamp: float64(time.Now().UnixNano()) / 1e9,
		}

		// Send JSON back over WebSocket
		if err := conn.WriteJSON(resp); err != nil {
			fmt.Println("WebSocket write error:", err)
			return
		}
	}
}

// ─── 4) HTTP fallback handler ────────────────────────────────────────────────────
func httpFallbackHandler(w http.ResponseWriter, r *http.Request) {
	// Expect: POST with JSON e.g. {"message": "hello"}
	if r.Method != http.MethodPost {
		http.Error(w, "Only POST allowed", http.StatusMethodNotAllowed)
		return
	}

	var payload struct {
		Message string `json:"message"`
	}

	decoder := json.NewDecoder(r.Body)
	if err := decoder.Decode(&payload); err != nil {
		http.Error(w, "Invalid JSON payload", http.StatusBadRequest)
		return
	}

	// Build the same TextResponse
	resp := TextResponse{
		Message:   "Fallback echo: " + payload.Message,
		Timestamp: float64(time.Now().UnixNano()) / 1e9,
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(resp)
}

// ─── 5) Set up HTTP routes and start server ─────────────────────────────────────
func main() {
	http.HandleFunc("/ws", wsHandler)
	http.HandleFunc("/api/fallback", httpFallbackHandler)

	addr := ":8000"
	fmt.Println("Server listening on", addr)
	if err := http.ListenAndServe(addr, nil); err != nil {
		panic(err)
	}
}

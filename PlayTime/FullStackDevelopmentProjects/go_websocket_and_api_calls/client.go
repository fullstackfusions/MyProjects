// client.go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"

	"github.com/gorilla/websocket"
)

// ─── 1) Reuse TextResponse struct ──────────────────────────────────────────────
type TextResponse struct {
	Message   string  `json:"message"`
	Timestamp float64 `json:"timestamp"`
}

// ─── 2) A simple client that tries WS first ────────────────────────────────────
func main() {
	wsURL := "ws://localhost:8000/ws"
	httpURL := "http://localhost:8000/api/fallback"

	// 2.1) Attempt WebSocket connection
	conn, _, err := websocket.DefaultDialer.Dial(wsURL, nil)
	if err != nil {
		fmt.Println("⚠️  WebSocket failed:", err)
		doHTTPFallback(httpURL, "Hello via HTTP")
		return
	}
	defer conn.Close()
	fmt.Println("✅ WebSocket connected")

	// 2.2) Send a JSON message over WS
	request := map[string]string{"message": "Hello over WS"}
	if err := conn.WriteJSON(request); err != nil {
		fmt.Println("WebSocket write error:", err)
		conn.Close()
		doHTTPFallback(httpURL, "Hello via HTTP after WS failed")
		return
	}

	// 2.3) Read a JSON response into TextResponse
	var resp TextResponse
	if err := conn.ReadJSON(&resp); err != nil {
		fmt.Println("WebSocket read error:", err)
		conn.Close()
		doHTTPFallback(httpURL, "Hello via HTTP since WS read failed")
		return
	}

	fmt.Printf("⬅️  Received via WS: %+v\n", resp)
}

// ─── 3) HTTP fallback helper ───────────────────────────────────────────────────
func doHTTPFallback(url, text string) {
	payload := map[string]string{"message": text}
	bodyBytes, _ := json.Marshal(payload)

	resp, err := http.Post(url, "application/json", bytes.NewBuffer(bodyBytes))
	if err != nil {
		fmt.Println("❌ HTTP POST failed:", err)
		return
	}
	defer resp.Body.Close()

	data, _ := ioutil.ReadAll(resp.Body)
	var parsed TextResponse
	if err := json.Unmarshal(data, &parsed); err != nil {
		fmt.Println("❌ JSON unmarshal failed:", err)
		return
	}

	fmt.Printf("⬅️  Received via HTTP fallback: %+v\n", parsed)
}

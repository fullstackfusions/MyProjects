import { useEffect, useState } from "react";

const WebSocketComponent = () => {
  const [messages, setMessages] = useState<string[]>([]);
  const [input, setInput] = useState("");
  const [ws, setWs] = useState<WebSocket | null>(null);

  useEffect(() => {
    const websocket = new WebSocket("ws://localhost:8000/ws");

    websocket.onopen = () => console.log("WebSocket Connected");
    websocket.onmessage = (event) => {
      console.log("Received from backend:", event.data);
      setMessages((prev) => [...prev, event.data]); // Add backend response
    };
    websocket.onerror = (error) => console.error("WebSocket Error:", error);
    websocket.onclose = () => console.log("WebSocket Disconnected");

    setWs(websocket);

    return () => {
      websocket.close();
    };
  }, []);

  const sendMessage = () => {
    if (ws && input) {
      const userMessage = `You: ${input}`; // Prefix to distinguish user messages
      setMessages((prev) => [...prev, userMessage]); // Add user message to UI
      ws.send(input); // Send to backend
      setInput(""); // Clear input field
    }
  };

  return (
    <div>
      <h1>WebSocket Chat</h1>
      <div>
        {messages.map((msg, index) => (
          <p key={index}>{msg}</p>
        ))}
      </div>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type a message"
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
};

export default WebSocketComponent;

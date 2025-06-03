// npm install --save-dev @types/react @types/react-dom

// src/components/InputComponent.tsx

import React, { useState, useCallback, useEffect, useRef } from "react";
import { Box, Button, TextField } from "@mui/material";
import SendIcon from "@mui/icons-material/Send";
import { Message } from "../hooks/interfaces"; // <-- adjust path if needed

interface InputComponentProps {
  addMessage: (msg: Message) => void;
}

const InputComponent: React.FC<InputComponentProps> = ({ addMessage }) => {
  const [input, setInput] = useState("");
  const [key, setKey] = useState(0);
  const [ws, setWs] = useState<WebSocket | null>(null);
  const wsRef = useRef<WebSocket | null>(null);

  // ─── WebSocket setup ─────────────────────────────────────────────────────────
  useEffect(() => {
    if (!wsRef.current) {
      const websocket = new WebSocket("ws://localhost:8000/ws/chat");
      wsRef.current = websocket;

      websocket.onopen = () => {
        console.log("WebSocket Connected");
        setWs(websocket);
      };

      websocket.onmessage = (event) => {
        try {
          const response = JSON.parse(event.data);
          addMessage({
            chatId: response.chatId || "ws_chat",
            user: response.user || { name: "Bot", email: "bot@test.com" },
            role: "bot",
            messageId: response.messageId || `ws_${new Date().getTime()}`,
            message: response.message || "",
            response: response.response || event.data,
            timestamp: Date.now(),
          });
        } catch (e) {
          console.error("Failed to parse WebSocket message:", e);
          addMessage({
            chatId: "system",
            user: { name: "System", email: "system@test.com" },
            role: "bot",
            messageId: `error_${new Date().getTime()}`,
            message: "",
            response: "Error processing WebSocket response",
            timestamp: Date.now(),
          });
        }
      };

      websocket.onerror = (error) => console.error("WebSocket Error:", error);

      websocket.onclose = () => {
        console.log("WebSocket Disconnected");
        setWs(null);
        wsRef.current = null;
      };
    }

    return () => {
      console.log("Cleaning up WebSocket");
      if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
        wsRef.current.close();
      }
    };
  }, [addMessage]);

  // ─── REST success / error handlers ────────────────────────────────────────────
  const handleSuccess = useCallback(
    (response: any) => {
      addMessage({
        chatId: response.chatId,
        user: response.user,
        role: "bot",
        messageId: response.messageId,
        message: response.message,
        response: response.response,
        timestamp: Date.now(),
      });
      setInput("");
    },
    [addMessage]
  );

  const handleError = useCallback(
    (error: Error | Response) => {
      let errorMessage =
        error instanceof TypeError
          ? `Error encountered: ${error.message}`
          : "Failed to send due to unexpected error";

      if (error instanceof Response) {
        if (error.status >= 400 && error.status < 500) {
          errorMessage =
            "Failed to send message: The request was not valid. Please check your input.";
        } else if (error.status >= 500) {
          errorMessage =
            "Failed to send message: Server Error. Please try again later.";
        }
      } else if (error instanceof Error) {
        console.error("Network or unexpected error:", error);
      }

      addMessage({
        chatId: "system",
        user: { name: "System", email: "system@test.com" },
        messageId: `error_${new Date().getTime()}`,
        role: "bot",
        message: "",
        response: errorMessage,
        timestamp: Date.now(),
      });
      setInput("");
    },
    [addMessage]
  );

  // ─── REST‐based sendMessage ──────────────────────────────────────────────────
  const sendMessageRest = useCallback(async () => {
    const payload: Message = {
      chatId: "Test-123",
      user: { name: "TestUser", email: "testuser@gmail.com" },
      role: "user",
      messageId: `msg_${new Date().getTime()}`,
      message: input,
      response: "",
      timestamp: Date.now(),
    };
    addMessage(payload);

    try {
      console.log("Sending via REST:", payload);
      const response = await fetch(`http://localhost:8000/message/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });
      if (!response.ok) throw response;
      const data = await response.json();
      handleSuccess(data);
    } catch (err) {
      console.error(err);
      handleError(err as Error | Response);
    }
  }, [input, handleSuccess, handleError, addMessage]);

  // ─── WebSocket‐based sendMessage ──────────────────────────────────────────────
  const sendMessageWs = useCallback(() => {
    if (ws && input.trim() && ws.readyState === WebSocket.OPEN) {
      const payload: Message = {
        chatId: "Test-123",
        user: { name: "TestUser", email: "testuser@gmail.com" },
        role: "user",
        messageId: `ws_${new Date().getTime()}`,
        message: input,
        response: "",
        timestamp: Date.now(),
      };
      ws.send(JSON.stringify(payload));
      console.log("Sent via WebSocket:", payload);
      addMessage(payload);
      setInput("");
    } else {
      console.error("WebSocket not connected or not ready");
    }
  }, [ws, input, addMessage]);

  const handleSubmit = () => {
    if (!input.trim()) return;
    setKey((prev) => prev + 1);
    // You can switch between WS or REST here:
    sendMessageWs();
    // If you want REST instead, comment out sendMessageWs() and uncomment:
    // sendMessageRest();
    setInput("");
  };

  // ─── RENDER ───────────────────────────────────────────────────────────────────
  return (
    <Box
      sx={{
        alignItems: "center",
        alignContent: "center",
        width: "100%",
        backgroundColor: "primary",
        display: "inline-flex",
      }}
    >
      <TextField
        key={key}
        id="user-input"
        fullWidth
        multiline
        maxRows={4}
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            handleSubmit();
          }
        }}
        placeholder="Type a message..."
      />
      <Button onClick={handleSubmit}>
        <SendIcon />
      </Button>
    </Box>
  );
};

export default InputComponent;

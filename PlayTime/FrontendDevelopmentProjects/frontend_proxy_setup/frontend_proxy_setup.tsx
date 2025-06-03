// vite.config.ts
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      // 1) Proxy all HTTP API calls under /api
      "/api": {
        target: "http://localhost:8000",
        changeOrigin: true,
        secure: false,
        // Example: frontend calls "/api/chat" → backend sees "/"
        // Example: frontend calls "/api/chat/foo" → backend sees "/foo"
        rewrite: (path) => path.replace(/^\/api\/chat/, ""),
      },

      // 2) Proxy WebSocket connections under /ws
      "/ws": {
        target: "ws://localhost:8000",
        ws: true,
        changeOrigin: true,
        secure: false,
        // Example: frontend opens "ws://localhost:3000/ws/chat" → backend sees "/"
        // Example: frontend opens "ws://localhost:3000/ws/chat/room1" → backend sees "/room1"
        rewrite: (path) => path.replace(/^\/ws\/chat/, ""),
      },
    },
  },
});

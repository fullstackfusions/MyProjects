### **Usage Instructions**
1. **Ensure you have Docker and Docker Compose installed.**
2. **Create necessary files** in the same directory:
   - `Dockerfile`
   - `docker-compose.yml`
   - `Caddyfile`
   - `index1.html` (HTML file for server 1)
   - `index2.html` (HTML file for server 2)
3. **Start all containers** by running:
   ```
   docker-compose up -d
   ```
4. **Test the load balancer** at:
   ```
   http://localhost:8080/
   ```
   or using curl:
   ```
   curl localhost:8080
   ```
   Each request should alternate responses between `caddy1` and `caddy2`.

---

This setup fully automates the creation of the network, the two application servers, and the Caddy load balancer.

First, we need to start some application servers so that we have something to load balance! We'll be using `Caddy`, an awesome open-source load balancer/web server. Nginx and Apache are other popular alternatives that do similar things, but Caddy is a modern version written in Go, so I think it will be cool to play with.

**pull the caddy image**
`docker pull caddy`

**Run Caddy Containers to Serve the HTML**
- Run a container for `index1.html` on port `8001`: docker run -p 8001:80 -v $PWD/index1.html:/usr/share/caddy/index.html caddy
- Run a container for `index2.html` on port `8002`: docker run -p 8002:80 -v $PWD/index2.html:/usr/share/caddy/index.html caddy


**result**
You can run them in separate terminal sessions, or you can run them in detached mode with -d, whichever you prefer.

Navigate to localhost:8001 in a browser. You should see "Hello from server 1". Next, navigate to localhost:8002 and hopefully, you'll see "Hello from server 2"!

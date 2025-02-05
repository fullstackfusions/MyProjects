- [Pull the Caddy image](#pull-the-caddy-image)
- [Custom network creation](#custom-network-creation)
- [Restart Your Application Servers on the Network](#restart-your-application-servers-on-the-network)
- [Contacting the Caddy Servers Through the Bridge](#contacting-the-caddy-servers-through-the-bridge)
- [Configuring the Load Balancer](#configuring-the-load-balancer)
- [Caddyfile for the Load Balancer](#caddyfile-for-the-load-balancer)
- [Run the Load Balancer](#run-the-load-balancer)



## Pull the Caddy image
`docker pull caddy`


## Custom network creation

Docker allows us to create custom bridge networks so that our containers can communicate with each other if we want them to, but remain otherwise isolated. We're going to build a system where the application servers are hidden within a custom network, and only our load balancer is exposed to the host.

Let's create a custom bridge network called "caddytest".

`docker network create caddytest`

You can see if it worked by listing all the networks:
`docker network ls`

## Restart Your Application Servers on the Network

Stop and restart your caddy application servers, but this time, make sure you attach them to the caddytest network and give them names:

> Run following commands in individual terminal if you don't want to start them in detached mode.

`docker run --network caddytest --name caddy1 -v $PWD/index1.html:/usr/share/caddy/index.html caddy`

`docker run --network caddytest --name caddy2 -v $PWD/index2.html:/usr/share/caddy/index.html caddy`

Note that we didn't expose any ports with -p because we don't need to do that anymore. Instead, we'll use the bridge network to communicate with these containers from another container.

## Contacting the Caddy Servers Through the Bridge

To make sure it's working, let's get a shell session inside a "getting started" container on the custom network:

> Run the following command in new terminal if you haven't started the container in detached mode.

`docker run -it --network caddytest docker/getting-started /bin/sh`

By giving our containers some names, caddy1 and caddy2, and providing a bridge network, Docker has set up name resolution for us! The container names resolve to the individual containers from all other containers on the network. Within your docker/getting-started container shell, curl the first container:

`curl caddy1`

And the second container:

`curl caddy2`

Note that if you need to restart your caddy application servers after naming them, you can use: `docker start caddy1` and `docker start caddy2`.


## Configuring the Load Balancer
We've confirmed that we have 2 application servers (Caddy) working properly on a custom bridge network. Let's create a load balancer that balances network requests between the two! We'll use a round-robin balancing strategy, so each request should route back and forth between the servers.

If you haven't yet, you can stop any containers that aren't the 2 caddy servers we're working on currently.

## Caddyfile for the Load Balancer

Caddy works great as a file server, which is what our little HTML servers are, but it also works great as a load balancer! To use Caddy as a load balancer we need to create a custom Caddyfile to tell Caddy how we want it to balance traffic.

Create a new file in your local directory called Caddyfile:

```
localhost:80

reverse_proxy caddy1:80 caddy2:80 {
	lb_policy       round_robin
}
```

This tells Caddy to run on localhost:80, and to round robin any incoming traffic to caddy1:80 and caddy2:80. Remember, this only works because we're going to run the loadbalancer within the same network, so caddy1 and caddy2 will automatically resolve to our application server's containers.

## Run the Load Balancer

Instead of providing an index.html to this Caddy server, we're going to give it our custom Caddyfile.

`docker run --network caddytest -p 8080:80 -v $PWD/Caddyfile:/etc/caddy/Caddyfile caddy`

Now you can hit the load balancer on `http://localhost:8080/`! You should either get a response from server 1 or server 2, and if you hard refresh the page, it will swap back and forth.

If it's not swapping properly, try using curl instead. Your browser might be caching the HTML.

`curl localhost:8080`

Each time you run curl, you should get a response from a different server!

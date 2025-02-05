- [Pull the Caddy image](#pull-the-caddy-image)
- [Custom network creation](#custom-network-creation)
- [Restart Your Application Servers on the Network](#restart-your-application-servers-on-the-network)
- [Contacting the Caddy Servers Through the Bridge](#contacting-the-caddy-servers-through-the-bridge)


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

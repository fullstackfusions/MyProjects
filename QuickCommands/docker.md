**it is similar to Podman but most users use this in their local test server and this also can be used for deployment in production best practice is use with Kubernetes for deployment**

> Note: sudo is only requires when you don't have normal permissions, you can try without sudo as well

```shell
sudo docker pull <image_name>:<version>     # to pull the specified image

sudo docker build -t <image-name>   # to build the image

sudo docker run -p <host_port>:<container_port> <image_name>:<version>  # to run normally without any external file attachment like env file

sudo docker run -d --env-file .env --name <container-name> -p 8501:8501 <image-name>    # to attach env file and export the port to access from web

sudo docker stop <container-name>   # to stop the running container

sudo docker rm <container-name>     # to remove container, first it requires to stop container

sudo docker rmi <image-name>    # to remove image, first it requires to remove the container

sudo docker images -a # to see all images

sudo docker container ls -a # to see all containers

sudo docker ps  # to see all the running containers

docker exec CONTAINER_ID <command> -ltnp  # allows to execute a command in a running container, i.e. netstat, ls

# Live Shell
docker exec -it CONTAINER_ID /bin/sh    # -i -> makes the exec command interactive, -t -> gives us a tty keyboard interface

# running multiple containers
docker run -d -p XX:80 docker/getting-started # In the -p XX:YY flag, the XX is the host port, while YY is the port within the container.
# XX -> can be replaced by different port e.g. 81, 82, 83
# for different port the containers will run to that port e.g http://localhost:81, http://localhost:82, http://localhost:83

# set some limitation like no network for containers. - best security practices
docker run -d --network none docker/getting-started # --network none -> will break the network access
# now if you will run ping google.com then it will not be able to access google.
docker exec CONTAINER_ID ping google.com -W 2

# Without network limitation
docker exec CONTAINER_ID ping google.com -W 2   # it will be able to access google.

docker network ls # You can see all the networks

```

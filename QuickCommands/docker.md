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
```

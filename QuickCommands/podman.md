## podman

**it is similar to Docker but most enterprises uses this in their production server**

> Note: sudo is only requires when you don't have normal permissions, you can try without sudo as well

```shell
sudo podman pull <image_name>:<version>     # to pull the specified image

sudo podman build -t <image-name>   # to build the image

sudo podman run -p <host_port>:<container_port> <image_name>:<version>  # to run normally without any external file attachment like env file

sudo podman build -t <image-name>   # to build the image

sudo podman run -d --env-file .env --name <container-name> -p 8501:8501 <image-name>    # to attach env file and export the port to access from web

sudo podman stop <container-name>   # to stop the running container

sudo podman rm <container-name>     # to remove container, first it requires to stop container

sudo podman rmi <image-name>    # to remove image, first it requires to remove the container

sudo podman images -a # to see all images

sudo podman container ls -a # to see all containers

sudo podman ps  # to see all the running containers
```

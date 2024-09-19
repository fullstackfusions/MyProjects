```bash

docker-compose build    # to build container

docker-compose build --no-cache # build container without any cached layers

docker-compose up   # builds and start container

docker-compose up --build   # builds and start contianer if there are changes made

docker-compose up -d    # builds and run container in detached mode

docker-compose stop  # to stop the container without removing them

docker-compose down # stop and remove container, network and volumes

docker-compose logs # display logs of each service

docker-compose logs [service_name]  # displays log for specific service name

docker-compose ps   # list status of all containers

docker-compose rm   # removes stopped containers

docker-compose rm -f    # force to remove stopped containers

docker-compose run [service_name] [command] # runs a one-time command in a new container based on the service configuration. i.e. docker-compose run app python manage.py migrate

```

### example of `docker-compose.yml`

```yml
version: "3.8"

# logic to hold common setups between any services
x-common-service: &common-service
  build:
    context: .
    dockerfile: Dockerfile
    args:
      # using this notation will search for .env file and
      # from there it will take USERNAME and PASSWORD
      # this way you don't need to explicitely pass username and password before env initialize in docker compose
      USERNAME: ${USERNAME}
      PASSWORD: ${PASSWORD}

services:
  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    container_name: zookeeper
    ports:
      - "2181:2181"
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000

  kafka:
    image: confluentinc/cp-kafka:latest
    container_name: kafka
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT
      KAFKA_INTER_BROKER_LISTENER_NAME: PLAINTEXT
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_AUTO_LEADER_REBALANCE_ENABLE: "true"
    depends_on:
      - zookeeper

  module-1:
    <<: *common-service
    # install debugpy first
    # debugpy helps to debug the docker containers in vscode
    # command: debugpy --listen 0.0.0.0:5676 --wait-for-client -m module-1
    command: module-1
    container_name: module-1-app
    ports:
      - "7272:7272"
    volumes:
      - ./:/app/
    depends_on:
      - kafka
    env_file:
      - .env
      - .env.module1

  module-2:
    <<: *common-service
    # command: debugpy --listen 0.0.0.0:5677 --wait-for-client -m module-2
    command: module-2
    container_name: module-2-app
    ports:
      - "7273:7273"
    volumes:
      - ./:/app/
    depends_on:
      - kafka
    env_file:
      - .env
      - .env.module2

  module-3:
    <<: *common-service
    # command: debugpy --listen 0.0.0.0:5678 --wait-for-client -m module-3
    command: module-3
    container_name: module-3-app
    ports:
      - "7274:7274"
    volumes:
      - ./:/app/
    depends_on:
      - kafka
    env_file:
      - .env
      - .env.module3
```

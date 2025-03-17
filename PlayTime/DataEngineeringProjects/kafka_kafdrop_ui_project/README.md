
### Step 1: Running Kafka Locally with Docker
Kafka requires a ZooKeeper instance for coordination, but the Confluent Kafka image can be paired with a ZooKeeper image easily. Here’s a simple Docker Compose setup to get both running locally:

1. **Create a `docker-compose.yml` file:**
   ```yaml
   version: '3'
   services:
     zookeeper:
       image: confluentinc/cp-zookeeper:latest
       environment:
         ZOOKEEPER_CLIENT_PORT: 2181
         ZOOKEEPER_TICK_TIME: 2000
       ports:
         - "2181:2181"

     kafka:
       image: confluentinc/cp-kafka:latest
       depends_on:
         - zookeeper
       ports:
         - "9092:9092"
       environment:
         KAFKA_BROKER_ID: 1
         KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
         KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
         KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT
         KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
   ```

2. **Run Docker Compose:**
   Open a terminal in the directory with your `docker-compose.yml` and run:
   ```
   docker-compose up -d
   ```
   This starts ZooKeeper and Kafka in the background. Kafka will be accessible at `localhost:9092`.

3. **Verify it’s running:**
   Check the logs with `docker-compose logs kafka` to ensure Kafka starts without errors. You should see something like "Kafka Server started."

### Step 2: Testing Kafka Accessibility
Before connecting another project, let’s ensure Kafka is working. You can use the built-in Kafka tools in the container to create a topic and test it.

1. **Access the Kafka container:**
   ```
   docker exec -it <kafka-container-name> bash
   ```
   (Find the container name with `docker ps`—it’ll be something like `<directory>_kafka_1`.)

2. **Create a topic:**
   Inside the container, run:
   ```
   kafka-topics --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
   ```

3. **List topics to confirm:**
   ```
   kafka-topics --list --bootstrap-server localhost:9092
   ```
   You should see `test-topic`.

### Step 3: Connecting a Local Project (Producer/Consumer)
Now, let’s set up a simple Python project using `confluent_kafka` to produce and consume messages from your local Kafka instance.

1. **Install the library:**
   Ensure you have the `confluent-kafka` Python package installed:
   ```
   pip install confluent-kafka
   ```

2. **Producer Example (`producer.py`):**
   ```python
   from confluent_kafka import Producer

   # Configuration for connecting to local Kafka
   conf = {
       'bootstrap.servers': 'localhost:9092'
   }

   # Create Producer instance
   producer = Producer(conf)

   # Delivery callback
   def delivery_report(err, msg):
       if err is not None:
           print(f'Message delivery failed: {err}')
       else:
           print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

   # Produce a message
   topic = 'test-topic'
   for i in range(5):
       producer.produce(topic, f'Hello, Kafka! {i}'.encode('utf-8'), callback=delivery_report)

   # Wait for any outstanding messages to be delivered
   producer.flush()
   ```

3. **Consumer Example (`consumer.py`):**
   ```python
   from confluent_kafka import Consumer

   # Configuration for connecting to local Kafka
   conf = {
       'bootstrap.servers': 'localhost:9092',
       'group.id': 'my-group',
       'auto.offset.reset': 'earliest'
   }

   # Create Consumer instance
   consumer = Consumer(conf)

   # Subscribe to topic
   topic = 'test-topic'
   consumer.subscribe([topic])

   # Consume messages
   try:
       while True:
           msg = consumer.poll(1.0)  # Timeout of 1 second
           if msg is None:
               continue
           if msg.error():
               print(f'Consumer error: {msg.error()}')
               continue
           print(f'Received message: {msg.value().decode("utf-8")}')
   except KeyboardInterrupt:
       consumer.close()
   ```

4. **Run the scripts:**
   - In one terminal, run the consumer: `python consumer.py`
   - In another terminal, run the producer: `python producer.py`

   The producer will send 5 messages, and the consumer should print them as they’re received.

### Key Points for Local Project Access
- **Kafka Address:** Your local project connects to Kafka at `localhost:9092` because that’s the advertised listener we set in the `docker-compose.yml`. If your other project runs on the same machine, this should work out of the box.
- **Topic Creation:** Ensure the topic your other project uses exists (create it as shown above if needed).
- **Network:** Since both Kafka and your project are local, no extra network config is needed. If your project runs in a Docker container, you’d need to adjust networking (e.g., use the same Docker network).

### Troubleshooting
- **Connection Issues:** If your project can’t connect, double-check `bootstrap.servers` is set to `localhost:9092` and that Kafka is running (`docker ps`).
- **Logs:** Check Kafka logs with `docker-compose logs kafka` for errors.
- **Port Conflict:** Ensure nothing else is using port 9092 or 2181.

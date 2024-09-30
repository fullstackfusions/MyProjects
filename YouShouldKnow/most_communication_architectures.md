A summary of the most used architectures with details on communication type, protocol, use case, strengths, and weaknesses:

---

### 1. **REST (Representational State Transfer)**

- **Communication Type**: Request-response
- **Protocol**: HTTP/1.1 or HTTP/2
- **Use Case**: Web APIs, CRUD operations, simple services
- **Strength**: Simplicity, stateless, wide adoption
- **Weakness**: Over-fetching/under-fetching, no native streaming
- **Example**:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def rest_api():
    return jsonify({'message': 'Hello, REST!'})

if __name__ == '__main__':
    app.run(debug=True)

```

> Run this script and visit http://127.0.0.1:5000/api to see the output.

---

### 2. **GraphQL**

- **Communication Type**: Request-response
- **Protocol**: HTTP, WebSocket
- **Use Case**: APIs where clients need specific data queries
- **Strength**: Flexibility, client-defined queries
- **Weakness**: Complex queries can cause performance issues
- **Example**:

```python
import graphene
from flask import Flask
from flask_graphql import GraphQLView

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="world"))

    def resolve_hello(self, info, name):
        return f'Hello {name}!'

schema = graphene.Schema(query=Query)

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)

```

> Run this script and go to http://127.0.0.1:5000/graphql to use GraphQL queries like:

```graphql
{
  hello(name: "GraphQL")
}
```

---

### 3. **SOAP (Simple Object Access Protocol)**

- **Communication Type**: Request-response, asynchronous messaging
- **Protocol**: HTTP, SMTP, TCP
- **Use Case**: Enterprise-grade applications, banking, government services
- **Strength**: Built-in security, transactional support
- **Weakness**: Verbose, complex, slower performance
- **Example**:

```python
from zeep import Client

wsdl = 'http://www.dneonline.com/calculator.asmx?WSDL'
client = Client(wsdl=wsdl)

result = client.service.Add(5, 3)
print(f"SOAP Add Result: {result}")

```

> This example uses a public WSDL for a calculator service.

---

### 4. **gRPC**

- **Communication Type**: Request-response, bi-directional streaming
- **Protocol**: HTTP/2
- **Use Case**: Microservices communication, low-latency services
- **Strength**: Efficient, supports multiple languages, streaming
- **Weakness**: Requires Protobuf, harder to debug
- **Example (Using grpcio)**:

_First, you need a `.proto` file, for example:_
`example.proto:`

```proto
syntax = "proto3";

service Greeter {
  rpc SayHello (HelloRequest) returns (HelloReply) {}
}

message HelloRequest {
  string name = 1;
}

message HelloReply {
  string message = 1;
}

```

_Generate the python code:_

```bash
python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. example.proto
```

_Now the python server_

```python
import grpc
from concurrent import futures
import example_pb2
import example_pb2_grpc

class Greeter(example_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return example_pb2.HelloReply(message=f'Hello, {request.name}')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

```

_Now the python client_

```python
import grpc
import example_pb2
import example_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = example_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(example_pb2.HelloRequest(name='gRPC'))
    print(f"gRPC Response: {response.message}")

if __name__ == '__main__':
    run()

```

---

### 5. **WebSocket**

- **Communication Type**: Full-duplex, bidirectional
- **Protocol**: TCP over HTTP
- **Use Case**: Real-time communication (e.g., chat apps, live updates)
- **Strength**: Low latency, continuous connection
- **Weakness**: Harder to scale horizontally, lacks formalized security
- **Example (Using websockets)**:

_Python Server_

```python
import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(f"Hello, {message}")

start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

```

_Python Server_

```python
import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("WebSocket")
        response = await websocket.recv()
        print(f"Response: {response}")

asyncio.get_event_loop().run_until_complete(hello())

```

---

### 6. **Kafka**

- **Communication Type**: Pub/Sub, streaming
- **Protocol**: TCP
- **Use Case**: Event streaming, log aggregation, data pipelines
- **Strength**: High throughput, scalability, fault tolerance
- **Weakness**: Not suitable for direct request-response interactions
- **Example (Using confluent-kafka-python)**:

_Python Producer_:

```python
from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

p.produce('my_topic', key='key', value='Hello Kafka!', callback=delivery_report)
p.flush()

```

_Python Consumer_:

```python
from confluent_kafka import Consumer

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['my_topic'])

while True:
    msg = c.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(f"Consumer error: {msg.error()}")
        continue

    print(f'Received message: {msg.value().decode("utf-8")')

c.close()

```

---

### 7. **AMQP (Advanced Message Queuing Protocol)**

- **Communication Type**: Pub/Sub, message queuing
- **Protocol**: TCP
- **Use Case**: Distributed systems, message brokering (RabbitMQ)
- **Strength**: Reliable messaging, decouples producers and consumers
- **Weakness**: Complex, may have performance overhead
- **Example (Using pika for RabbitMQ)**:

_Python Producer_:

```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello AMQP!')
print("Sent 'Hello AMQP!'")
connection.close()

```

_Python Consumer_:

```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(f"Received {body}")

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

```

---

### 8. **MQTT (Message Queuing Telemetry Transport)**

- **Communication Type**: Pub/Sub
- **Protocol**: TCP/IP
- **Use Case**: IoT devices, lightweight messaging
- **Strength**: Low overhead, ideal for low-bandwidth environments
- **Weakness**: Limited quality of service and message retention
- **Example (Using paho-mqtt)**:

_Python Publisher_:

```python
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)
client.publish("test/topic", "Hello MQTT!")
client.disconnect()

```

_Python Subscriber_:

```python
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"Received {msg.payload.decode()}")

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)
client.subscribe("test/topic")
client.on_message = on_message
client.loop_forever()

```

---

### 9. **SMPP (Short Message Peer-to-Peer)**

- **Communication Type**: Asynchronous, transactional messaging
- **Protocol**: TCP
- **Use Case**: SMS message delivery
- **Strength**: Optimized for SMS delivery, high throughput
- **Weakness**: Limited to messaging use cases, SMS-specific

---

### 10. **Thrift**

- **Communication Type**: RPC (Remote Procedure Call)
- **Protocol**: TCP, HTTP
- **Use Case**: Cross-language microservices communication
- **Strength**: Multi-language support, efficient serialization
- **Weakness**: Complex setup, binary protocol harder to debug

---

### 11. **XMPP (Extensible Messaging and Presence Protocol)**

- **Communication Type**: Messaging, real-time communication
- **Protocol**: TCP
- **Use Case**: Chat apps, presence notification (e.g., Google Talk)
- **Strength**: Decentralized, open standard, extensible
- **Weakness**: Overhead in setting up, not optimized for high-scale apps

---

### 12. **CoAP (Constrained Application Protocol)**

- **Communication Type**: Request-response
- **Protocol**: UDP
- **Use Case**: IoT and constrained devices
- **Strength**: Lightweight, suitable for low-power devices
- **Weakness**: Limited reliability (UDP-based), simpler than HTTP

---

### 13. **DDS (Data Distribution Service)**

- **Communication Type**: Pub/Sub
- **Protocol**: TCP, UDP
- **Use Case**: Real-time data systems, robotics, autonomous vehicles
- **Strength**: Real-time communication, fault tolerance
- **Weakness**: Complex setup, not widely adopted

---

### 14. **ZeroMQ**

- **Communication Type**: Messaging, Pub/Sub
- **Protocol**: TCP, IPC
- **Use Case**: Distributed messaging across processes or systems
- **Strength**: Lightweight, fast
- **Weakness**: Lacks built-in message persistence or broker capabilities

---

### 15. **Protobuf (Protocol Buffers)**

- **Communication Type**: Serialization format (used in gRPC, Thrift)
- **Protocol**: TCP
- **Use Case**: Data serialization in microservices
- **Strength**: Efficient, compact binary format
- **Weakness**: Requires schema management, harder to debug

---

### 16. **Avro**

- **Communication Type**: Data serialization
- **Protocol**: Typically TCP
- **Use Case**: Big data, Hadoop, message serialization
- **Strength**: Dynamic typing, schema evolution
- **Weakness**: Slightly slower than Protobuf

---

### 17. **SSE (Server-Sent Events)**

- **Communication Type**: Unidirectional streaming
- **Protocol**: HTTP
- **Use Case**: Continuous updates from server to client
- **Strength**: Simple, supports automatic reconnection
- **Weakness**: Only unidirectional, less efficient than WebSockets
- **Example (Using Flask-SSE)**:

_Server Flask SSE_:

```python
from flask import Flask, jsonify
from flask_sse import sse

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')

@app.route("/send")
def send_message():
    sse.publish({"message": "Hello SSE!"}, type='greeting')
    return jsonify({"status": "Message sent!"})

if __name__ == '__main__':
    app.run()

```

_Python Client_:

```python
<script>
  const evtSource = new EventSource("/stream");
  evtSource.onmessage = function(event) {
    console.log(event.data);
  };
</script>

```

---

### 18. **STOMP (Simple/Streaming Text Oriented Messaging Protocol)**

- **Communication Type**: Messaging
- **Protocol**: TCP
- **Use Case**: Lightweight messaging in brokers (ActiveMQ)
- **Strength**: Simple text-based protocol
- **Weakness**: Less efficient for large-scale systems

---

### 19. **Nanomsg**

- **Communication Type**: Messaging, Pub/Sub
- **Protocol**: TCP, IPC
- **Use Case**: High-performance messaging between processes
- **Strength**: Scalability, supports various messaging patterns
- **Weakness**: Still in development, not widely used

---

### 20. **ØMQ (ZeroMQ)**

- **Communication Type**: Messaging
- **Protocol**: TCP, IPC
- **Use Case**: Distributed messaging and multi-process communication
- **Strength**: High performance, flexibility
- **Weakness**: Lacks built-in reliability, requires custom setup

---

### 21. **TIBCO EMS (Enterprise Messaging Service)**

- **Communication Type**: Message queuing, Pub/Sub
- **Protocol**: TCP
- **Use Case**: Enterprise-level messaging and integration
- **Strength**: High throughput, reliability
- **Weakness**: Expensive, requires complex setup

---

### 22. **JMS (Java Message Service)**

- **Communication Type**: Messaging, Pub/Sub
- **Protocol**: TCP
- **Use Case**: Java enterprise messaging systems
- **Strength**: Reliable messaging in Java applications
- **Weakness**: Limited to Java ecosystem

---

### 23. **HTTP/2**

- **Communication Type**: Request-response, multiplexing
- **Protocol**: TCP
- **Use Case**: Web communication, APIs
- **Strength**: Multiplexing, header compression, faster than HTTP/1.1
- **Weakness**: Complex protocol, harder to debug

---

### 24. **QUIC**

- **Communication Type**: Request-response, multiplexing
- **Protocol**: UDP-based
- **Use Case**: Web performance optimization (used in HTTP/3)
- **Strength**: Fast, reduced latency
- **Weakness**: Not yet as widely adopted

---

### 25. **ICE (Interactive Connectivity Establishment)**

- **Communication Type**: Peer-to-peer communication
- **Protocol**: UDP, TCP
- **Use Case**: WebRTC, VoIP
- **Strength**: NAT traversal, real-time communication
- **Weakness**: Complex setup

---

### 26. **LwM2M (Lightweight Machine to Machine protocol)**

- **Communication Type**: Client-server
- **Protocol**: UDP, CoAP
- **Use Case**: IoT device management
- **Strength**: Optimized for constrained devices
- **Weakness**: Limited to IoT environments

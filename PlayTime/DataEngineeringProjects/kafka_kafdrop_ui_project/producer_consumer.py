"""

producer and consumer of kafka can have their individual script as it is supposed to perform individually

Here's a detailed breakdown of each configuration option:

1. logger
- Description: This refers to a logger object used to capture logs and messages for debugging or monitoring purposes.
- Purpose: It's essential for tracking what happens when the Kafka producer connects to the broker, sends messages, or encounters errors. The logger logs the Kafka client activities.

2. bootstrap.servers
- Description: Specifies the Kafka broker(s) that the producer connects to. It can be a comma-separated list of broker addresses, with the format host:port.
- Purpose: This tells the Kafka producer where to send messages. In this case, the broker is running on localhost on port 9092, which is Kafka's default port.

3. sasl.mechanisms
- Description: Defines the SASL (Simple Authentication and Security Layer) mechanism used to authenticate clients. In this case, the value is 'PLAIN'.
- Purpose: This indicates that PLAIN authentication is used. The PLAIN mechanism sends the username and password in plain text (but over a secure channel if SSL is used, as in this case).
- Common Values:
    - PLAIN: Basic username/password authentication.
    - GSSAPI: Used for Kerberos authentication.
    - SCRAM-SHA-256, SCRAM-SHA-512: More secure username/password mechanisms with hashing.

4. security.protocol
- Description: Specifies the security protocol used for communication between the Kafka producer and broker. In this case, it's 'SASL_SSL'.
- Purpose: This ensures that the communication is both encrypted (using SSL) and authenticated (using SASL).
- Common Values:
    - PLAINTEXT: No encryption or authentication.
    - SSL: Encryption using SSL.
    - SASL_PLAINTEXT: Authentication using SASL, but no encryption.
    - SASL_SSL: Both SASL authentication and SSL encryption.

5. sasl.kerberos.service.name
- Description: Defines the Kerberos service principal name for Kafka, which is typically set to 'kafka'.
- Purpose: When using Kerberos authentication, this identifies the service you are connecting to (Kafka in this case). Kerberos uses service principal names to authenticate services.
- Example: 'kafka' is the service name for the Kafka broker.

6. sasl.kerberos.principal
- Description: The Kerberos principal for the client that is attempting to authenticate. In this case, the client principal is 'service_id@yourdomain.com'.
- Purpose: This is the identity of the service or user (in this case, 'service_id') attempting to authenticate with Kerberos. The client principal typically follows the format service_id@REALM.
- Example: 'service_id@yourdomain.com' where service_id is the Kerberos principal name and yourdomain.com is the Kerberos realm.

7. sasl.kerberos.keytab
- Description: The path to the Kerberos keytab file that contains the service's encrypted credentials.
- Purpose: A keytab file is used to authenticate the client without having to manually enter a password. It's generated by Kerberos administrators using tools like ktutil and contains the service ID and its encrypted password.
- Example: 'service_id.keytab' is the file that the Kafka producer uses to authenticate with Kerberos.

8. (Commented Out) sasl.username
- Description: If using SASL PLAIN or SASL SCRAM mechanisms, this would be the username for authentication.
- Purpose: It would be used for simple username/password authentication, typically with cloud Kafka services or internal setups using basic authentication.
- Example: '<YOUR_API_KEY>' would be the username (or API key) for the service.

9. (Commented Out) sasl.password
- Description: The corresponding password or API secret for the sasl.username.
- Purpose: It would be used alongside the sasl.username to authenticate with the Kafka broker.
- Example: '<YOUR_API_SECRET>' would be the password or API secret used for authentication.


In this configuration, Kerberos is being used for authentication, which is indicated by the options sasl.kerberos.service.name, sasl.kerberos.principal, and sasl.kerberos.keytab. These options enable secure authentication using the Kerberos protocol over an encrypted SSL connection (security.protocol set to SASL_SSL).

However, the configuration also provides a commented-out alternative that uses PLAIN authentication (via sasl.username and sasl.password). This shows that the system is flexible and can switch between Kerberos-based authentication and simple username/password authentication by uncommenting those options if needed.

"""

# pip install confluent-kafka
import logging
import sys
import json
from confluent_kafka import Consumer, KafkaError, Producer, KafkaException

logger = logging.getLogger(__name__)

topic = "test-topic"    # You will have to create a topic, refer README.md step 2

# script for consumer
common_kafka_options = {
    'logger': logger,
    'bootstrap.servers': 'kafka:29092',
    # 'sasl.mechanisms': 'PLAIN',

    # Approach 1: Kerberos authentication over an encrypted SSL connection
    # 'security.protocol': 'SASL_SSL',
    # 'sasl.kerberos.service.name': 'kafka',
    # 'sasl.kerberos.principal': 'service_id@yourdomain.com',
    # 'sasl.kerberos.keytab': 'service_id.keytab', # this will be your ktutil keytab file, created using service id and password for your enterprise

    # Approach 2: Simple username/password authentication
    # 'sasl.username': '<YOUR_API_KEY>',
    # 'sasl.password': '<YOUR_API_SECRET>',
}
# Consumer setup with a unique group ID
consumer = Consumer({
    **common_kafka_options,
    'group.id': 'stock_price_group',
    'auto.offset.reset': 'latest',  # Start from the latest message
    'enable.auto.commit': False
})

# Subscribe to the Kafka topic
consumer.subscribe([topic])

# Producer setup
producer = Producer({**common_kafka_options})



# Produce the data
data = {"data": "Hello World!"}
print(f"selecting topic {topic}, {data}")
producer.produce(topic, json.dumps(data).encode('utf-8'))
producer.flush()
print(f"request sent to queue '{topic}'")


# Poll for new messages and print them
try:
    while True:
        msg = consumer.poll(1.0) # Adjust poll timeout as needed, usually we can keep 0

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                print(f'{msg.topic()} [{msg.partition()}] reached end at offset {msg.offset()}')
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            # Message is a normal message
            print(f'Received message: {msg.value().decode("utf-8")}')
finally:
    # Clean up on exit
    consumer.close()

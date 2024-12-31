"""

A singleton is a design pattern that restricts the instantiation of a class to one single instance. This is useful when exactly one object is needed to coordinate actions across the system. In Python, a singleton can be implemented in various ways.

Example use cases:
- database connections
- configuration settings
- logging purpose to keep track of single logger
- hardware interface access
- caching
- service providers
- kafka

"""

class KafkaHandler:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(KafkaHandler, cls).__new__(cls)
            # Initialize Kafka connection here
        return cls._instance

    # Kafka-related methods here

# Usage
kafka_handler = KafkaHandler()


# Another example:
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Usage
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Output: True
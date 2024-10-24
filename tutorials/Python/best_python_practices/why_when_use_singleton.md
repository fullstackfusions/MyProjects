```
The Problem:

I have one core class where I have a constructor of that class and inside it I am initializing multiple clients and then I am importing this class wherever I need any related clients initialized in core file.

now the problem is as many time I import this class it is taking times in multiplied factor.

For example if I import in one file that will instantiate it once and then if I import it in another file then it will also instantiate again and every time creating all the clients again I cannot afford wasting this time.

```

It sounds like you're facing an issue with redundant initializations due to multiple imports of a class that performs expensive operations (like client initializations) in its constructor. To avoid this, you can implement a pattern that ensures the class is only instantiated once, and the same instance is reused wherever needed. Here are two common approaches to solve this problem in Python:

## 1. Singleton Pattern

The Singleton pattern ensures that a class has only one instance and provides a global point of access to it. Here's a simple way to implement a Singleton in Python using a class decorator:

```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

class Singleton:
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Core:
    def __init__(self):
        # Initialize clients
        print("Clients initialized")

# Usage:
core1 = Core()  # Initializes clients
core2 = Core()  # Does not initialize again, reuses core1
```

or

```python
from typing import Any

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
class Singleton(object, metaclass=SingletonMeta):
    pass


class Core(Singleton):
    def __init__(self):
        # Initialize clients
        print("Clients initialized")

# Usage:
core1 = Core()  # Initializes clients
core2 = Core()  # Does not initialize again, reuses core1
```

## 2. Module-level Singleton

Python modules are singletons by nature because the module is only loaded once, and subsequent imports retrieve the already loaded module. You can take advantage of this by instantiating your class at the module level.

**core.py:**

```python
class Core:
    def __init__(self):
        # Initialize clients
        print("Clients initialized")

# Create a single instance of Core when the module is imported
core_instance = Core()
```

**usage.py:**

```python
from core import core_instance

# Use the pre-initialized 'core_instance'

# you could also do
from core import Core
core = Core()

# but this will also remain same as previous core_instance as this class is singleton
```

**another_usage.py:**

```python
from core import core_instance
# Same 'core_instance' is being used here

# you could also do
from core import Core
core = Core()

# but this will also remain same as previous core_instance as this class is singleton
```

## Choosing Between the Two

- **Singleton Pattern**: More explicit in its intent to restrict the class to a single instance. It is also more flexible if you need to manage the lifetime or creation parameters of the instance.
- **Module-level Singleton**: Simpler and leverages Python's module loading behavior. It's very straightforward but less flexible in terms of initialization parameters unless combined with other patterns (like factory methods).

For most cases where initialization overhead is a concern, the module-level singleton is sufficient and clean. However, if your use case requires that the singleton has potentially different initialization parameters or controlled re-instantiation, the explicit Singleton pattern would be more appropriate.


# This is used to preserve the original function’s metadata when applying a decorator.

from functools import wraps

def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("Calling the function...")
        return f(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    return f"Hello, {name}"

print(greet("Mihir"))  # Output: Calling the function... Hello, Mihir
print(greet.__name__)  # Output: greet (original function name preserved)

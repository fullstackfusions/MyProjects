from functools import partial, lru_cache, wraps

# Create a decorator that prints when the function is called
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with arguments: {args}")
        return func(*args, **kwargs)
    return wrapper

# Caching the results of the power function using lru_cache
@lru_cache(maxsize=100)
@log_execution  # Logs execution for demonstration
def power(base, exponent):
    return base ** exponent

# Create partial functions for square and cube
square = partial(power, exponent=2)
cube = partial(power, exponent=3)

# Main logic
if __name__ == "__main__":
    # Call square and cube functions
    print(square(4))  # Output: 16
    print(cube(3))    # Output: 27

    # Call square again to demonstrate caching
    print(square(4))  # Output (cached): 16
    print(cube(3))    # Output (cached): 27

    # Show cache information
    print(power.cache_info())  # Shows cache hits, misses, etc.

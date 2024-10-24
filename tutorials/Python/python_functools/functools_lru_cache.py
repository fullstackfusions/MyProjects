
# This is a decorator that provides memoization, caching the results of function calls.


from functools import lru_cache

@lru_cache(maxsize=55)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Output: 55
print(fibonacci.cache_info())  # Shows cache usage info

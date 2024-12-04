"""

This is useful when you want to apply a function asynchronously and collect the results later.

"""



import multiprocessing

# A function that multiplies two numbers
def multiply(a, b):
    return a * b

if __name__ == "__main__":
    data = [(1, 2), (3, 4), (5, 6)]
    results = []
    
    # Create a pool of workers
    with multiprocessing.Pool() as pool:
        # Apply the `multiply` function asynchronously to each tuple
        for pair in data:
            result = pool.apply_async(multiply, pair)
            results.append(result)
        
        # Retrieve the results
        output = [res.get() for res in results]
    
    print("Result from pool.apply_async():", output)

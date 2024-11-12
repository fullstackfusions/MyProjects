"""

In this script we are using pool.map(), but it allows passing multiple arguments to the function by unpacking tuples.

"""


import multiprocessing

# A function that adds two numbers
def add(a, b):
    return a + b

if __name__ == "__main__":
    data = [(1, 2), (3, 4), (5, 6)]
    
    # Create a pool of workers
    with multiprocessing.Pool() as pool:
        # Apply the `add` function to each tuple in `data` using pool.starmap()
        result = pool.starmap(add, data)
    
    print("Result from pool.starmap():", result)

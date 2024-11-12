"""

In this we are running parallel processes with the help of `pool.map` and here we are taking single argument for function.

"""

import multiprocessing

# A simple function to square a number
def square(num):
    return num * num

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    
    # Create a pool of workers
    with multiprocessing.Pool() as pool:
        # Apply the `square` function to each element in `data` using pool.map()
        result = pool.map(square, data)
    
    print("Result from pool.map():", result)

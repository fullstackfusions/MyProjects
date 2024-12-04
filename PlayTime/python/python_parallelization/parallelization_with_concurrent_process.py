"""

An alternative to multiprocessing.Pool is using concurrent.futures for parallelization.

"""



from concurrent.futures import ProcessPoolExecutor

# A function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    data = [5, 7, 10, 3]
    
    # Create a ProcessPoolExecutor
    with ProcessPoolExecutor() as executor:
        # Apply the `factorial` function to each element in `data`
        result = list(executor.map(factorial, data))
    
    print("Result from ProcessPoolExecutor:", result)

import concurrent.futures

# Define a simple function to be executed
def task(n):
    return n ** 2

# Create a ProcessPoolExecutor with maximum 2 worker processes
with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
    # Submit tasks to the executor
    results = [executor.submit(task, i) for i in range(5)]

    # Retrieve results as they become available
    for future in concurrent.futures.as_completed(results):
        result = future.result()
        print(result)
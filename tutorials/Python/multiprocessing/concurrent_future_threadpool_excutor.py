import concurrent.futures

# Define a simple function to be executed
def task(n):
    return n ** 2

# Create a ThreadPoolExecutor with maximum 2 worker threads
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    # Submit tasks to the executor
    results = [executor.submit(task, i) for i in range(5)]

    # Retrieve results as they become available
    for future in concurrent.futures.as_completed(results):
        result = future.result()
        print(result)
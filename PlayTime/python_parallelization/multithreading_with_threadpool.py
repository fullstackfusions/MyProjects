"""

This approach uses the ThreadPoolExecutor for managing a pool of threads and simplifies running multiple tasks in parallel. This approach higher-level API for thread management, ideal for executing multiple tasks concurrently.

Note: due to the Global Interpreter Lock (GIL) in CPython, only one thread can execute Python bytecode at a time, limiting true parallelism for CPU-bound tasks.

"""

from concurrent.futures import ThreadPoolExecutor
import time

# Function to simulate a task that takes time
def task(name, duration):
    print(f"Starting task {name}")
    time.sleep(duration)
    print(f"Task {name} finished after {duration} seconds")
    return name

if __name__ == "__main__":
    # Create a pool of threads
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks to the thread pool
        futures = [executor.submit(task, f"Task-{i}", i) for i in range(3)]
        
        # Process the results as they complete
        for future in futures:
            print(f"{future.result()} is complete.")

    print("All tasks completed.")

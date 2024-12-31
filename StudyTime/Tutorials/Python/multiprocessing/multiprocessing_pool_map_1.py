import multiprocessing

def worker_function(number):
    # Simulate some work
    result = number * 2
    print(f"Processed {number} and got result: {result}")

if __name__ == "__main__":
    # Define the number of processes you want to run
    num_processes = 4

    # Create a list of numbers to process
    numbers_to_process = [1, 2, 3, 4]

    # Create a multiprocessing Pool with the desired number of processes
    with multiprocessing.Pool(processes=num_processes) as pool:
        # Map the worker function to the list of numbers for parallel processing
        pool.map(worker_function, numbers_to_process)

    # All processes are completed at this point
    print("All processes have completed.")
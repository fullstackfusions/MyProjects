"""

This is the simplest approach, where you manually create and start threads for concurrent execution of a function. This approach manually creating and managing threads.

Note: due to the Global Interpreter Lock (GIL) in CPython, only one thread can execute Python bytecode at a time, limiting true parallelism for CPU-bound tasks.

"""

import threading
import time

# Function to simulate a task that takes time
def print_numbers():
    for i in range(5):
        print(f"Thread {threading.current_thread().name} - Number: {i}")
        time.sleep(1)

if __name__ == "__main__":
    # Create two threads
    thread1 = threading.Thread(target=print_numbers, name="Thread-1")
    thread2 = threading.Thread(target=print_numbers, name="Thread-2")
    
    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()
    
    print("Both threads finished execution.")

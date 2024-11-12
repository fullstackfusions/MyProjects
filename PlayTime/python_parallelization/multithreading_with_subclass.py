"""

This approach subclasses threading.Thread to encapsulate the thread's behavior in a class. This approach encapsulates threading functionality inside a custom class.

Note: due to the Global Interpreter Lock (GIL) in CPython, only one thread can execute Python bytecode at a time, limiting true parallelism for CPU-bound tasks.

"""

import threading
import time

# Subclassing threading.Thread
class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print(f"{self.name} starting")
        for i in range(5):
            print(f"{self.name} - Step {i}")
            time.sleep(1)
        print(f"{self.name} finished")

if __name__ == "__main__":
    # Creating instances of the custom thread class
    thread1 = MyThread("Worker-1")
    thread2 = MyThread("Worker-2")
    
    # Start both threads
    thread1.start()
    thread2.start()

    # Wait for both threads to complete
    thread1.join()
    thread2.join()
    
    print("Both custom threads finished execution.")

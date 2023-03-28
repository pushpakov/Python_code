import concurrent.futures
import logging
import time

# Function that will be run by the thread
def thread_function(name):
    logging.info("Thread %s: starting", name)  # Output message indicating the thread has started
    time.sleep(2)  # Wait for 2 seconds
    logging.info("Thread %s: finishing", name)  # Output message indicating the thread has finished


if __name__ == "__main__":
    # Configure the format of the logging messages and the level of the logging
    
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    
# Create a ThreadPoolExecutor with a maximum of 3 worker threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:

         # Execute the thread_function for each number in the range of 3
        executor.map(thread_function, range(3))





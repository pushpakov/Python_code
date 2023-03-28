# Importing necessary libraries
import logging
import threading
import time

# Function that will be run by the thread
def thread_function(name):
    logging.info("Thread %s: starting", name)  # Output message indicating the thread has started
    time.sleep(2)  # Wait for 2 seconds
    logging.info("Thread %s: finishing", name)  # Output message indicating the thread has finished

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")  # Setting up logging configuration

    logging.info("Main    : before creating thread")  # Output message indicating the main program is about to create a thread
    x = threading.Thread(target=thread_function, args=(1,))  # Creating a thread object
    logging.info("Main    : before running thread")  # Output message indicating the thread is about to start running
    x.start()  # Starting the thread
    logging.info("Main    : wait for the thread to finish")  # Output message indicating the main program is waiting for the thread to finish
    logging.info("Main    : all done")  # Output message indicating the main program has finished executing




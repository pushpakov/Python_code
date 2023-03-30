"""
    generate a list of numbers from 1 to 20, then add a random integer from 10–20 to each number in the list
    and then convert the list to a set so that there are no duplicates in the final output.
"""   
import random
import time
from multiprocessing import Manager, Pool

def generate_numbers_list(numbers_queue):
    for x in range(1, 21):
        numbers_queue.put(x)
        print("numbers_queue",numbers_queue.get())
        time.sleep(0.5)

def add_random(numbers_queue, randint_queue):
    while True:
        num = random.randint(10, 20)
        if not numbers_queue.empty():
            x = numbers_queue.get()
            randint_queue.put(x + num)
            print("randint_queue",randint_queue.get())   
        else:
            break

def numbers_list(randint_queue, shared_list):
    while True:
        if not randint_queue.empty():
            shared_list.append(randint_queue.get())
            print("shared_list", shared_list)
        else:
            break

if __name__ == '__main__':
    with Manager() as manager:
        shared_list = []
        numbers_queue = manager.Queue()
        randint_queue = manager.Queue()
        pool = Pool(processes=3)
        pool.apply_async(generate_numbers_list, args=(numbers_queue,))
        pool.apply_async(add_random, args=(numbers_queue, randint_queue))
        pool.apply_async(numbers_list, args=(randint_queue, shared_list))
        pool.close()
        pool.join()

        # Converting list to a set to remove duplicates
        final_set = (shared_list)
        print(final_set)






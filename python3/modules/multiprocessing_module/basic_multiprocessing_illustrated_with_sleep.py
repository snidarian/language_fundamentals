#!/usr/bin/python3
# Basic illustration of the multiprocessing module with the sleep command

import time
import multiprocessing


start = time.perf_counter()
print(f"Starting at {start}")


def do_something():
    print('Sleeping for 1 second')
    time.sleep(1)
    print('Done Sleeping')

# Define as many processes as needed
p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)
p3 = multiprocessing.Process(target=do_something)
p4 = multiprocessing.Process(target=do_something)
p5 = multiprocessing.Process(target=do_something)


# START() = Start child process
# Start those processes
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()

# JOIN() = wait until child process finishes
# Make sure those processes complete before continuing further in program
p1.join()
p2.join()
p3.join()
p4.join()
p5.join()


finish = time.perf_counter()
print(f"Finished at {finish}")


print(f'Finished in {round(finish-start, 2)} second(s)')









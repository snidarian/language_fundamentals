#!/usr/bin/python3
# Basic illustration of the multiprocessing module with the sleep command

import time
import multiprocessing
import os


GLOBAL_VARIABLE_EXAMPLE = "Test_string"


start = time.perf_counter()
print(f"Starting at {start}")


# This function will have access to globally defined variables
def do_something(proc_number):
    print(f'PID {os.getpid()}: Child Proc {proc_number} - Sleeping for 1 second')
    time.sleep(1)
    print(f'PID {os.getpid()}: Child Proc {proc_number} - Done Sleeping')

# Define as many processes as needed
p1 = multiprocessing.Process(target=do_something, args=(1,))
p2 = multiprocessing.Process(target=do_something, args=(2,))
p3 = multiprocessing.Process(target=do_something, args=(3,))
p4 = multiprocessing.Process(target=do_something, args=(4,))
p5 = multiprocessing.Process(target=do_something, args=(5,))


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









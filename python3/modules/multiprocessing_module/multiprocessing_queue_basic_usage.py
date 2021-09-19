#!/usr/bin/python3
# Uses the multiprocessing module to calculate large quantity of sequential squared integer


import multiprocessing
import numpy
import os
from colorama import Fore


def calculate_squares(numbers, q):
    for n in numbers:
        q.put((os.getppid(),n,n*n))
        print(f'PID {os.getpid()}: {n}^2 = ' + str(n*n))


if __name__ == "__main__":
    # .arrange() create an array of sequential integers
    # .reshape() creates a 2d array of X lists of Z size
    number_set = numpy.arange(1, 101, 1).reshape(10,10)
    # multiprocessing.Queue() class is used to shared data between processes
    q = multiprocessing.Queue()
    
    for set_of_100 in number_set:
        p = multiprocessing.Process(target=calculate_squares, args=(set_of_100, q))
        p.start()
        p.join()

    print(Fore.YELLOW)
    print("\n\nPrinting out data set items from the multiprocessing shared queue in the following format:")
    print("CALC PID, NUMBER, NUMBER SQUARED\n")
    print(Fore.RESET)
    while q.empty() is False:
        print(q.get())
    
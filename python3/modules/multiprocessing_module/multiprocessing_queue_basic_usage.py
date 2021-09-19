#!/usr/bin/python3


import multiprocessing
import numpy


def calculate_squares(numbers, q):
    
    for n in numbers:
        q.put((n,n*n))
        print(f'(Inside process): {n}^2 = ' + str(n*n))


if __name__ == "__main__":
    number_set = numpy.arange(1, 200, 1)
    # multiprocessing.Queue() class is used to shared data between processes
    q = multiprocessing.Queue()
    #p = multiprocessing.Process(target=calculate_squares, args=(number_set, q))

    print(number_set)


    #p.start()

    #p.join()

    while q.empty() is False:
        print(q.get())
    
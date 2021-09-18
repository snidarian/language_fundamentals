#!/usr/bin/python3


import multiprocessing


def calculate_squares(numbers, q):
    
    for n in numbers:
        q.put((n,n*n))
        print(f'(Inside process): {n}^2 = ' + str(n*n))


if __name__ == "__main__":
    number_set = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # multiprocessing.Queue() class is used to shared data between processes
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calculate_squares, args=(number_set, q))


    p.start()

    p.join()

    while q.empty() is False:
        print(q.get())
    
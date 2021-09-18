#!/usr/bin/python3


from basic_multiprocessing_illustrated_with_sleep import do_something
import time
import multiprocessing



def do_something() -> None:
    print("Sleeping for one second")
    time.sleep(1)
    print("Done sleeping")




start = time.perf_counter()



for _ in range(10):
    p = multiprocessing.Process(target=do_something)
    p.start()




finish = time.perf_counter()

time_elapsed = round((finish-start), 2)


print(f"Program ran in {time_elapsed} second(s)")




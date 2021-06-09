#!/usr/bin/python3


import numba


list0 = [1, 2, 3, 42.23, 14242414.2423423423432, "string", [234, 21342, 234324], ["asdfa", "asdff", "asdfaff"], True, False]
list1 = [1, 2, 3, 4, 5, 6]


@numba.njit
def function0():
    for _ in list1:
        print(_)



function0()





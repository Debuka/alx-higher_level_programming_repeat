#!/usr/bin/python3
"""returns weighted average of all the integer tuple"""

def weight_average(my_list=[]):
    if not my_list:
        return 0

    idx = 0
    fn = 0

    for tup in my_list:
        idx += tup[0] * tup[1]
        fn += tup[1]

    return (idx / fn)


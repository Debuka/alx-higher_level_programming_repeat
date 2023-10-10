#!/usr/bin/python3
"""searches for multiples of two in a list"""

def divisible_by_2(my_list=[]):
    int_value = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            int_value.append(True)
        else:
            int_value.append(False)

    return (int_value)

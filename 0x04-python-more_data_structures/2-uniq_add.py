#!/usr/bin/python3

def uniq_add(my_list=[]):
    d_unique_list = set(my_list)
    idx = 0

    for i in d_unique_list:
        idx += i

    return (idx)

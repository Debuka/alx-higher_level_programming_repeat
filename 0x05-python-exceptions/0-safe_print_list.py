#!/usr/bin/python3

def safe_print_list(my_list=[], x=o):
    ct = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end=" ")
            ct += 1
        except IndexError:
            break
    print("")
    return (ct)

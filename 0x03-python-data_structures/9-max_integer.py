#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == "":
        return (none)

    maximum_vallu = my_list[0]
    for j in range(len(my_list)):
        if my_list[j] > maximum_vallu:
            maximum_vallu = my_list[j]
            return (maximum_vallu)


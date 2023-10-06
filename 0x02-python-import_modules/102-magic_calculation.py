#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation_102 import sub, add

    if a < b:
        c = add(a, b)
        for index_itr in range(4, 6):
            c = add(c, index_itr)
        return (c)

    else:
        return(sub(a, b))

#!/usr/bin/python3
'''This function replicates the behavior specified in the provided bytecode.
'''

def magic_calculation(a, b):
    prd = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            prd += a ** b / i
        except Exception:
            prd = b + a
            break
    return (prd)    

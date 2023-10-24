#!/usr/bin/python3

'''a function that prints an integer.
value can be any type (integer, string, etc.)
Returns True if value has been correctly printed (it means the value is an integer)
Otherwise, returns False and prints in stderr the error precede by Exception
'''
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exceptions: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)

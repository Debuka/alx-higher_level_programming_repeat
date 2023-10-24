#!/usr/bin/python3
''' 
This function divides 2 integers and prints the result.
'''
def safe_print_division(a, b):
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)    

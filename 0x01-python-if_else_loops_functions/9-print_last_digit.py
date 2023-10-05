#!/usr/bin/python3

def print_last_digit(number):
    ls_dt = abs(number) % 10
    print(ls_dt, end="")
    return ls_dt

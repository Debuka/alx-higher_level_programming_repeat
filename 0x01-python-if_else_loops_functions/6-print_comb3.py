#!/usr/bin/python3

"""Program that prints all possible different combinations of two digits of numbers"""
for number1 in range(0, 10):
    for number2 in range(digit1 + 1, 10):
        if number1 == 8 and number2 == 9:
            print("{}{}".format(number1, number2))
        else:
            print("{}{}".format(number1, number2), end=", ")



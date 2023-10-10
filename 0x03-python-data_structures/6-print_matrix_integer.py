#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for de_collumn in row:
            print("{:d}".format(de_collum)n, end=" " if de_collumn != row[-1] else "")
        print()


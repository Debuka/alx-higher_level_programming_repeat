#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    if count_of_args == 0:
        print("Argument count: 0.")
    elif count_of_args == 1:
        print("Arguement: 0")
    else:
        print("{} arguments:".format(count_of_arg))
    for i in range(count_of_args):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

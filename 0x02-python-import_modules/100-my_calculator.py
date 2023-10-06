#!/usr/bin/python3

    from calculator_1 import add, div, sub, mul
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    functs = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(functs.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, functs[sys.argv[2]](a, b)))

    if __name__ == "__main__":
        a, operator, b, ops = check_args(sys.argv[1:])
        perform_operation(a, operator, b, functs)

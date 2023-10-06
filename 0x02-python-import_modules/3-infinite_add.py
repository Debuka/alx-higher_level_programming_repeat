#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    all_args = 0
    for i in range(len(sys.argv) - 1):
        all_args += int(sys.argv[i + 1])
    print("{}".format(all_args))

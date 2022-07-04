#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum_args = 0
    for i in range(1, len(argv)):
        sum_args += int(argv[i])
    print("{}".format(sum_args))

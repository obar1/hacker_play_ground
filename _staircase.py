#!/bin/python3


#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#


def staircase(i):
    while True:
        res = "#" * i
        yield str.rjust(res, n)


if __name__ == "__main__":
    n = int(input().strip())
    res = (next(staircase(i)) for i in range(1, n + 1))
    print("\n".join(res))

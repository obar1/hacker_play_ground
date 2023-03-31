#!/bin/python3

import os

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#


def aVeryBigSum(ar):
    print(ar)
    return sum(ar)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + "\n")

    fptr.close()

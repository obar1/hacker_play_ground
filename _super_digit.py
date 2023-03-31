#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


def superDigit(n, k):
    # Write your code here
    if k == 1:
        return n

    n_str = [*str(n)]
    print(n_str)
    n_ints = [int(i) for i in n_str]
    print(n_ints)
    sum_n = sum(n_ints)
    print(sum_n)
    return superDigit(sum_n, len(n_ints))


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])
    nn = str(n) * k
    kk = n * k
    result = superDigit(nn, kk)

    fptr.write(str(result) + "\n")

    fptr.close()

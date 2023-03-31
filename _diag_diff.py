#!/bin/python3

import os

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def get_diag_sum(arr, diagonals):
    """get sum of input"""
    print(diagonals)
    diag1 = []
    for d in diagonals:
        # print(type(d))
        a, b, *z = d
        # print(type(a))
        # print(type(b))
        diag1.append(arr[a][b])
        print(diag1)
    return sum(diag1)


def get_diag_idx(card):
    """get idx"""
    r = range(0, card)
    diag1_dix = [(i, i) for i in r]
    print("_diag1_dix")
    print(diag1_dix)
    diag2_idx = []
    for i in range(0, card):
        diag2_idx.append((i, card - i - 1))
    print("diag2_idx")
    print(diag2_idx)
    return (diag1_dix, diag2_idx)


def diagonalDifference(card, arr):
    print(arr)
    diag1_idx, diag2_idx = get_diag_idx(card)

    diag1 = get_diag_sum(arr, diag1_idx)
    diag2 = get_diag_sum(arr, diag2_idx)
    return abs(diag1 - diag2)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(n, arr)

    fptr.write(str(result) + "\n")

    fptr.close()

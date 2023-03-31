#!/bin/python3


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    # print(arr)
    sarr = sorted(arr)
    min_sum = sum(sarr[:4])
    max_sum = sum(sarr[1:])
    print(f"{min_sum} {max_sum}")


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

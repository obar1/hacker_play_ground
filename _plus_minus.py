#!/bin/python3


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here]
    sum_positive = sum([1 for x in arr if x > 0])
    sum_zero = sum([1 for x in arr if x == 0])
    sum_neg = sum([1 for x in arr if x < 0])
    sum_all = len(arr)
    print(
        f"""\
{sum_positive/ sum_all}
{sum_neg / sum_all}
{sum_zero / sum_all}\
"""
    )


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

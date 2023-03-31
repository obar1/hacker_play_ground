#!/bin/python3

import os
import heapq

#
# return list of pick of changes for the bill


def gen_change(bill, coins):
    while True:
        heapq.heapify(coins)
        # print(coins)
        if len(coins) == 0:
            break
        c = coins[0]
        # print(bill)
        # print(c)

        if bill == 0 or bill <= c:
            break

        if bill > c:
            bill = bill - c
            yield coins.pop(0)


def f(s):
    # Write your code here
    print(s)
    coins = [int(c) for c in s.split(" ") if str(c).isdigit()]
    bill = 67

    print(bill)
    print(coins)
    res = list(gen_change(bill, coins))
    print(res)
    print([x for x in coins if x not in res])
    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = f(s)

        fptr.write(str(result) + "\n")

    fptr.close()

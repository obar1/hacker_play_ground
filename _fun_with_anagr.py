#!/bin/python3

import os


#
# Complete the 'funWithAnagrams' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY text as parameter.
#


def funWithAnagrams(text):
    # Write your code here
    print(text)
    mapping = dict()
    for t in text:
        mapping[t] = "".join(sorted(t))
    print(mapping)
    res = []
    keys = list(mapping.keys())
    for k in keys:
        res.append(k)
        for j in keys[::-1]:
            if mapping[k] == mapping[j]:  # only the 1st
                res.remove(k)
                break

    print(res)
    return keys


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    text_count = int(input().strip())

    text = []

    for _ in range(text_count):
        text_item = input()
        text.append(text_item)

    result = funWithAnagrams(text)

    fptr.write("\n".join(result))
    fptr.write("\n")

    fptr.close()

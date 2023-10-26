#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#


def insertionSort1(n, arr):
    # Write your code here
    for i in range(1, n):
        j = n - 1
        key = str(arr[j])
        test = 0
        for k in range(n):
            arr[k] = str(arr[k])
        while True:
            if j == 0 or int(key) > int(arr[j - 1]):
                test = j
                break
            arr[j] = arr[j - 1]
            j -= 1
            print(" ".join(arr))
        arr[test] = key
    print(" ".join(arr))
    return


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

#!/bin/python3

import math
import os
import random
import re
import sys


def rotate(ls, d):
    # number of right rotations = len - d ?
    result = [None] * len(ls)
    right = len(ls) - d

    for i in range(len(ls)):
        divisor, remainder = divmod(i + right, len(ls))
        result[remainder] = ls[i]

    return result

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    a = list(map(int, input().rstrip().split()))
    result = rotate(a, k)
    print(" ".join([str(i) for i in result]))
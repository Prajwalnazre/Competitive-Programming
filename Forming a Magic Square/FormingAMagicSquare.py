#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    sumarr = []
    sum1 = 0
    for i in range(3):
        for j in range(3):
            sum1 = sum1 + s[i][j]
        sumarr.append(int(sum1))
        sum1 = 0

    #sumarr = sorted(sumarr)

    med = 15
    diffsum = 0
    for k in sumarr:
        diff = k - 15
        if(diff < 0):
            diff = int(diff/-1)
        diffsum = diffsum + diff

    return diffsum




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()


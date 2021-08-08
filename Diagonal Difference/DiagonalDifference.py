#!/bin/python3

import math
import os
import random
import re
import sys
#import numpy as np
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    #arr1 = np.array(arr)
    arr1 = arr

    d1 = 0
    d2 = 0
    arrShape = int(len(arr1))
    for i in range(arrShape):
        for j in range(arrShape):
            if(i == j):
                d1 = d1 + arr1[i][j]

    in1 = 0
    in2 = int(arrShape -1)

    for k in range(arrShape):
        d2 = d2 + arr1[in1][in2]
        in1 = in1 + 1
        in2 = in2 - 1
        
    differ = int(d1 - d2)

    if(differ < 0):
        differ = int(differ/-1)

    return differ            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


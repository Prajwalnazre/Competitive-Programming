#!/bin/python3

import math
import os
import random
import re
import sys


def biggerIsGreater(w):
    n = len(w) - 2
    while (n >= 0 and w[n] >= w[n + 1]) :
        n -= 1
        
    if len(w) < 2 :
        return "no answer"
    if len(w) == 2 :
        if w[0] < w[1] :
            return "".join(reversed(w))
        else :
            return "no answer" 
    
    if n == -1 :
        return "no answer"
    else :
        w = list(w)
        for i in reversed(range(n + 1, len(w))) :
            if w[i] > w[n] :
                w[n], w[i] = w[i], w[n]
                break
        
        w[n + 1:] = reversed(w[n + 1:])
        w = "".join(w)
        return w        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    coordinate = [r_q,c_q]
    # Up
    c = coordinate.copy()
    total = 0
    c[0] += 1
    if c not in obstacles : 
        while c not in obstacles and c[0] <= n :
            c[0] += 1
            total += 1            
        # print(total)
        
    # Down
    c = coordinate.copy()
    c[0] -= 1
    if c not in obstacles : 
        while c not in obstacles and c[0] >= 1 :
            c[0] -= 1
            total += 1
        # print(total)
        
    # Left
    c = coordinate.copy()
    c[1] -= 1
    if c not in obstacles : 
        while c not in obstacles and c[1] >= 1 :
            c[1] -= 1
            total += 1
        # print(total)
        
    # Right  
    c = coordinate.copy()    
    c[1] += 1
    if c not in obstacles : 
        while c not in obstacles and c[1] <= n :
            c[1] += 1
            total += 1
        # print(total)
        
    # Up Right 
    c = coordinate.copy()
    c[0] += 1    
    c[1] += 1
    if c not in obstacles : 
        while c not in obstacles and (c[1] <= n and c[0] <=n):
            c[0] += 1
            c[1] += 1
            total += 1
        # print(total)
        
    # Down Right
    c = coordinate.copy()
    c[0] -= 1    
    c[1] += 1
    if c not in obstacles : 
        while c not in obstacles and (c[1] <= n and c[0] >= 1) :
            # print(c)
            c[0] -= 1
            c[1] += 1
            total += 1
        # print(total)
        
    # Down Left
    c = coordinate.copy()
    c[0] -= 1    
    c[1] -= 1
    if c not in obstacles : 
        while c not in obstacles and (c[1] >= 1 and c[0] >= 1) :
            c[0] -= 1
            c[1] -= 1
            total += 1
        # print(total)
        
    # Up Left
    c = coordinate.copy()
    c[0] += 1    
    c[1] -= 1
    if c not in obstacles : 
        while c not in obstacles and (c[0] <= n and c[1] >= 1) :
            c[0] += 1
            c[1] -= 1
            total += 1
        # print(total)
        
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()


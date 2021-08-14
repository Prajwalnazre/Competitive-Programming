#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    dictionary = {
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven", 
        8 : "eight",
        9 : "nine",
        10 : "ten",
        11 : "eleven",
        12 : "twelve",
        13 : "thirteen",
        14 : "fourteen",
        16 : "sixteen",
        17 : "seventeen",
        18 : "eighteen",
        19 : "nineteen",
        20 : "twenty",
        21 : "twenty one",
        22 : "twenty two",
        23 : "twenty three",
        24 : "twenty four",
        25 : "twenty five",
        26 : "twenty six",
        27 : "twenty seven",
        28 : "twenty eight",
        29 : "twenty nine",
    }
    s1 = ""
    if m > 30 :
        h += 1
        s1 = "to"
        m = 60 - m
        if m == 15 :
            return "quarter to " + str(dictionary[h])
        else :
            return str(dictionary[m]) + " minutes to " + str(dictionary[h])
    if m == 30 :
        return "half past " + str(dictionary[h])
    if m < 30 and m > 1 :
        if m == 15 :
            return "quarter past " + str(dictionary[h])
        else :
            return str(dictionary[m]) + " minutes past " + str(dictionary[h])
    if m == 0 :
        return str(dictionary[h]) + " o' clock"
    if m == 1 :
        return str(dictionary[m]) + " minute past " + str(dictionary[h])
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()


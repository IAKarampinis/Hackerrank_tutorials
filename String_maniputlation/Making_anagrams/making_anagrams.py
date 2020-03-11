#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    s1 = {}
    s2 = {}
    for iChar in a:
        try:
            s1[iChar]+=1
        except KeyError:
            s1[iChar]=1
        
    for iChar in b:
        try:
            s2[iChar]+=1
        except KeyError:
            s2[iChar]=1
    
    chars1 = set(s1.keys())
    chars2 = set(s2.keys())
    count = 0
    # First, we count the chars in a not in b and the chars in b not in a 
    A_not_B = chars1-chars2
    B_not_A = chars2-chars1
    for char in A_not_B:
        count += s1[char]
    
    for char in B_not_A:
        count +=s2[char]
    
    # Now we count the intersection
    A_and_B = chars1&chars2
    for char in A_and_B:
        count += abs(s1[char]-s2[char] )

    return count
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    
    def insertion(x):
        arr.append(x)
        if x not in freqDict.keys():
            freqDict[x]=1
        else:
            freqDict[x]+=1


    def deletion(x):
        if x in arr:
            arr.remove(x)
            freqDict[x]-=1
    
    
    def freqCheck(freq):
        if freq in freqDict.values():
            result.append(1)
        else:
            result.append(0)

    
        
    freqDict = {}
    result = []
    arr = []
    operations = {1: insertion,
                  2: deletion,
                  3: freqCheck}
    
    for iQuery in range(len(queries)):
        operations[queries[iQuery][0]](queries[iQuery][1])


    return result
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    def insertion(x):
        try:
            freqDict[x]+=1
        except KeyError:
            freqDict[x]=1
    
    def deletion(x):
        try:
            freqDict[x]-=1
            if freqDict[x]==0:
                del freqDict[x]
        except KeyError:
            pass
    
    
    def freqCheck(freq):
        result.append(int(freq in freqDict.values()))

    
        
    freqDict = {}
    reverseDict={}
    result = []
    operations = {1: insertion,
                  2: deletion,
                  3: freqCheck}
    
    
    for iQuery, number in queries:
        operations[iQuery](number)


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

#!/bin/python3

import math
import os
import random
import re
import sys


def freqQuery(queries):

    def insertion(x):
        try:
            freqDict[x] += 1
            # even though the following is reverseDict amending, because
            # it happens only in this branch, it's faster than using another "if".
            reverseDict[freqDict[x]-1].remove(x)
            if reverseDict[freqDict[x]-1] == []:
                del reverseDict[freqDict[x]-1]
        except KeyError:
            freqDict[x] = 1

        # amend reverseDict
        try:
            reverseDict[freqDict[x]].append(x)
        except KeyError:
            reverseDict[freqDict[x]] = [x]

    def deletion(x):
        try:
            freqDict[x] -= 1
            performed_deletion = True
            # same logic should apply here. The append can go outside this environment,
            # but the remove should be here
            reverseDict[freqDict[x]+1].remove(x)
            if reverseDict[freqDict[x]+1] == []:
                del reverseDict[freqDict[x]+1]
            if freqDict[x] == 0:
                del freqDict[x]
        except KeyError:
            performed_deletion = False

        # amend reverseDict
        if performed_deletion:
            try:
                reverseDict[freqDict[x]].append(x)
            except KeyError:
                try:
                    reverseDict[freqDict[x]] = [x]
                except KeyError:
                    # here we pass, because if there is still a KeyError,
                    # it means freqDict[x] became 0 and we don't append at 0.
                    pass

    def freqCheck(freq):
        result.append(int(freq in reverseDict.keys()))

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

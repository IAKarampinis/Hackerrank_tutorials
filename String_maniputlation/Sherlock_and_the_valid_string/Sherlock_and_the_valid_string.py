
"""Code works for 100% of test cases """
import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    freq={}
    for char in s:
        try:
            freq[char]+=1
        except KeyError:
            freq[char]=1

    freq_list = list(freq.values())
    freq_set = set(freq_list)
    f_max = max(freq_list)
    f_min = min(freq_list)
    if len(freq_set)>2:
        return 'NO'
    else:
        if len(freq_set)==1:
            return 'YES'
        else:
            if 1 in freq_set:
                if freq_list.count(1)>1:
                    return 'NO'
                else:
                    return 'YES'
            else:
                if (f_max-f_min)==1:
                    return 'YES'
                else:
                    return 'NO'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

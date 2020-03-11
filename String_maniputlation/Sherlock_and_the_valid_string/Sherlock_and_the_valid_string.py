
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
        # if we have more than 2 different frequencies, the task is impossible.
        return 'NO'
    else:
        if len(freq_set)==1:
            # if we only have one frequency, all the characters appear the same number of times and we are done.
            return 'YES'
        else:
            # in this subcase, we have exactly 2 different frequencies of characters.
            if 1 in freq_set:
                # if we have characters that appear only once, check how many such characters there are.
                # if only one such character exists, we can delete it and the rest will have the same frequency.
                # otherwise, the task is impossible.
                if freq_list.count(1)>1:
                    return 'NO'
                else:
                    return 'YES'
            else:
                # finally, if we don't have characters that appear only once, check the difference between the 2 frequencies
                # that appear. If that difference is one, we can delete one character from the group with the higher frequency
                # and then both groups, and hence the whole set, will have a common frequency. Otherwise, we can't delete a
                # single character to achieve the task.
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

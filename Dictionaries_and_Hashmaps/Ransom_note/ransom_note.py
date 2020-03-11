
print('\n'*10)

#!/bin/python3

""" This version of the code runs succesfully for 100% of the test cases"""

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_words={}
    for word in magazine:
        if word not in magazine_words.keys():
            magazine_words[word]=1
        else:
            magazine_words[word]+=1
    
    note_words={}
    for word in note:
        if word not in note_words.keys():
            note_words[word]=1
        else:
            note_words[word]+=1
    
    result = True

    for word in note:
        if word not in magazine_words.keys():
            result = False
        elif (note_words[word]>magazine_words[word]):
            result = False
    
    if result:
        print('Yes')
    else:
        print('No')



if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

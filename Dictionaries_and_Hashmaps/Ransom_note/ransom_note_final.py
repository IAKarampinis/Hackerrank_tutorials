#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_words={}
    for word in magazine:
        try:
            magazine_words[word]+=1
        except KeyError:
            magazine_words[word]=1
    
    note_words={}
    for word in note:
        try:
            note_words[word]+=1
        except KeyError:
            note_words[word]=1
    
    test = True

    for word in note:
        if word not in magazine_words.keys():
            test = False
        elif (note_words[word]>magazine_words[word]):
            test = False
    
    if test:
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

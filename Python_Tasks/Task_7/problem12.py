# Problem 12:Making Anagrams
# HackerRank Link:https://www.hackerrank.com/challenges/making-anagrams/problem

import math
import os
import random
import re
import sys

def makingAnagrams(s1, s2):
    
    freq = [0] * 26

    for char in s1:
       freq[ord(char) - ord('a')] += 1

    for char in s2:
       freq[ord(char) - ord('a')] -= 1

    deletions = 0

    for count in freq:
       deletions += abs(count)

    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

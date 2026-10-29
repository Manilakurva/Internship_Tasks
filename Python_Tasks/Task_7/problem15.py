# Problem 15:Game of Thrones - I
# HackerRank Link:https://www.hackerrank.com/challenges/game-of-thrones/problem

import math
import os
import random
import re
import sys

def gameOfThrones(s):
    freq = [0] * 26

    for char in s:
        freq[ord(char) - ord('a')] += 1

    odd_count = 0

    for count in freq:
        if count % 2 != 0:
            odd_count += 1

    if odd_count <= 1:
        return "YES"
    else:
        return "NO"  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()


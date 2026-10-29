# Problem 14: Anagram
# HackerRank Link:https://www.hackerrank.com/challenges/anagram/problem

import math
import os
import random
import re
import sys

def anagram(s):
    n = len(s)

# If the length is odd, equal splitting is impossible
    if n % 2 != 0:
        return -1

# Split the string into two equal parts
    s1 = s[:n // 2]
    s2 = s[n // 2:]

# Count character frequencies
    freq = [0] * 26

    for char in s1:
        freq[ord(char) - ord('a')] += 1

    for char in s2:
        freq[ord(char) - ord('a')] -= 1

# Count the required changes
    changes = 0

    for count in freq:
        if count > 0:
            changes += count
            
    return changes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()

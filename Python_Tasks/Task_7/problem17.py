# Problem 17:Separate the Numbers
# HackerRank Link:  https://www.hackerrank.com/challenges/separate-the-numbers/problem

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        first = s[:i]
        
        if first[0] == '0':
            continue
            
        num = int(first)
        expected = first
        next_num = num + 1
            
        while len(expected) < n:
            expected += str(next_num)
            next_num += 1
            
        if expected == s:
            print("YES", num)
            return

    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)

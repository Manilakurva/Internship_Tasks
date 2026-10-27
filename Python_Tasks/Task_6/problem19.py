# Problem 19:Company Logo
# HackerRank Link:https://www.hackerrank.com/challenges/most-commons/problem

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    count = Counter(s) 
    result = sorted(count.items(), key=lambda x: (-x[1], x[0])) 
    
    for char, frequency in result[:3]: 
        print(char, frequency)

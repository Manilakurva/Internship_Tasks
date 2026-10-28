# Problem 7:Alphabet Rangoli
# HackerRank Link:https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string
def print_rangoli(size):
    
    alphabet = string.ascii_lowercase 
    lines = [] 
    for i in range(size): 
        left = alphabet[size-1:size-i-1:-1] 
        middle = alphabet[size-i-1] 
        right = alphabet[size-i:size] 
        row = "-".join(left + middle + right) 
        row = row.center(4 * size - 3, "-") 
        lines.append(row) 
    for i in range(size - 2, -1, -1): 
        lines.append(lines[i]) 
    print("\n".join(lines))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

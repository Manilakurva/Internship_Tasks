# Problem 10:Designer Door Mat
# HackerRank Link:https://www.hackerrank.com/challenges/designer-door-mat/problem

n, m = map(int, input().split())

# Top part of the mat
for i in range(1, n, 2):
    print(('.|.' * i).center(m, '-'))

# Center
print('WELCOME'.center(m, '-'))

# Bottom part of the mat
for i in range(n - 2, 0, -2):
    print(('.|.' * i).center(m, '-'))

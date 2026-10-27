# Problem 14:Set .intersection() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

result = english.intersection(french)

print(len(result))

# Problem 6: Find the Runner-Up Score!
# HackerRank Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
n = int(input())
numbers = list(map(int, input().split()))

unique_numbers = sorted(set(numbers))

print(unique_numbers[-2])

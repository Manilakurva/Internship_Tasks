# Problem 19:Collections.Counter()
# HackerRank Link:https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

X = int(input())
shoe_sizes = list(map(int, input().split()))

shoe_inventory = Counter(shoe_sizes)

N = int(input())
total_money = 0

for _ in range(N):
    size, price = map(int, input().split())

    if shoe_inventory[size] > 0:
        total_money += price
        shoe_inventory[size] -= 1

print(total_money)

# Problem 12:Set .discard(), .remove() & .pop()
# HackerRank Link:https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = input()
s = set(map(int, input().split()))
for i in range(int(input())):
    c = input().split()
    if c[0] == 'pop':
        s.pop()
    elif c == 'remove':
        s.remove(int(c[1]))
    else:
        s.discard(int(c[1]))
print(sum(s))

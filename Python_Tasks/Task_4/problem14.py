# Problem 14:Set .add()
# HackerRank Link:https://www.hackerrank.com/challenges/py-set-add/problem

if __name__ == '__main__':
    n = int(input())
    countries = set()

    for i in range(n):
        country = input()
        countries.add(country)

    print(len(countries))

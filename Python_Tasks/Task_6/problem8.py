# Problem 8:Tuples
# HackerRank Link:https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int,input().split()))
    print(hash(integer_list))

# Problem 2:String Split and Join
# HackerRank Link:https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    # write your code here
    word= line.split()
    new= "-".join(word)
    return new
    
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

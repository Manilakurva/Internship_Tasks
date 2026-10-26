# Problem 18:The Minion Game
# HackerRank Link:https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    kevin = 0
    stuart = 0
    vowels = "AEIOU"

    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

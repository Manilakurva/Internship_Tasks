# Problem 4:Funny String
# HackerRank Link:https://www.hackerrank.com/challenges/funny-string/problem

def funnyString(s):
    r = s[::-1] 
    for i in range(1, len(s)): 
        diff1 = abs(ord(s[i]) - ord(s[i - 1])) 
        diff2 = abs(ord(r[i]) - ord(r[i - 1])) 
        if diff1 != diff2: 
            return "Not Funny" 
    return "Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()

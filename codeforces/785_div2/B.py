import sys
from collections import Counter
input = sys.stdin.readline

def solver(s):
    queueChar = [s[0]]
    flag = False
    for i in range(1,len(s)):
        if queueChar[0]==s[i]:
            flag = True
            queueChar.pop(0)
        elif flag:
            return 'NO'
        queueChar.append(s[i])


    newS = Counter(queueChar)
    for key,value in newS.items():
        if value>1:
            return 'NO'
    
    return 'YES'
for _ in range(int(input())):
    s = input().rstrip()

    print(solver(s))
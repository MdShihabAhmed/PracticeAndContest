import sys

input = sys.stdin.readline

def solver(s):
    key = []
    for i in s:
        if i=='r' or i=='g' or i =='b':
            key.append(i)
        elif i=='R' or i=='G' or i =='B':
            if i.lower() not in key:
                return "NO"

    return "YES"


for _ in range(int(input())):
    s = input().rstrip()

    print(solver(s))
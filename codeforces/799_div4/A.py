import sys

input = sys.stdin.readline

def solver(a,b,c,d):
    result = 0

    if a<b:
        result+=1
    if a<c:
        result+=1
    if a<d:
        result+=1
    return result

for _ in range(int(input())):
    a,b,c,d = map(int,input().split())

    print(solver(a,b,c,d))
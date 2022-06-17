import sys,math
input = sys.stdin.readline

def solver(n, B, x, y):
    result = 0
    a = 0
    for i in range(n):
        if a+x<=B:
            a+=x
        else:
            a-=y
        result+=a
    
    return result
   
for _ in range(int(input())):
    n, B, x, y = map(int,input().split())

    print(solver(n, B, x, y))
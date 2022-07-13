import sys
input = sys.stdin.readline

def solver(s):
    pass

for _ in range(int(input())):
    a, b = map(int,input().split())
    c, d = map(int,input().split())
    if a+b+c+d==0:
        print(0)
    elif a+b+c+d==4:
        print(2)
    else:
        print(1)
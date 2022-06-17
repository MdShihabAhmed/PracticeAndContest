import sys

input = sys.stdin.readline

def solver(x, y):
    if y%x==0:
        print(1, y//x)
    else:
        print(0, 0)
for _ in range(int(input())):
    x, y = map(int,input().split())

    solver(x, y)
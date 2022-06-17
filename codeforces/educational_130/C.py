import sys

input = sys.stdin.readline

def solver(a, b, c, x, y):
    if a>=x and b>=y:
        return 'YES'
    if max(0,x-a)+max(0,y-b)<=c:
        return 'YES'
    return 'NO'
for _ in range(int(input())):
    a, b, c, x, y = map(int,input().split())

    print(solver(a, b, c, x, y))
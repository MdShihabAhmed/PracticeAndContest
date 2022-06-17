import sys
input = sys.stdin.readline
from math import sqrt

def solver(x, y):
    if x==0 and y==0:
        return 0
    if sqrt(x**2+y**2).is_integer():
        return 1
    return 2

for _ in range(int(input())):
    x, y = map(int,input().split())

    print(solver(x, y))
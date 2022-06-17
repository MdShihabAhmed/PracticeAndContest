import sys
from functools import reduce

input = sys.stdin.readline

def solver(arr):
    moves = 0
    maxx = float('-inf')
    for i in arr:
        if i> maxx:
            maxx = i
            moves+=1

    if moves%2:
        return "BOB"
    else:
        return "ANDY"

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    print(solver(arr))
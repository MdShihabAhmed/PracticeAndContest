import sys
from functools import reduce
from operator import xor

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))

    res = reduce(xor, s)
    ones = sum(s)

    if res==0:
        if n==ones and ones%2==0:
            print("First")
        else:
            print("Second")
    else:
        if n==ones and ones%2==1:
            print("Second")
        else:
            print("First")

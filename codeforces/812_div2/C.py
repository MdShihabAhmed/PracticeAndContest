import sys
from math import sqrt,ceil

input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    arr = [0]*n
    dupliN = n-1
    index = 0
    while(index<n):
        temp = ceil(sqrt(dupliN))
        addition = temp*temp-dupliN
        limit = addition
        for i in range(dupliN,limit-1,-1):
            arr[i] = addition
            addition += 1
            index += 1
        dupliN = limit-1
    
    print(' '.join([str(i) for i in arr]))


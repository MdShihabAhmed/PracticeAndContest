import sys
from collections import defaultdict

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    daughter = defaultdict(list)
    for i in range(n):
        temp = list(map(int,input().split()))
        daughter[i+1] = temp[1:]
    unmarried = -1
    kingdom = [False]*(n+1)
    for key,value in daughter.items():
        for val in value:
            if not kingdom[val]:
                kingdom[val] = True
                break
        else:
            unmarried = key
    
    if unmarried<0:
        print("OPTIMAL")
    else:
        print("IMPROVE")
        for i in range(1,n+1):
            if not kingdom[i]:
                print(unmarried, i)
                break



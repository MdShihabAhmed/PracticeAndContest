import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    up = 0
    lo = 0
    for c in s:
        if c=="_":
            lo+=1
        else:
            up+=1
    
    left = (up+1)//2
    right = (up)//2
    print(left*right*lo)
import sys

input = sys.stdin.readline

for test in range(int(input())):
    n = int(input())
    window = []
    maxSpeed = float('inf')
    minSpeed = float('-inf')
    for i in range(n):
        a,b = map(int,input().split())
        
        window.append([a,b])
        if a!=0:
            maxSpeed = min(maxSpeed, (i+1)/a)
        minSpeed = max(minSpeed, (i+1)/b)
    
    if minSpeed<=maxSpeed:
        print(f"Case #{test+1}: {minSpeed}")
    else:
        print(f"Case #{test+1}: {-1}")
        
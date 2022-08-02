import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, H, M = map(int,input().split())

    result = float('inf')
    sleepStart = H*60+M
    for i in range(n):
        h, m = map(int,input().split())
        temp = 0
        sleepEnd = h*60+m
        if sleepEnd<sleepStart:
            temp = 24*60-sleepStart+sleepEnd
        else:
            temp = sleepEnd-sleepStart
        result = min(result, temp)
    
    print(result//60, result%60)
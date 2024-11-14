import sys

input = sys.stdin.readline

for test in range(int(input())):
    n, g = map(int,input().split())
    result = float('inf')
    stones = []
    off = 0
    for i in range(n):
        stone = int(input())
        stones.append(stone)
        if abs(stone-g)<result:
            result = abs(stone-g)
            off = stone
    stones.sort()
    for i in range(n):
        if stones[i]==off:
            print(f"Case #{test+1}: {i+1} {result}")
            break
            


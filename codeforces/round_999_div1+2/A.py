import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    odd = 0
    even = 0
    for c in a:
        if c%2:
            odd+=1
        else:
            even+=1
    result = 0
    if even:
        result = odd+1
    elif odd:
        result = odd-1
    
    print(result)
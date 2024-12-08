import sys
from collections import Counter
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a = Counter(a)

    result = 0
    for v in a.values():
        result+=(v//2)
    
    print(result)
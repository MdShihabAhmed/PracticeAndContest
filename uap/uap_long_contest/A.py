import sys

input = sys.stdin.readline

for _ in range(1):
    n = int(input())
    if n<=3:
        print(n-1)
        continue
    first = 2
    second = 3
    result = 2
    while(first+second<=n):
        second = second + first
        first = second - first
        result+=1
    
    print(result)
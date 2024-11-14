import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    a.sort()
    result = 0
    for i in range(n):
        result+=abs(a[i]-a[2*n-i-1])
    
    print(result)
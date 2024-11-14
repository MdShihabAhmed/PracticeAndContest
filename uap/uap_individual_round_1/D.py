import sys

input = sys.stdin.readline
n = int(input())
while(n):
    result = 0
    for i in range(1,n+1):
        result+=(i**2)
    print(result)
    n = int(input())
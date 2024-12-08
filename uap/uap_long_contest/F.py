import sys

input = sys.stdin.readline

n = int(input())
result = 0
for i in range(2,n):
    result+=(i*(i+1))
print(result)
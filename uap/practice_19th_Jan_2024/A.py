import sys

input = sys.stdin.readline

n = int(input())

result = 1
first = 1
for i in range(2, int(n**0.5)+1):
    if not n%i:
        first = i
        break
else:
    first = n
result += (n-first)//2

print(result)
import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int,input().split()))

total = sum(p)
result = total
for i in range(1<<n):
    temp = 0
    for j in range(n):
        if i&(1<<j):
            temp+=p[j]
    if temp!=total:
        result = min(result,abs(temp-(total-temp)))
print(result)
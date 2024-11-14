import sys

input = sys.stdin.readline

n, c = map(int, input().split())
a = list(map(int, input().split()))

result = 1
temp = a[0]

for i in range(1,n):
    if a[i]-temp>=c:
        temp =a[i]
        result+=1

print(result)

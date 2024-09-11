x = int(input())
n = int(input())
re = 0

for i in range(n):
    re = max(0,re+x-int(input()))

print(re+x)
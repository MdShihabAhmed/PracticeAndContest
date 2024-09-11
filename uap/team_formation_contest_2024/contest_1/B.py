import sys
from bisect import bisect_left,bisect_right
input = sys.stdin.readline

n,a,b,d = map(int,input().split())

p = []
check = []
temp = list(map(int,input().split()))
for i in range(n):
    p.append([temp[i],i])
    check.append(temp[i])

p.sort(key= lambda x: x[0])
check.sort()

result = []

for i in range(bisect_left(check,a-d),bisect_right(check,b+d)):
    result.append(p[i][1])
print(" ".join(map(str,result)))
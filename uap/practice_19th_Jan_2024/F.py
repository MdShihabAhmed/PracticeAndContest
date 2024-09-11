import sys

input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))

for i in range(1,n):
    a[i][0]+=max(a[i-1][1],a[i-1][2])
    a[i][1]+=max(a[i-1][0],a[i-1][2])
    a[i][2]+=max(a[i-1][1],a[i-1][0])


print(max(a[-1]))
import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int,input().split()))

pre = [0]*(n+2)
one = 0

for i in range(n):
    if a[i]==1:
        one+=1
    pre[i+1]+=pre[i]
    if a[i]==0:
        pre[i+1]+=one


suf = [0]*(n+2)
zero =0
for i in range(n,-1,-1):
    if a[i-1]==0:
        zero+=1
    suf[i]+=suf[i+1]
    if a[i-1]==1:
        suf[i]+=zero
print(pre,suf)
re = 10**10
for i in range(1,n+1):
    re = min(re, pre[i]+suf[i])

print(re)

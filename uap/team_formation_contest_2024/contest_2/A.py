import sys

input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    x, y = map(int,input().split())
    a.append([x, y])

a.sort()
one = 0
two = 0
result = 0
i = 0
while(i<n):
    if a[i][1]==2:
        while(i<n and a[i][1]==2):
            two+=2
            i+=1
        result=max(result, one)
        result+=two
        two = 0
    elif a[i][1]==1:
        while(i<n and a[i][1]==1):
            one+=1
            i+=1
        result=max(one,result)
print(result+10**9)
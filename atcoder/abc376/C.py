import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort(reverse=True)
b.sort(reverse=True)
i = 0
result = -1
flag = 0
for j in range(n):
    if i>n-2:
        result = a[j]
        break
    if a[j]<=b[i]:
        i+=1
        continue
    else:
        result = a[j]
        flag+=1
    
if flag>1:
    print(-1)
else:
    print(result)

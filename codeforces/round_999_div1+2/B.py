import sys
from bisect import bisect_left

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    flag = False
    for i in range(n-1):
        if a[i]==a[i+1]:
            for j in range(i+2,n-1):
                if (a[j+1]-a[j])<a[i]+a[i+1]:
                    print(a[j],a[j+1],a[i],a[i+1])
                    flag = True
                    break
            if not flag:
                for j in range(i-1):
                    if (a[j+1]-a[j])<a[i]+a[i+1]:
                        print(a[j],a[j+1],a[i],a[i+1])
                        flag = True
                        break
            if not flag:
                if i-1>=0 and i+2<n and (a[i+2]-a[i-1])<a[i]+a[i+1]:
                    print(a[i-1],a[i+2],a[i],a[i+1])
                    flag = True
                    break
            break

        if flag:
            break
    
    if not flag:
        print(-1)
import sys
import heapq

input = sys.stdin.readline

def check(a,n,s1,s2):
    i = 0
    j = n-1
    result = []
    while(i<j):
        while(i<n and a[i]!=s1):
            i+=1
        while(j>=0 and a[j]!=s2):
            j-=1
        if i>=j:
            break

        a[i],a[j]=a[j],a[i]
        result.append([i+1,j+1])
        i+=1
        j-=1

    return result

def check2(a,n,s1,s2,mi,ma):
    i = 0
    j = n-1
    result = []
    while(i<j):
        while(i<n and a[i]!=s1):
            i+=1
        while(j>=0 and a[j]!=s2):
            j-=1
        if i>=j:
            break

        a[i],a[j]=a[j],a[i]
        result.append([i+1,j+1])
        i+=1
        j-=1

    return result





for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    
    result = []
    

    result.extend(check(a,n,2,1))
    result.extend(check(a,n,1,0))
    mi = 10**9
    ma = -1
    for i in range(n):
        if a[i]==1:
            mi = min(mi,i)
            ma = max(ma,i)
    print(a)
    result.extend(check2(a,n,2,0,mi,ma))
    

    print(len(result))
    if result:
        for d in result:
            print(d[0],d[1])


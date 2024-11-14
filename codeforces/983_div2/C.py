import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    i = 0
    j = n-1
    result1 = 0
    while(i+1<j and a[i]+a[i+1]<=a[j]):
        result1+=1
        i+=1
    
    i = 0
    j = n-1
    result2 = 0
    while(i+1<j and a[i]+a[i+1]<=a[j]):
        result2+=1
        j-=1
    print(min(result1,result2))
import sys

input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    l = 0
    r = 0
    le = 0
    for i in range(n):
        temp = 0
        for j in range(i+1,n):
            if a[i]<a[j]:
                temp-=1
            elif a[i]>a[j]:
                temp+=1
            if temp>le:
                le = temp
                l = i
                r = j
    
    print(l+1,r+1)
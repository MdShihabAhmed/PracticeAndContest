import sys
from collections import Counter
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    a = list(map(int,input().split()))
    ind = [0]*(k+1)
    for i in range(k):
        ind[a[i]]=1
    n = k-2
    for i in range(1,int(n**0.5)+1):
        if n%i==0 and ind[i] and ind[n//i]:
            print(i,n//i)
            break
    

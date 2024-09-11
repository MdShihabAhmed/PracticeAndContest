import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
index = [0 for i in range(6)]
index[0] = 10**9
for i in range(n):
    if index[a[i]-1]:
        index[a[i]]+=1  
        index[a[i]-1]-=1
print(index[-1])
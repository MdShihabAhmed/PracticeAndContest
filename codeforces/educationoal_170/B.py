import sys

input = sys.stdin.readline


mod = 10**9+7

t = int(input())

n = list(map(int,input().split()))
k = list(map(int,input().split()))

for i in range(t):
    print(pow(2,k[i],mod))

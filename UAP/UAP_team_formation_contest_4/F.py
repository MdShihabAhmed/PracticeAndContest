import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
result = [0]*n

for i in range(n-1):
    result[arr[i]-1]+=1

print("\n".join([str(i) for i in result]))

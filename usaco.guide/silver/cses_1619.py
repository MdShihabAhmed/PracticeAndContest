import sys

input = sys.stdin.readline

n = int(input())

customersTime = []

stayingTime = set()
for i in range(n):
    a, l = map(int,input().split())
    customersTime.append([a, l])
    stayingTime.add(a)
    stayingTime.add(l)

stayingTime = sorted(list(stayingTime))

compressedIndex = {stayingTime[i]:i for i in range((len(stayingTime)))}

arr = [0]*(len(stayingTime)+1)

for i in range(n):
    a, l = customersTime[i]
    arr[compressedIndex[a]]+=1
    arr[compressedIndex[l]]-=1

for i in range(1,len(arr)):
    arr[i]+=arr[i-1]

print(max(arr))
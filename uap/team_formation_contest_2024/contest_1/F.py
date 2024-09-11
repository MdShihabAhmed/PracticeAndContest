import sys

input = sys.stdin.readline

n = int(input())
walls = [0 for i in range(10**5+1)]
for i in range(1,4):
    temp = set(map(int,input().split()))
    for h in temp:
        walls[h]+=1

result = -1
for i in range(10**5+1):
    if walls[i]==3:
        result=max(result,i)

print(result)

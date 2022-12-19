#spoj haybal stacking
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
stacks = [0]*(n+1)
for i in range(k):
	a, b = map(int, input().split())
	stacks[a-1]+=1
	stacks[b]-=1

for i in range(n):
	stacks[i+1]+=stacks[i]

stacks.sort()
print(stacks[(n+1)//2])
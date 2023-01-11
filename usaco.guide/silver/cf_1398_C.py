import sys
from collections import defaultdict
    
input = sys.stdin.readline

for _ in range(int(input())):
	n = int(input())
	digits = input().rstrip()
	digits = [ord(digits[i])-ord('0') for i in range(n)]
	
	prefixSum = [0]*(n+1)
	result = 0
	previousSameIndex = defaultdict(int)
	previousSameIndex[0] = 1

	for i in range(n):
		prefixSum[i+1] = prefixSum[i]+digits[i]
	
		result += previousSameIndex[prefixSum[i+1]-(i+1)]
		previousSameIndex[prefixSum[i+1]-(i+1)]+=1
	print(result)
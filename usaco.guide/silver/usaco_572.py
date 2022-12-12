import sys

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	n, q = map(int, input().split())
	
	prefixSum = [[0, 0, 0]]
	for i in range(n):
		breedID = int(input())
		prefixSum.append(prefixSum[-1][:])
		prefixSum[i+1][breedID-1]+=1
	
	result = []
	for i in range(q):
		a, b = map(int, input().split())
		result.append(f"{prefixSum[b][0]-prefixSum[a-1][0]} {prefixSum[b][1]-prefixSum[a-1][1]} {prefixSum[b][2]-prefixSum[a-1][2]}")
	
	print('\n'.join(result))


if __name__ == "__main__":
	solver('bcount')
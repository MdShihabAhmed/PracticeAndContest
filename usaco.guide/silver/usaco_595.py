import sys

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	n = int(input())
	
	result = 0
	distinctIDs = []
	prefixSum = [0]*(n+1)
	
	first = [0]*7
	
	for i in range(n):
		distinctIDs.append(int(input()))
		prefixSum[i+1] = (prefixSum[i]+distinctIDs[-1])%7

		if first[prefixSum[i+1]]:
			result = max(result, i+1-first[prefixSum[i+1]])
		else:
			first[prefixSum[i+1]] = i+1

	print(result)

if __name__ == "__main__":
	solver('div7')
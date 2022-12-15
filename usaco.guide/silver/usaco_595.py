import sys

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	n = int(input())
	result = 0
	distinctIDs = []
	prefixSum = [0]*(n+1)
	for i in range(n):
		distinctIDs.append(int(input()))
		prefixSum[i+1] = (prefixSum[i]+distinctIDs[-1])%7

	first = [0]*7
	second = [0]*7
	for i in range(1,n+1):
		if first[prefixSum[i]]:
			second[prefixSum[i]] = i
		else:
			first[prefixSum[i]] = i

	result = 0
	for i in range(7):
		result = max(result, second[i]-first[i])
	
	print(result)


if __name__ == "__main__":
	solver('div7')
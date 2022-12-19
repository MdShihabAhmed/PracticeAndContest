import sys

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	n, k, b = map(int,input().split())
	
	signals = [0]*(n+1)

	for i in range(b):
		signals[int(input())] = 1
	
	result = n
	for i in range(1,n+1):
		signals[i]+=signals[i-1]
	
		if i<k:
			continue
		result = min(result,signals[i]-signals[i-k])
	
	print(result)

if __name__ == "__main__":
	solver('maxcross')
import sys

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	n, k, b = map(int,input().split())
	
	signals = [0]*(n+1)

	for i in range(b):
		signals[int(input())] = 1
	
	for i in range(n):
		signals[i+1]+=signals[i]
	
	result = n
	for i in range(k,n+1):
		result = min(result,signals[i]-signals[i-k])
	
	print(result)

if __name__ == "__main__":
	solver('maxcross')
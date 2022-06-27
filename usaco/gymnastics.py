import sys

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	#solve here
	k, n = map(int,input().split())
	results = [n]*n
	for _ in range(k):
		ranks = list(map(int,input().split()))
		for i in range(n):
			results[ranks[i]-1] = min(n-1-i,results[ranks[i]-1])
	
	print(results)
	print(sum(results))

if __name__ == "__main__":
	solver('gymnastics')
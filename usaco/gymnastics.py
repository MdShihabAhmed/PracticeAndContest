import sys

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	#solve here
	k, n = map(int,input().split())
	ranks = []
	for _ in range(k):
		ranks.append(list(map(int,input().split())))
	results = [[1 for i in range(n)] for j in range(n)]
	
	for i in range(n):
		for j in range(k):
			for l in range(n):
				if i+1==ranks[j][l]:
					results[i][ranks[j][l]-1]-=1
					break
				results[i][ranks[j][l]-1]-=1

	summ = 0
	for i in range(n):
		for j in range(n):
			if results[i][j]>0:
				summ+=results[i][j]

	print(summ)	
		


if __name__ == "__main__":
	solver('gymnastics')
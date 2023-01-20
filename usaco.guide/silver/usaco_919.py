import sys

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	n, k = map(int,input().split())
	
	barn = [[0]*(1002) for i in range(1002)]

	for i in range(n):
		x1, y1, x2, y2 = map(int,input().split())
		barn[x1+1][y1+1]+=1
		barn[x1+1][y2+1]-=1
		barn[x2+1][y1+1]-=1
		barn[x2+1][y2+1]+=1
	
	result = 0
	for i in range(1,1002):
		for j in range(1,1002):
			barn[i][j]+= barn[i-1][j] + barn[i][j-1] - barn[i-1][j-1]
			if barn[i][j]==k:
				result+=1

	print(result)

if __name__ == "__main__":
	solver('paintbarn')
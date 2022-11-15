import sys

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	#solve here
	n = int(input())
	flippedOrNot = []

	for i in range(n):
		flippedOrNot.append(input().rstrip())
	
	result = [0]*n

	for i in range(n-1,-1,-1):
		for j in range(n-1,-1,-1):
			if sum(result[j:])%2: # checking if the current cell flipped or not
				if flippedOrNot[i][j]=='0': # if flipped: '0' is tipped and '1' is un-tipped
					result[j]+=1
			elif flippedOrNot[i][j]=='1':
				result[j]+=1

	print(sum(result))
if __name__ == "__main__":
	solver('cowtip')
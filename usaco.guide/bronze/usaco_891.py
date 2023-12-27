import sys

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	#solve here
	shell = [1,2,3]
	result = [0,0,0]
	for i in range(int(input())):
		a, b, g = map(int,input().split())
		shell[a-1],shell[b-1] = shell[b-1],shell[a-1]
		result[shell[g-1]-1]+=1
	
	print(max(result))

if __name__ == "__main__":
	solver('shell')
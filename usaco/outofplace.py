import sys

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	#solve here
	n = int(input())
	order = [0]*n

	temp = 0
	value = [0]*n
	for i in range(n):
		order[i] = int(input())
		if temp==order[i]:
			value[i] = 0
		else:
			value[i] = 1
		temp = order[i]

	result = 0
	for j in range(n):
		for i in range(n-1):
			if order[i+1]<order[i]:
				order[i+1],order[i] = order[i],order[i+1]
				result+=value[i]

	print(result)

if __name__ == "__main__":
	solver('outofplace')
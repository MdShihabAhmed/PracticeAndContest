import sys

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	n, k = map(int,input().split())
	arr = []
	for _ in range(n):
		arr.append(int(input()))
	arr.sort()
	i=0
	j=n-1
	result = n

	while(i<=j):
		if arr[j]-arr[i]>k:
			result-=1
			if arr[j]-arr[i+1]>k:
				j-=1
			else:
				i+=1
		else:
			break
	
	print(result)
if __name__ == "__main__":
	solver('diamond')
import sys

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	x, y, m = map(int, input().split())
	result = 0
	temp = m-(m%x)
	i=(m//x)+1
	while(i):
		temp -= x
		if temp+y<=m:
			temp+=y
		if temp>result:
			result = temp
		i-=1
	print(result)

if __name__ == "__main__":
	solver('pails')
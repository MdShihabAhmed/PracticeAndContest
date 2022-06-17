import sys

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	#solve here

if __name__ == "__main__":
	solver('cowsignal')
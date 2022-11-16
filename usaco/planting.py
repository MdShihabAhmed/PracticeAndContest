import sys
from collections import defaultdict

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	#solve here
	graph = defaultdict(list)
	n = int(input())
	for i in range(n-1):
		node1, node2 = map(int,input().split())
		graph[node1].append(node2)
		graph[node2].append(node1)
	
	result = 0
	for key, value in graph.items():
		if len(value)>result:
			result = len(value)
	
	print(result + 1)

if __name__ == "__main__":
	solver('planting')
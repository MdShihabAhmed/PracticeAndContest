import sys

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	#solve here
	n, m = map(int,input().split())
	graph = [[] for i in range(n+1)]
	for i in range(m):
		node1, node2 = map(int,input().split())
		graph[node2].append(node1)
		graph[node1].append(node2)

	result = [0]*(n)
	grass = {1,2,3,4}
	for i in range(1,n+1):
		temp = set()
		for j in graph[i]:
			temp.add(result[j-1])
		temp = grass-temp
		result[i-1] = min(temp)
	
	print(*result,sep='')


if __name__ == "__main__":
	solver('revegetate')
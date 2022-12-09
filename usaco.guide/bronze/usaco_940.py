import sys

def solver(filename):
	sys.stdin = open(filename + '.in', 'r')
	sys.stdout = open(filename + '.out', 'w')

	#solve here
	n = int(input())
	graph = [[] for i in range(n+1)]
	for i in range(n-1):
		node1, node2 = map(int,input().split())
		graph[node2].append(node1)
	
	for i in range(1,n+1):
		visited = [0]*(n+1)
		stack = [i]
		visited[i]=1
		while(stack):
			top = stack.pop()
			for child in graph[top]:
				if not visited[child]:
					visited[child] = 1
					stack.append(child)
		if sum(visited)==n:
			print(i)
			break
	else:
		print(-1)

if __name__ == "__main__":
	solver('factory')
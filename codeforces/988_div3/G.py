import sys
from collections import defaultdict,deque
input = sys.stdin.readline

primeFactors = defaultdict(list)
primeToIndex = defaultdict(list)
graph = defaultdict(set)

n = int(input())
a = list(map(int,input().split()))

for i in range(n):


    num = a[i]
    div_num = 1
    while(num!=1):
        largest = max_div[num]
        for v in primeToIndex[str(largest)]:
            graph[v].add(str(i+1))

        count = 0
        while num % largest == 0:
            count += 1
            num //= largest
        primeFactors[str(a[i])].append(str(largest))
        primeToIndex[str(largest)].append(str(i+1))


result = [0]*(n+1)
result[1]=1
result = 0
visited = set()

queue = deque()
queue.append(str(1))



while(queue):
    parent = queue.popleft()

    for child in graph[parent]:
        if child in visited:
            continue
        queue.append(child)
        if int(child)==n:
            result+=1

print(result)

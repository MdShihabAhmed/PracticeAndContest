import sys
import heapq

input = sys.stdin.readline

n, k = map(int,input().split())
songs = []
for i in range(n):
    t, b = map(int,input().split())
    songs.append([b,t])

songs.sort(reverse=True)
taken = []
heapq.heapify(taken)
result = 0
total = 0
for i in range(n):
    heapq.heappush(taken,songs[i][1])
    total+=songs[i][1]
    if len(taken)>k:
        temp = heapq.heappop(taken)
        total-=temp
    result = max(result,total*songs[i][0])

print(result)
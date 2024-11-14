import sys
from collections import defaultdict,deque

input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    q = list(map(int,input().split()))
    k = list(map(int,input().split()))
    j = list(map(int,input().split()))
    play = [q,k,j]
    players = ["q","k","j"]
    graph = defaultdict(list)
    
    for i in range(3):
        for j in range(n):
            play[i][j] = [play[i][j],j+1]
        play[i].sort(reverse=True)
        temp = []
        for j in range(n-1,0,-1):
            temp.append((play[i][j][1],players[i]))
            graph[str(play[i][j-1][1])]+=temp
    
    previous = [0]*(n+2)
    queue = deque([(1,"")])
    visited = set()
    visited.add("1")
    found = False
    while(queue):
        card = queue.popleft()

        for val in graph[str(card[0])]:
            if val[0]<card[0]:
                continue
            if str(val[0]) not in visited:
                visited.add(str(val[0]))
                queue.append(val)
                previous[val[0]]= card
                if val[0]==n:
                    found = True
                    previous[n+1] = val
                    break
        if found:
            break
    
    if found:
        print("YES")
        result = []
        search = n+1
        while(previous[search][0]!=1):
            result.append(previous[search])
            search = previous[search][0]
        
        print(len(result))
        for i in range(len(result)-1,-1,-1):
            print(result[i][1],result[i][0])

    else:
        print("NO")
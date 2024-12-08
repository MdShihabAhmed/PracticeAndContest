import sys
import heapq

input = sys.stdin.readline


for _ in range(int(input())):
    n, m, L = map(int,input().split())
    hurdles = []
    for i in range(n):
        l, r = map(int,input().split())
        hurdles.append([l,r])
    power = []
    for i in range(m):
        x,v = map(int,input().split())
        power.append([x,v])
    
    jump = 1
    pq = []
    heapq.heapify(pq)
    j=0
    result = 0
    flag = True
    for i in range(n):
        l, r = hurdles[i]
        
        while(j<m):
            if power[j][0]<l:
                heapq.heappush(pq,-power[j][1])
                j+=1
            else:
                break

        while(pq and (r-l+2)>jump):
            jump+=abs(heapq.heappop(pq))
            result+=1

        if (r-l+2)>jump:
            flag = False
            break
    if flag:
        print(result)
    else:
        print(-1)



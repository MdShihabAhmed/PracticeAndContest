input = open('speeding.in', 'r').readline
fout = open('speeding.out', 'w')
print = lambda x: fout.write(str(x)+'\n')

N, M = map(int,input().split())
road = []
for _ in range(N):
    roadSegment, speedLimit = map(int,input().split())
    road.append([roadSegment, speedLimit])
road.append([float('inf'),float('inf')])
result = 0
tempRoad = 0
tempSpeed = 0
i=0

for _ in range(M):
    bessieJourney, bessieSpeed = map(int,input().split())
    if road[i][0]>=bessieJourney+tempRoad:
        result = max(result,max(bessieSpeed,tempSpeed)-road[i][1])
        road[i][0]-=bessieJourney+tempRoad
        tempRoad = 0
        tempSpeed = 0
        if road[i][0]==0:
            i+=1
    else:

        tempRoad+=bessieJourney
        result = max(result,max(bessieSpeed,tempSpeed)-road[i][1])
        tempSpeed = bessieSpeed
        while(road[i][0]<=tempRoad):
            result = max(result,tempSpeed-road[i][1])
            tempRoad-=road[i][0]
            i+=1
            
        if tempRoad==0:
            tempSpeed = 0


print(result)
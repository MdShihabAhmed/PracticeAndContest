import sys

input = sys.stdin.readline

n = int(input())
forward = [False]*n
backward = [False]*n
clock = 0
antiClock = 0
for i in range(n):
    a, b, c = map(int,input().split())
    
    if forward[a-1] or backward[b-1]:
        clock+=c
        forward[b-1]=True
        backward[a-1]=True
    else:
        antiClock+=c
        forward[a-1]=True
        backward[b-1]=True


print(min(clock,antiClock))


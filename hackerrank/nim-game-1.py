import sys
input = sys.stdin.readline

def nimGame(n,s):
    One = 0
    spareMoves = 0
    for i in s:
        if i==1:
            One+=1
        else:
            spareMoves+=(i-1)
    moves = n + spareMoves
    
    if n%2==0:
        if sparemoves%2:
            return "First"
        else:
            return "Second"
    else:
        pass



for _ in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    print(nimGame(n, s))
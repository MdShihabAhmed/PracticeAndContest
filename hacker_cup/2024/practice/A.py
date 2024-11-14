import sys

input = sys.stdin.readline

for test in range(int(input())):
    n, k = map(int,input().split())
    seconds = []
    for i in range(n):
        seconds.append(int(input()))
    
    seconds.sort()
    
    req = 0
    req+=(2*seconds[0])*(max(n-2,0))
    req+=seconds[0]

    if req<=k:
        print(f"Case #{test+1}: YES")
    else:
        print(f"Case #{test+1}: NO")
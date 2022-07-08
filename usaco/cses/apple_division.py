import sys

input = sys.stdin.readline

result = []
arr = []
def solver(s):
    if s<n:
        solver(s+1)
        arr.append(p[s])
        result.append(abs(sum(arr)*2-summ))
        solver(s+1)
        arr.pop()
    
    return 

for _ in range(1):
    n = int(input())
    p = list(map(int,input().split()))
    summ = sum(p)
    solver(0)
    print(min(result))
import sys

input = sys.stdin.readline

def solver(n):
    result = [i+1 for i in range(n)]
    
    for i in range(n-2,-1,-2):
        result[i],result[i+1] = result[i+1],result[i]
    
    print(*result)

for _ in range(int(input())):
    n = int(input())

    solver(n)
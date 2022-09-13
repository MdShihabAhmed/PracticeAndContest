import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    result = []
    for i in range(n-2,0,-1):
        result.append(i)
    
    result.append(n-1)
    result.append(n)
    
    if n%2:
        result[n-5:n-2] = [1, 3, 2]
    
    print(*result)


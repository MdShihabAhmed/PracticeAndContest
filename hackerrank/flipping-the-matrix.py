import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    matrix = []
    for i in range(2*n):
        arr = list(map(int,input().split()))
        matrix.append(arr)

    result = 0

    for i in range(n):
        for j in range(n):
            result+=max([matrix[i][j],matrix[i][2*n-1-j],matrix[2*n-1-i][j],matrix[2*n-1-i][2*n-1-j]])

    print(result)
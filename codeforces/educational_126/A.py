import sys
input = sys.stdin.readline

def solver(n, a, b):
    result = 0
    for i in range(n-1):
        result+=min((abs(a[i]-a[i+1])+abs(b[i]-b[i+1])),(abs(b[i]-a[i+1])+abs(a[i]-b[i+1])))

    return result

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    print(solver(n, a, b))
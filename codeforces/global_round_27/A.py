import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m, r, c = map(int,input().split())
    ma = (n-r)*(m)
    other = ((n-r)*m)+(m-c)-(n-r)
    print(ma+other)

    

    
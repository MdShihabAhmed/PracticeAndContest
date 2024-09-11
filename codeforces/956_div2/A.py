import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    print(" ".join(map(str,[i for i in range(1,n+1)])))
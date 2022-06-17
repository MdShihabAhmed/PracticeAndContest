import sys

input = sys.stdin.readline

def solver(n,s):
    return s//(n*n)


for _ in range(int(input())):
    n, s = map(int,input().split())

    print(solver(n,s))
import sys

input = sys.stdin.readline

def solver(n,a):
    a.sort()
    return a[-1]+a[-2]

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    print(solver(n,a))
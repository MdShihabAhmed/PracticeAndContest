import sys

input = sys.stdin.readline

def solver(n):
    return 2**n-1

for _ in range(int(input())):
    n = int(input())

    print(solver(n))
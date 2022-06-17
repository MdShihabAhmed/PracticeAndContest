import sys

input = sys.stdin.readline

def solver(n,a):

    result = a[0]
    for i in range(1,n):
        result = result | a[i]

    return result



for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    print(solver(n,a))
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    a.sort(reverse=True)
    print(a[(n-1)//2])
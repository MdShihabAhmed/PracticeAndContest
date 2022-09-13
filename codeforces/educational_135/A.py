import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    cnt = list(map(int,input().split()))

    print(cnt.index(max(cnt))+1)
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c = map(int,input().split())

    d = abs(b-c)+abs(c-1)
    a-=1
    if a>d:
        print(2)
    elif a<d:
        print(1)
    else:
        print(3)
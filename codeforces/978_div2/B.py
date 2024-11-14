import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x = map(int,input().split())
    a = list(map(int,input().split()))
    

    print(max((sum(a)+x-1)//x,max(a)))
    

    
import sys 

input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    print(int(round((10**10-1)/(100*k),0)))
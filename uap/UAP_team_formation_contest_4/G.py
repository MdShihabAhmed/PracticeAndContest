import sys

input = sys.stdin.readline

a, b, c = map(int,input().split())

print(max(0,(b+c)-a))
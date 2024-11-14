import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    if n&1:
        print("Kosuke")
    else:
        print("Sakurako")
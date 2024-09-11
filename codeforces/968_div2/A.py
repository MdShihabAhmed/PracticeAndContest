import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input().rstrip()
    if s[0]==s[-1]:
        print("NO")
    else:
        print("YES")


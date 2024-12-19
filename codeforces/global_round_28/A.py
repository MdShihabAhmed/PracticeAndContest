import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x = int(input())
    if x%33:
        print("NO")
    else:
        print("YES")

    

    
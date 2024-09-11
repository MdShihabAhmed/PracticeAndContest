import sys

input = sys.stdin.readline

for _ in range(int(input())):
    p, s, r = map(int,input().split())
    if p==s and r!=1:
        print(f"Case {_+1}: No")
    else:
        print(f"Case {_+1}: Yes")
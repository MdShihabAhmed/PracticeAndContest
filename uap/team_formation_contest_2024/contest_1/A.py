import sys

input = sys.stdin.readline

s = input().rstrip()
s = s.lower()

if "be" in s:
    print("yes")
else:
    print("no")
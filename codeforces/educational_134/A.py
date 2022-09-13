import sys
input = sys.stdin.readline

from collections import Counter

def solver(s):
    pass

for _ in range(int(input())):
    line1 = list(input().rstrip())
    line2 = list(input().rstrip())
    line = line1+line2

    ne = Counter(line)

    print(len(ne)-1)

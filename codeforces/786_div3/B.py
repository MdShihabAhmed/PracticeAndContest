import sys

input = sys.stdin.readline

def solver(s):
    first = ord(s[0])-96
    second = ord(s[1])-96
    if first<second:
        second-=1
    return (first-1)*25+second

for _ in range(int(input())):
    s = input().rstrip()

    print(solver(s))
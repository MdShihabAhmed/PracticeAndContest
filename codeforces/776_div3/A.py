import sys

input = sys.stdin.readline

def solver(s,c):
    n = len(s)
    for i in range(n):
        # print(s[i])
        if s[i]==c:
            # print(c)
            m = len(s[:i])
            if m%2==0 and (n-m+1)%2==0:
                return "YES"

    return "NO"

for _ in range(int(input())):
    s = input().rstrip()
    c = input().rstrip()

    print(solver(s,c))
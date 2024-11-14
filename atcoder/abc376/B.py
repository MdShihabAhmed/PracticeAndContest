import sys

input = sys.stdin.readline

n, q = map(int, input().split())

l = 1
r = 2
result = 0
for i in range(q):
    h, t = input().split()
    t = int(t)
    if h=='L':
        if t==l:
            continue
        if t>l:
            if (l<=r and r<=t):
                result+=(n-(t-l))
            else:
                result+=((t-l))
        else:
            if (t<=r and r<=l):
                result+=(n-(l-t))
            else:
                result+=((l-t))
        l = t
    elif h=='R':
        if t==r:
            continue
        if t>r:
            if (r<=l and l<=t):
                result+=(n-(t-r))
            else:
                result+=((t-r))
        else:
            if (t<=l and l<=r):
                result+=(n-(r-t))
            else:
                result+=((r-t))
        r = t
print(result)
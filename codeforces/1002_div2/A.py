import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    c = list(map(int,input().split()))
    d = list(map(int,input().split()))
    a = set()
    b = set()
    for num in c:
        a.add(str(num))
    for num in d:
        b.add(str(num))

    if len(a)>=3 or len(b)>=3:
        print("YES")
    elif len(a)==2 and len(b)==2:
        print("YES")
    else:
        print("NO")
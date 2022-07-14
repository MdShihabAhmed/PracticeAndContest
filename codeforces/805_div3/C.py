import sys
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
    e = input()
    n, k = map(int,input().split())
    u = list(map(int,input().split()))
    uDict = defaultdict(list)
    check = defaultdict(bool)
    for i in u:
        uDict[str(i)] = [float('inf'),-1]
        check[str(i)] = True
    for i in range(n):
        uDict[str(u[i])][0] = min(uDict[str(u[i])][0], i)
        uDict[str(u[i])][1] = max(uDict[str(u[i])][1], i)

    for i in range(k):
        a, b = map(int,input().split())
        flag = True
        if check[str(a)] and check[str(b)]:
            if uDict[str(a)][0]<=uDict[str(b)][1]:
                flag = False
                print('YES')
        if flag:
            print('NO')
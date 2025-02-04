import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int,input().split())
    cards =[]
    for i in range(n):
        temp = sorted(list(map(int,input().split())))
        cards.append(temp+[i])
    cards.sort()

    flag = True
    for i in range(1,n):
        for j in range(m):
            if cards[i-1][j]+1==cards[i][j]:
                continue
            else:
                flag = False
                break
        if not flag:
            break
    
    if flag:
        result = []
        for i in range(n):
            result.append(cards[i][-1]+1)
        print(*result)
    else:
        print(-1)


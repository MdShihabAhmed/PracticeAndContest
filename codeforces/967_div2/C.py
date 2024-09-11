import sys
from sys import stdout


input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    visit = [[0 for i in range(n+1)] for j in range(n+1)]
    result = ["!"]
    flag = False
    for i in range(1,n):
        for j in range(i+1,n+1):
            if i==j or visit[i][j] or visit[j][i]:
                continue
            a = i
            b = j
            stack = [0, a]
            while(stack):
                if visit[a][b] or visit[b][a]:
                    break
                print("?",a,b)
                stdout.flush()
                visit[a][b]=1
                visit[b][a]=1
                ans = int(input())
                if ans==-1:
                    flag = True
                    break
                if ans==a:
                    result.append(a)
                    result.append(b)
                    if stack:
                        b = stack.pop()
                    if stack:
                        a = stack.pop()
                else:
                    stack.append(ans)
                    a = ans

            if flag:
                break
        if flag:
            break
    print(" ".join(map(str,result)))
    stdout.flush()
    

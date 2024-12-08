import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int,input().split())
    le = 0
    re = []
    for i in range(n):
        temp = input().strip()
        re.append(temp)
    
    result = 0
    for temp in re:
        if le+len(temp)<=m:
            le+=len(temp)
            result+=1
        else:
            break
    
    print(result)
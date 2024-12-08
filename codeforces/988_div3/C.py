import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    if n<5:
        print(-1)
        continue
    result = [i for i in range(1,n+1,2)]
    result[2],result[-1]=result[-1],result[2]
    result.append(4)
    for i in range(2,n+1,2):
        if i==4:
            continue
        result.append(i)
    
    print(" ".join(map(str,result)))
    
    

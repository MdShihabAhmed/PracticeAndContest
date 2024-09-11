import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    result = l[-1]
    for i in range(n-2,-1,-1):
        if l[i]>l[i+1]:
            if (result<l[i]):
                result = l[i]
            else:
                result+=1
        else:
            result+=1
    print(result)

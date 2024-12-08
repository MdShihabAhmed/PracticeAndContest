import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    flag = False
    re = -1
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if (a[i]-a[j])%k==0:
                break
        else:
            flag = True
            re = i
            break
    if flag:
        print("YES")
        print(re+1)
    else:
        print("NO")

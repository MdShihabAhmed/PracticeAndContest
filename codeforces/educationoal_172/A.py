import sys

input = sys.stdin.readline


for _ in range(int(input())):
    n, k= map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    re = a[0]
    result = 0
    for i in range(1,n):
        if re+a[i]==k:
            re+=a[i]
            break
        if re+a[i]>k:
            result=k-re
            re+=(k-re)
            break
        re+=a[i]
    if re<k:
        result=k-re
    print(result)
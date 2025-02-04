import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))

    cnt = [0]*(n+1)
    for c in a:
        cnt[c]+=1

    result = 0
    for c in a:

        if cnt[c]>0 and (k-c<=n and k-c>=1 and cnt[k-c]>0):
            temp = min(cnt[c],cnt[k-c])
            if c==k-c:
                temp//=2
            result+=temp
            cnt[k-c]=0
        cnt[c]=0
    print(result)
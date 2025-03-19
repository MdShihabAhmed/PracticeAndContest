import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x, n, m = map(int,input().split())
    if 2**n -1 >=x:
        print(0,0)
        continue
    lo = x
    up = x
    i = 0
    j = 0
    cnt1 = 0
    while(True):
        cnt1+=1
        if (i>=n and j>=m) or cnt1>50:
            break
        temp = lo/2
        if temp==int(temp):
            if j<m:
                j+=1
            elif i<n:
                i+=1
            else:
                break
            lo = int(temp)
        else:
            if i<n:
                i+=1
                lo = int(temp)
            elif j<m:
                j+=1
                lo = int(temp) + 1
            else:
                break
    i = 0
    j = 0
    cnt2 = 0
    while(True):
        cnt2+=1
        if (i>=n and j>=m) or cnt2>50:
            break
        temp = up/2
        if temp==int(temp):
            if i<n:
                i+=1
            elif j<m:
                j+=1
            else:
                break
            up = int(temp)
        else:
            if j<m:
                j+=1
                up = int(temp) + 1
            elif i<n:
                i+=1
                up = int(temp)
            else:
                break
    
    print(lo, up)
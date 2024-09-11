import sys

input = sys.stdin.readline


for _ in range(int(input())):
    n, l, r = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    i = 0
    j = 0
    temp = a[j]
    while(i<=j and j<n):
        
        if temp>r and i<j:
            temp -= a[i]
            i+=1
        elif temp<l:
            j+=1
            if j<n:
                temp+=a[j]
        else:
            if temp>=l and temp<=r:
                ans+=1
                # print(temp,temp)
            j+=1
            i = j
            temp = 0
            if i<n:
                temp+=a[i]


        
    print(ans)


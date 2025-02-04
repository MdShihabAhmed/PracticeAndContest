import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a = list(map(int,input().split()))
    re = 0
    aa = a[::]
    aa.insert(2,a[0]+a[1])
    for i in range(3):
        if aa[i]+aa[i+1]==aa[i+2]:
            re+=1
    re1 = 0
    aa = a[::]
    aa.insert(2,a[-1]-a[-2])
    for i in range(3):
        if aa[i]+aa[i+1]==aa[i+2]:
            re1+=1
    
    print(max(re,re1))

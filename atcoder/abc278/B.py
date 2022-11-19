import sys

input = sys.stdin.readline

h, m = map(int, input().split())
hC = mC = 0
while(True):
    flag = False
    while(True):
        minV = (h%10)*10+m%10
        hV = h-h%10 + m//10
        if (hV<=23 and hV>=0) and (minV<=59 and minV>=0):
            print(h, m)
            flag = True
            break
        m = (m+1)%60
        if m==0:
            break
    if flag:
        break
    h = (h+1)%24
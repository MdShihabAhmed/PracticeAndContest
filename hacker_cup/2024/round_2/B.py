import sys

input = sys.stdin.readline
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 121, 232, 343, 454, 565, 676, 787, 898, 12321, 23432, 34543, 45654, 56765, 67876, 78987, 1234321, 2345432, 3456543, 4567654, 5678765, 6789876, 123454321, 234565432, 345676543, 456787654, 567898765, 12345654321, 23456765432, 34567876543, 45678987654, 1234567654321, 2345678765432, 3456789876543, 123456787654321, 234567898765432, 12345678987654321]


for test in range(int(input())):
    a, b, m = map(int,input().split())
    temp = a%m
    if temp:
        a+=(m-temp)
    temp = b%m
    if temp:
        b -= temp
    result = 0
    start = max(a,m)
    end = b

    result = 0
    for num in range(start,end+1,m):
        sNum = str(num)
        l = len(sNum)
        if l%2==0:
            continue
        if l==1 and sNum!='0':
            result+=1
            continue
        flag = True
        if sNum[l//2-1]=='0' or sNum[l//2+1]=='0' or sNum[l//2-1]>=sNum[l//2] or sNum[l//2+1]>=sNum[l//2]:
            flag = False
        if flag:
            for i in range(1,l//2):
                if sNum[i]=='0' or sNum[i-1]=='0':
                    flag = False
                    break
                if sNum[i]<sNum[i-1]:
                    flag =False
                    break
        if flag:
            for i in range(l//2+2,l):
                if sNum[i]=='0' or sNum[i-1]=='0':
                    flag = False
                    break
                if sNum[i-1]<sNum[i]:
                    flag =False
                    break
        if flag:
            result+=1

    print(f"Case #{test+1}: {result}")
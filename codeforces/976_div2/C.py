import sys

input = sys.stdin.readline

for _ in range(int(input())):
    b,c,d = map(int,input().split())

    bb = bin(b)
    cc = bin(c)
    dd = bin(d)
    m = max(len(bb),len(cc),len(dd))
    # print(bb,cc,dd,m)
    bb = bb[:2]+'0'*(m-(len(bb)))+bb[2:]
    cc = cc[:2]+'0'*(m-(len(cc)))+cc[2:]
    dd = dd[:2]+'0'*(m-(len(dd)))+dd[2:]
    # print(bb,cc,dd,m)
    a = []
    flag = False 
    for i in range(m-1,1,-1):
        if (1 | int(bb[i]))-int(dd[i])==(1 & int(cc[i])):
            a.append(1)
        elif (0 | int(bb[i]))-int(dd[i])==(0 & int(cc[i])):
            a.append(0)
        else:
            flag = True
            break
    if flag or len(a)>61:
        print(-1)
    else:
        result = 0
        for i in range(len(a)):
            if a[i]:
                result+=(2**i)
        
        print(result)
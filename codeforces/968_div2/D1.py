import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n,m = map(int,input().split())
    x = 0
    for i in range(n):
        temp = list(map(int,input().split()))
        temp2 = list(set(temp[1:]))
        temp2.sort()
        temp[0] = len(temp2)
        off = 0
        j = 0
        while(j<temp[0]):
            if temp2[j]==j+off:
                j+=1
                continue
            x = max(x,j+off)
            off+=1
            if off>=2:
                break
        if off<1:
            x = max(x,j,j+1)
        elif off<2:
            x = max(x,j+off)
    
    first =(x*min(x+1,m+1))
    second = (max(m-x,0)*(2*(x+1)+max(m-x,0)-1))//2
    # print(x,first,second,off)
    print(first+second)

    
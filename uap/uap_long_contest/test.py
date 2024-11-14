import sys 

input = sys.stdin.readline

for _ in range(int(input())):
    n, k, z = map(int,input().split())
    a = list(map(int,input().split()))


    pre = [0]
    for i in range(k+1):
        pre.append(a[i]+pre[-1])

    
    re = pre[-1]
    print(pre)
    for i in range(2,k+2):
        zz = z
        current = pre[i]-pre[i-2]

        remains = (k+1-i)
        valid = min(zz,(remains)//2)

        result =valid*current
        print(i,result)
        zz-=valid
        remains-=(valid*2)
        temp2 = pre[i+remains]

        temp1 =0
        print(i+remains)
        if remains and zz:
            temp1+=pre[i+remains-1]
            if i+remains-2>=0:
                temp1 = max(temp1, a[i+remains-2])
        result+=max(temp1,temp2)
        print(remains,result,zz,re)
        
        re = max(result, re)
    print(re)

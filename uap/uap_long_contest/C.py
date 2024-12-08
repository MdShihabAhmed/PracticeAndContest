import sys 

input = sys.stdin.readline

for _ in range(int(input())):
    n, k, z = map(int,input().split())
    a = list(map(int,input().split()))
    pre = [0]
    
    for i in range(k+1):
        pre.append(a[i]+pre[-1])

    result = pre[-1]
    # print(pre)
    for i in range(1,k+2):
        for j in range(1,z+1):
            temp = (k-(j)*2)
            if temp+1>=i:
                result = max(result, (pre[i+1]-pre[i-1])*(j)+pre[temp+1])
                # print(result,temp,i,j,(pre[i+1]-pre[i-1]),pre[temp+1])
    
    print(result)
        



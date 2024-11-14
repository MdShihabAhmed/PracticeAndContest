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
    for i in range(2,k+2):
        for j in range(z):
            temp = k+1-(j+1)*2
            if temp<=len(pre) and temp>=i:
                result = max(result, (pre[i]-pre[i-2])*(j+1)+pre[temp])
                # print(result,i,j,(pre[i]-pre[i-2])*(j+1)+pre[temp])
    
    print(result)
        



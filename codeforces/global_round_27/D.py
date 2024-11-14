import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    pre = [0]

    m = a[i]
    twos = 0
    result = []
    for i in range(n):
        m = max(m,a[i])
        result.append(pre[i]-m+(m*(2**twos)))

        temp = a[i]
        while(temp%2==0):
            temp//=2
            twos+=1
        pre.append(pre[-1]+temp)
    
    print(" ".join(map(str,result)))
    
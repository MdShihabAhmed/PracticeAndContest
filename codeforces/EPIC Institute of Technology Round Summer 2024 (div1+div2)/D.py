import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    count = [0 for i in range(n+1)]
    for i in range(n):
        count[a[i]]+=1

    final = []
    for i in range(n):
        final.append([count[a[i]],a[i]])
    
    a.sort()
    final.sort()
    flagA = dict()
    for i in range(n):
        flagA[a[i]] = False
    i = 0
    j = 0
    flag = True
    stepB = 0
    result = 0
    while(i<n):
        if flag:
            if not flagA[a[i]] and count[a[i]]:
                result+=1
                flag = False
                flagA[a[i]] = True
                stepB+=1
            i+=1
        elif j<n:
            if flagA[final[j][1]]:
                j+=1
            elif count[final[j][1]]<=stepB:
                flag = True
                stepB -= count[final[j][1]]
                count[final[j][1]] = 0
                j+=1
            else:
                flag = True
        elif not flag:
            i+=1
            flag = True
        else:
            break

    print(result)
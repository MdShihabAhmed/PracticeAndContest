import sys
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int,input().split())

    dd = defaultdict(list)
    
    for i in range(m):
        a,d,k = map(int,input().split())
        dd[a%d].append([a,a+d*k,k+1,d])
    # print(dd)
    result = n
    for key,val in dd.items():
        if len(val)<1:
            continue
        temp = sorted(val)
        print("temp",temp)
        start = temp[0][0]
        end = temp[0][1]
        tempResult = temp[0][2]
        for i in range(1,len(temp)):
            if end>=temp[i][0]:
                end = max(end,temp[i][1])
                tempResult += (temp[i][2]-1)
            else:
                result-=max(0,(tempResult-1))
                print(result)
                start = temp[i][0]
                end = temp[i][1]
                tempResult = temp[i][2]
        
        # print(tempResult,val[j])
        result-=max(0,(tempResult-1))
        print(result)
            
    print(result)
    print()
import sys
import heapq

input = sys.stdin.readline


for _ in range(int(input())):
    s = list(input().strip())
    n = len(s)
    for i in range(n):
        number = int(s[i])
        if number==0:
            continue
        tempVal = number
        flag = False 
        tempIndex = -1
        for j in range(i-1,-1,-1):
            if number-(i-j)<=0:
                break
            if number-(i-j)>int(s[j]):
                tempVal = number-(i-j)
                tempIndex = j
                flag = True
        
        if flag:
            for k in range(i,tempIndex,-1):
                s[k]=s[k-1]
            s[tempIndex]=str(tempVal)
            # print(s)
    
    print("".join(s))